# LLM630 Compute Kit - StackFlow API Yolo11n Demo

本案例将演示通过在 LLM630 Compute Kit 设备上运行脚本程序，通过 StackFlow 的 API 接口获取 yolo 的检测数据，并打印至终端。

## 1. 准备工作

1. 按照下图接线方式，在设备上电前通过 FPC 排线连接 CamModule SC850SL 摄像头 和 LLM630 Compute Kit

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_01.jpg" width="70%" />

1. 参考[LLM630 Compute Kit UART / ADB / SSH 连接调试](/zh_CN/stackflow/llm630_compute_kit/config)教程，学习如何为 LLM630 Compute Kit 配置网络与文件传输，并获取设备 IP 地址。
2. 参考[LLM630 Compute Kit 软件包更新教程](/zh_CN/stackflow/llm630_compute_kit/software)，完成以下模型包和软件包的安装。

```shell
apt install llm-camera llm-yolo # SoftWare Package
```

\#> 注意事项 | CSI Camera 使用了 AI-ISP，在暗光下有非常好的成像效果，会使用一半的 NPU 算力用于 AI-ISP。默认的 YOLO 模型无法在开启 AI-ISP 模式下使用，需要通过以下命令安装支持 AI-ISP 的 YOLO 模型。

```shell
apt install llm-model-yolo11n-npu1 llm-model-yolo11n-pose-npu1 llm-model-yolo11n-hand-pose-npu1 # Model Package
```

## 2. 客户端程序

下载客户端测试脚本，确保 PC 与 LLM630 Compute Kit 处于同一网段下。
复制并保存下方脚本，如果选择在电脑上运行，运行时需传入 LLM630 Compute Kit 实际的 IP 地址参数。

```bash
python llm-yolo.py --host 192.168.20.24
```

如果选择在设备上直接运行，需要将代码文件上传到 LLM630 Compute Kit 运行时无需传入 IP 地址参数。

```shell
adb push llm-yolo.py /root
```

```shell
adb shell
```

```shell
cd /root
python3 llm-yolo.py
```

```python
import argparse
import json
import select
import socket
import sys
import time
import platform

if platform.system() == "Windows":
    import msvcrt


def create_tcp_connection(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock


def send_json(sock, data):
    json_data = json.dumps(data, ensure_ascii=False) + '\n'
    sock.sendall(json_data.encode('utf-8'))


recv_buffer = ""

def receive_response(sock):
    global recv_buffer
    while '\n' not in recv_buffer:
        part = sock.recv(4096).decode('utf-8')
        if not part:
            break
        recv_buffer += part
    if '\n' in recv_buffer:
        line, recv_buffer = recv_buffer.split('\n', 1)
        return line.strip()
    else:
        line, recv_buffer = recv_buffer, ""
        return line.strip()

def close_connection(sock):
    if sock:
        sock.close()


def create_init_data(response_format, deivce, enoutput, frame_height, frame_width, enable_webstream, rtsp):
    return {
        "request_id": "camera_001",
        "work_id": "camera",
        "action": "setup",
        "object": "camera.setup",
        "data": {
            "response_format": "image.yuvraw.base64" if response_format =="yuv" else "image.jpeg.base64",
            "input": deivce,
            "enoutput": enoutput,
            "frame_width": frame_width,
            "frame_height": frame_height,
            "enable_webstream": enable_webstream,
            "rtsp": "rtsp.1280x720.h265" if rtsp == "h265" else "rtsp.1280x720.h264",
        }
    }


def parse_setup_response(response_data):
    error = response_data.get('error')
    if error and error.get('code') != 0:
        print(f"Error Code: {error['code']}, Message: {error['message']}")
        return None

    return response_data.get('work_id')


def reset(sock):
    sent_request_id = 'reset_000'
    reset_data = {
        "request_id": sent_request_id,
        "work_id": "sys",
        "action": "reset"
    }
    ping_data = {
        "request_id": "ping_000",
        "work_id": "sys",
        "action": "ping"
    }
    send_json(sock, reset_data)
    while True:
        try:
            send_json(sock, ping_data)
            time.sleep(1)
        except (BrokenPipeError, ConnectionResetError, OSError) as e:
            return # Sock disconnection indicates reset is complete


def setup(sock, init_data):
    sent_request_id = init_data['request_id']
    send_json(sock, init_data)
    while True:
        response = receive_response(sock)
        response_data = json.loads(response)
        if response_data.get('request_id') == sent_request_id:
            return parse_setup_response(response_data)


def exit_session(sock, deinit_data):
    send_json(sock, deinit_data)
    print("Exit")


def parse_inference_response(response_data):
    error = response_data.get('error')
    if error and error.get('code') != 0:
        print(f"Error Code: {error['code']}, Message: {error['message']}")
        return None

    return {
        "work_id": response_data.get("work_id"),
        "object": response_data.get("object"),
        "data": response_data.get("data")
    }


def parse_yolo_result(data):
    results = []
    for item in data:
        bbox = [float(x) for x in item.get('bbox', [])]
        kps = [float(x) for x in item.get('kps', [])]
        cls = item.get('class', '')
        conf = float(item.get('confidence', 0))
        results.append({
            'bbox': bbox,
            'class': cls,
            'confidence': conf,
            'kps': kps
        })
    return results


def main(args):
    sock = create_tcp_connection(args.host, args.port)

    frame_width, frame_height = args.imgsz

    try:
        print("Reset...")
        reset(sock)
        close_connection(sock)
        sock = create_tcp_connection(args.host, args.port)

        print("Setup Camera...")
        init_data = create_init_data(
            response_format = args.format,
            enoutput=args.enoutput,
            deivce=args.device,
            frame_height=frame_height,
            frame_width=frame_width,
            enable_webstream=args.webstream,
            rtsp=args.rtsp
        )
        camera_work_id = setup(sock, init_data)
        if camera_work_id is not None:
            print(f"Camera setup with work_id: {camera_work_id}")
        else:
            print("Camera setup failed.")
            return

        print("Setup Yolo...")
        yolo_init_data = {
            "request_id": "yolo_001",
            "work_id": "yolo",
            "action": "setup",
            "object": "yolo.setup",
            "data": {
                "model": args.model,
                "response_format": "yolo.box",
                "input":  camera_work_id,
                "enoutput": True,
            }
        }
        yolo_work_id = setup(sock, yolo_init_data)
        if yolo_work_id is not None:
            print(f"Yolo setup with work_id: {yolo_work_id}")
        else:
            print("Yolo setup failed.")
            return

        while True:
            if platform.system() == "Windows":
                if msvcrt.kbhit():
                    key = msvcrt.getwch()
                    if key == 'q':
                        print("Quit by user.")
                        break
            else:
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    key = sys.stdin.readline().strip()
                    if key == 'q':
                        print("Quit by user.")
                        break

            response = receive_response(sock)
            if not response:
                continue
            response_data = json.loads(response)

            Rawdata = parse_inference_response(response_data)
            if Rawdata is None:
                break

            work_id = Rawdata.get("work_id")
            object = Rawdata.get("object")
            data = Rawdata.get("data")

            if work_id == yolo_work_id and object == "yolo.box":
                yolo_results = parse_yolo_result(data)
                print(f"YOLO Results: {yolo_results}")

        exit_session(sock, {
            "request_id": "yolo_exit",
            "work_id": yolo_work_id,
            "action": "exit"
        })
        exit_session(sock, {
            "request_id": "camera_exit",
            "work_id": camera_work_id,
            "action": "exit"
        })
        time.sleep(3) # Allow time for the exit command to be processed
    finally:
        close_connection(sock)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP Client to send JSON data.")
    parser.add_argument("--host", type=str, default="localhost", help="Server hostname (default: localhost)")
    parser.add_argument("--port", type=int, default=10001, help="Server port (default: 10001)")
    parser.add_argument("--device", type=str, default="axera_single_sc850sl", help="Camera name, i.e. axera_single_sc850sl or /dev/video0")
    parser.add_argument("--enoutput", type=bool, default=False, help="Whether to output image data")
    parser.add_argument("--format", "--output-format", type=str, default="yuv", help="Output image data format, i.e. jpeg or yuv")
    parser.add_argument("--imgsz", "--img", "--img-size", nargs="+", type=int, default=[320, 320], help="image (h, w)")
    parser.add_argument("--webstream", action="store_true", help="Enable webstream")
    parser.add_argument("--rtsp", default="h264", help="rtsp output, i.e. h264 or h265")
    parser.add_argument("--model", type=str, default="yolo11n-npu1", help="Model name, i.e. yolo11n-npu1 or yolo11n-pose-npu1, yolo11n-hand-pose-npu1")


    args = parser.parse_args()
    main(args)
```

### 参数解析

- **host**：LLM630 Compute Kit 的 IP 地址
- **port**：TCP 通信端口，默认 10001
- **device**：摄像头名称，MIPI CSI 摄像头为 'axera_single_sc850sl'，如果使用 USB video camera，根据实际设备填写。例如 '/dev/video0'
- **enoutput**：是否输出图像数据，默认关闭
- **format**：输出的图像格式，默认 'yuv'，可以选择 'jpeg'
- **imgsz**：输出的图像尺寸，默认 '320\*320'
- **webstream**：是否开启网页浏览，默认关闭，打开后，浏览器访问 'http://IP:8989/' 即可访问，注意 IP 替换为 LLM630 Compute Kit 的 IP 地址
- **rtsp**：输出的 rstp 视频流编码，默认 'h264'，可以选择 'h265'
- **model**：加载的 yolo 模型，默认 'yolo11n-npu1'，可以选择 'yolo11n-pose-npu1' 或 'yolo11-hand-pose-npu1'

## 3. 开始交互

终端将打印 yolo 检测结果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_yolo11n_print_01.jpg" width="100%" />
