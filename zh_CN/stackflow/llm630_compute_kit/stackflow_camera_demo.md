# LLM630 Compute Kit - StackFlow API Camera Demo

本案例将演示通过在 PC 端上运行脚本程序，通过 StackFlow 的 API 接口获取摄像头数据和显示。

## 1. 准备工作

1. 按照下图接线方式，在设备上电前通过 FPC 排线连接 CamModule SC850SL 摄像头 和 LLM630 Compute Kit

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_01.jpg" width="70%" />

2. 参考[LLM630 Compute Kit UART / ADB / SSH 连接调试](/zh_CN/stackflow/llm630_compute_kit/config)教程，学习如何为 LLM630 Compute Kit 配置网络与文件传输，并获取设备 IP 地址。
3. 参考[LLM630 Compute Kit 软件包更新教程](/zh_CN/stackflow/llm630_compute_kit/software)，完成以下软件包的安装。

```shell
apt install llm-camera
```

## 2. 客户端程序

下载客户端测试脚本，确保 PC 与 LLM630 Compute Kit 处于同一网段下。PC 端需准备 Python 环境并通过 Pip 包管理器安装 `opencv-python` 依赖包。

```shell
pip install opencv-python
```

```shell
pip install opencv-python -i https://mirrors.aliyun.com/pypi/simple # For Chinese users
```

复制并保存下方脚本，并运行时候传入设备实际的 IP 地址参数。

```shell
python llm-camera.py --host 192.168.20.24
```

```python
import socket
import json
import argparse
import base64
import numpy as np
import cv2
import time

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
            "VinParam.bAiispEnable": 0,
            "rtsp": "rtsp.1280x720.h265" if rtsp == "h265" else "rtsp.1280x720.h264",
        }
    }


def parse_setup_response(response_data, sent_request_id):
    error = response_data.get('error')
    request_id = response_data.get('request_id')

    if request_id != sent_request_id:
        print(f"Request ID mismatch: sent {sent_request_id}, received {request_id}")
        return None

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
            return


def setup(sock, init_data):
    sent_request_id = init_data['request_id']
    send_json(sock, init_data)
    response = receive_response(sock)
    response_data = json.loads(response)
    return parse_setup_response(response_data, sent_request_id)


def exit_session(sock, deinit_data):
    send_json(sock, deinit_data)
    print("Exit")


def parse_inference_response(response_data):
    error = response_data.get('error')
    if error and error.get('code') != 0:
        print(f"Error Code: {error['code']}, Message: {error['message']}")
        return None

    return response_data.get('data')


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
        print("Setup Camera finished.")

        while True:
            response = receive_response(sock)
            if not response:
                continue
            response_data = json.loads(response)

            data = parse_inference_response(response_data)
            if data is None:
                break

            decoded = base64.b64decode(data)
            if args.format == "yuv":
                yuv_frame = np.frombuffer(decoded, dtype=np.uint8).reshape((frame_height, frame_width, 2))
                bgr_frame = cv2.cvtColor(yuv_frame, cv2.COLOR_YUV2BGR_YUY2)
            else:
                jpg_array = np.frombuffer(decoded, dtype=np.uint8)
                bgr_frame = cv2.imdecode(jpg_array, cv2.IMREAD_COLOR)

            cv2.imshow("Camera Frame", bgr_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

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
    parser.add_argument("--enoutput", type=bool, default=True, help="Whether to output image data")
    parser.add_argument("--format", "--output-format", type=str, default="jpeg", help="Output image data format, i.e. jpeg or yuv")
    parser.add_argument("--imgsz", "--img", "--img-size", nargs="+", type=int, default=[320, 320], help="image (h, w)")
    parser.add_argument("--webstream", action="store_true", help="Enable webstream")
    parser.add_argument("--rtsp", default="h264", help="rtsp output, i.e. h264 or h265")


    args = parser.parse_args()
    main(args)
```

### 参数解析

- **host**：LLM630 Compute Kit 的 IP 地址
- **port**：TCP 通信端口，默认 10001
- **device**：摄像头名称，MIPI CSI 摄像头为 'axera_single_sc850sl'，如果使用 USB video camera，根据实际设备填写。例如 '/dev/video0'
- **enoutput**：是否输出图像数据，默认开启
- **format**：输出的图像格式，默认 'jpeg'，可以选择 'yuv'
- **imgsz**：输出的图像尺寸，默认 '320*320'，可以选择 '480*480'
- **webstream**：是否开启网页浏览，默认关闭，打开后，浏览器访问 'http://IP:8989/' 即可访问，注意 IP 替换为 LLM630 Compute Kit 的 IP 地址
- **rtsp**：输出的 rstp 视频流编码，默认 'h264'，可以选择 'h265'

## 3. 开始交互

电脑屏幕将显示摄像头画面，如下图所示。按下键盘按键 “q” 可退出。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_02.jpg" width="100%" />
