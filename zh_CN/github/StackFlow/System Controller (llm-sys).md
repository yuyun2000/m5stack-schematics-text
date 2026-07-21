StackFlow System Controller (llm-sys)

# System Controller (llm-sys)

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [projects/llm_framework/main_sys/include/zmq_bus.h](projects/llm_framework/main_sys/include/zmq_bus.h)
- [projects/llm_framework/main_sys/src/event_loop.cpp](projects/llm_framework/main_sys/src/event_loop.cpp)
- [projects/llm_framework/main_sys/src/serial_com.cpp](projects/llm_framework/main_sys/src/serial_com.cpp)
- [projects/llm_framework/main_sys/src/tcp_com.cpp](projects/llm_framework/main_sys/src/tcp_com.cpp)
- [projects/llm_framework/main_sys/src/zmq_bus.cpp](projects/llm_framework/main_sys/src/zmq_bus.cpp)

</details>



## Purpose and Scope

The System Controller (`llm-sys`) is the central coordinator and entry point for the StackFlow LLM framework. It serves as the primary interface between external clients and internal AI units, managing command routing, system-level operations, and inter-process communication infrastructure.

This page documents the architecture, command dispatcher, external interfaces (UART/TCP), and system-level RPC functions provided by `llm-sys`. For information about the underlying ZMQ communication patterns and StackFlow base class functionality, see [StackFlow and pzmq Communication](#2.1). For details on unit lifecycle management and RPC protocol, see [RPC and Unit Management](#2.3).

**Sources:** [projects/llm_framework/main_sys/src/event_loop.cpp:1-844]()

---

## Architecture Overview

The `llm-sys` component acts as a bridge between external clients (UART/TCP) and internal AI processing units. It implements a multi-threaded event dispatcher that parses incoming JSON-RPC requests, routes them to appropriate handlers, and manages bidirectional communication with all StackFlow units.

```mermaid
graph TB
    subgraph "External Clients"
        UART["UART Interface<br/>/dev/ttyS*<br/>115200 baud"]
        TCP["TCP Server<br/>Port 10001<br/>hv::TcpServer"]
    end
    
    subgraph "llm-sys Core Components"
        SERIAL["serial_com<br/>zmq_bus_com"]
        TCPCOM["tcp_com<br/>zmq_bus_com"]
        DISPATCHER["unit_action_match()<br/>Command Dispatcher"]
        HANDLERS["System Handlers<br/>sys_ping, sys_hwinfo<br/>sys_unit_call, etc."]
        KVSTORE["Key-Value Store<br/>SAFE_READING/SETTING"]
    end
    
    subgraph "ZMQ Communication Layer"
        ZMQPULL["ZMQ PULL Socket<br/>ipc:///tmp/llm_zmq_c_*"]
        ZMQPUSH["ZMQ PUSH Sockets<br/>Per-client channels"]
        UNITPUB["Unit PUB Sockets<br/>zmq_bus_publisher_push"]
    end
    
    subgraph "StackFlow Units"
        UNITS["llm-audio<br/>llm-kws<br/>llm-asr<br/>llm-llm<br/>llm-tts<br/>..."]
    end
    
    UART --> SERIAL
    TCP --> TCPCOM
    
    SERIAL --> ZMQPULL
    TCPCOM --> ZMQPULL
    
    ZMQPULL --> DISPATCHER
    DISPATCHER --> HANDLERS
    DISPATCHER --> UNITPUB
    
    HANDLERS --> KVSTORE
    HANDLERS --> ZMQPUSH
    
    ZMQPUSH --> SERIAL
    ZMQPUSH --> TCPCOM
    
    SERIAL --> UART
    TCPCOM --> TCP
    
    UNITPUB --> UNITS
    UNITS -.->|unit_call| HANDLERS
```

**Sources:** [projects/llm_framework/main_sys/src/event_loop.cpp:743-762](), [projects/llm_framework/main_sys/src/zmq_bus.cpp:26-138](), [projects/llm_framework/main_sys/include/zmq_bus.h:43-77]()

---

## External Communication Interfaces

### UART Interface

The UART interface provides serial communication for embedded deployments. The `serial_com` class extends `zmq_bus_com` and implements a blocking read loop with JSON message parsing.

| Parameter | Configuration Key | Default Value |
|-----------|-------------------|---------------|
| Device Path | `config_serial_dev` | `/dev/ttyS*` |
| Baud Rate | `config_serial_baud` | `115200` |
| Data Bits | `config_serial_data_bits` | `8` |
| Stop Bits | `config_serial_stop_bits` | `1` |
| Parity | `config_serial_parity` | `0` (None) |
| ZMQ Port | `config_serial_zmq_port` | Internal routing |

```mermaid
sequenceDiagram
    participant Client as "External Device<br/>(UART)"
    participant SerialCom as "serial_com<br/>Thread"
    participant Parser as "select_json_str()"
    participant Dispatcher as "unit_action_match()"
    participant Handler as "sys_* Handler"
    
    Client->>SerialCom: "JSON bytes via UART"
    SerialCom->>SerialCom: "linux_uart_read()"
    SerialCom->>Parser: "Raw byte stream"
    
    Note over Parser: "Accumulate until<br/>valid JSON object"
    Parser->>Parser: "Track { } braces<br/>json_str_flage_"
    Parser->>Dispatcher: "Complete JSON string"
    
    Dispatcher->>Dispatcher: "simdjson parse<br/>extract action/work_id"
    Dispatcher->>Handler: "sys_* function call"
    Handler->>SerialCom: "zmq_com_send()"
    SerialCom->>Client: "JSON response via UART"
```

The UART interface supports dynamic reconfiguration through the `sys.uartsetup` command, which updates parameters in the key-value store and restarts the serial connection without restarting the entire service.

**Sources:** [projects/llm_framework/main_sys/src/serial_com.cpp:28-128](), [projects/llm_framework/main_sys/src/event_loop.cpp:83-101]()

### TCP Interface

The TCP interface uses the `libhv` networking library to provide concurrent client connections. Each connected client receives a dedicated ZMQ communication channel with a unique port identifier.

```mermaid
graph LR
    subgraph "TCP Server - Port 10001"
        LISTENER["hv::TcpServer<br/>Main Listener"]
    end
    
    subgraph "Client Connections"
        CLIENT1["Client 1<br/>tcp_com instance<br/>ZMQ port 8000"]
        CLIENT2["Client 2<br/>tcp_com instance<br/>ZMQ port 8001"]
        CLIENT3["Client N<br/>tcp_com instance<br/>ZMQ port 800N"]
    end
    
    subgraph "ZMQ Routing"
        ZMQ["ZMQ PULL/PUSH<br/>per-client channels"]
    end
    
    LISTENER -->|"onConnection()"| CLIENT1
    LISTENER -->|"onConnection()"| CLIENT2
    LISTENER -->|"onConnection()"| CLIENT3
    
    CLIENT1 <-->|"ipc:///tmp/llm_zmq_c_8000"| ZMQ
    CLIENT2 <-->|"ipc:///tmp/llm_zmq_c_8001"| ZMQ
    CLIENT3 <-->|"ipc:///tmp/llm_zmq_c_800N"| ZMQ
```

The port counter (`counter_port`) starts at 8000 and increments for each new connection, wrapping back to 8000 after reaching 65535. This ensures that each client has a unique ZMQ channel identifier for bidirectional communication.

**Sources:** [projects/llm_framework/main_sys/src/tcp_com.cpp:30-113](), [projects/llm_framework/main_sys/src/zmq_bus.cpp:179-186]()

---

## Command Dispatcher

The `unit_action_match` function is the central routing logic that processes all incoming JSON-RPC requests. It uses `simdjson` for high-performance JSON parsing and maintains thread safety with a mutex lock.

### Dispatcher Flow

```mermaid
flowchart TD
    START["unit_action_match()"]
    PARSE["simdjson parse<br/>Extract request_id, work_id, action"]
    CHECKERR{"Parse<br/>error?"}
    FRAGMENT["Split work_id by '.'<br/>work_id_fragment[]"]
    
    ACTIONTYPE{"action<br/>type?"}
    INFERENCE["action == 'inference'"]
    SYSCMD["work_id[0] == 'sys'"]
    REMOTE["Other work_id"]
    
    ZMQPUSH["Construct zmq_com URL<br/>Add to inference_raw_data"]
    BUSPUSH["zmq_bus_publisher_push()"]
    
    LOOKUP["Lookup sys.* function<br/>key_sql map"]
    SYSFUNC{"Function<br/>exists?"}
    CALLFUNC["call_fun(com_id, json_obj)"]
    
    REMOTECALL["remote_call()"]
    REMOTESUCCESS{"Success?"}
    
    ERROR["usr_print_error()"]
    END["Return"]
    
    START --> PARSE
    PARSE --> CHECKERR
    CHECKERR -->|"Yes"| ERROR
    CHECKERR -->|"No"| FRAGMENT
    FRAGMENT --> ACTIONTYPE
    
    ACTIONTYPE -->|"'inference'"| INFERENCE
    ACTIONTYPE -->|"sys.*"| SYSCMD
    ACTIONTYPE -->|"unit.*"| REMOTE
    
    INFERENCE --> ZMQPUSH
    ZMQPUSH --> BUSPUSH
    BUSPUSH --> END
    
    SYSCMD --> LOOKUP
    LOOKUP --> SYSFUNC
    SYSFUNC -->|"Yes"| CALLFUNC
    SYSFUNC -->|"No"| ERROR
    CALLFUNC --> END
    
    REMOTE --> REMOTECALL
    REMOTECALL --> REMOTESUCCESS
    REMOTESUCCESS -->|"No"| ERROR
    REMOTESUCCESS -->|"Yes"| END
    
    ERROR --> END
```

**Sources:** [projects/llm_framework/main_sys/src/event_loop.cpp:767-844]()

### JSON Parsing Strategy

The dispatcher uses three-tier parsing for performance:

1. **Fast Path**: `simdjson` streaming parser extracts `request_id`, `work_id`, and `action` fields without full deserialization [event_loop.cpp:768-802]()
2. **Lazy Parsing**: Full JSON object (`nlohmann::json`) created only when needed by handlers [event_loop.cpp:835]()
3. **Raw String**: For `inference` action, raw JSON passed directly to units to minimize overhead [event_loop.cpp:815-829]()

### Action Routing Logic

| Condition | Route Destination | Function Called |
|-----------|------------------|-----------------|
| `action == "inference"` | Unit's ZMQ PUB socket | `zmq_bus_publisher_push()` |
| `work_id[0] == "sys"` | System handler | `key_sql[unit_action]()` |
| Other `work_id` | Remote unit RPC | `remote_call()` |

**Sources:** [projects/llm_framework/main_sys/src/event_loop.cpp:815-843]()

---

## System RPC Functions

The `llm-sys` unit provides 16 system-level RPC functions accessible via the `sys.*` namespace. All functions are registered in the `key_sql` map during initialization.

### System Function Registry

```mermaid
graph TB
    REGISTRY["key_sql Map<br/>std::map&lt;std::string, sys_fun_call&gt;"]
    
    REGISTRY --> PING["sys.ping<br/>Connection test"]
    REGISTRY --> HWINFO["sys.hwinfo<br/>CPU/Memory/Temp"]
    REGISTRY --> CMMINFO["sys.cmminfo<br/>NPU memory info"]
    REGISTRY --> LSMODE["sys.lsmode<br/>List configurations"]
    REGISTRY --> RMMODE["sys.rmmode<br/>Remove package"]
    REGISTRY --> LSTASK["sys.lstask<br/>Reserved"]
    REGISTRY --> PUSH["sys.push<br/>File upload"]
    REGISTRY --> PULL["sys.pull<br/>File download"]
    REGISTRY --> UPDATE["sys.update<br/>Find update files"]
    REGISTRY --> UPGRADE["sys.upgrade<br/>Install packages"]
    REGISTRY --> BASHEXEC["sys.bashexec<br/>Execute shell"]
    REGISTRY --> UARTSETUP["sys.uartsetup<br/>Reconfigure UART"]
    REGISTRY --> RESET["sys.reset<br/>Restart services"]
    REGISTRY --> REBOOT["sys.reboot<br/>System reboot"]
    REGISTRY --> VERSION["sys.version<br/>Framework version"]
    REGISTRY --> VERSION2["sys.version2<br/>Binary versions"]
    REGISTRY --> UNITCALL["sys.unit_call<br/>Forward to unit"]
```

**Sources:** [projects/llm_framework/main_sys/src/event_loop.cpp:743-762]()

### Core System Functions

#### `sys.ping` - Connectivity Test

Simple echo function that returns success immediately. Used for connection verification and latency measurement.

**Implementation:** [event_loop.cpp:76-81]()

---

#### `sys.hwinfo` - Hardware Information

Collects system metrics including CPU load, memory usage, temperature, and network interface status. Runs in a detached thread to avoid blocking the dispatcher.

| Metric | Source | Units |
|--------|--------|-------|
| Temperature | `/sys/class/thermal/thermal_zone0/temp` | Millidegrees |
| CPU Load | `/proc/stat` (1-second sample) | Percentage |
| Memory | `/proc/meminfo` (MemTotal/MemAvailable) | Percentage |
| Network Speed | `/sys/class/net/*/speed` | Mbps |

**Response Format:**
```json
{
  "temperature": 45000,
  "cpu_loadavg": 23,
  "mem": 67,
  "eth_info": [
    {"name": "eth0", "ip": "192.168.1.100", "speed": "1000"}
  ]
}
```

**Implementation:** [event_loop.cpp:128-196]()

---

#### `sys.cmminfo` - NPU Memory Information

Reads Axera NPU contiguous memory manager (CMM) statistics from `/proc/ax_proc/mem_cmm_info`. Critical for monitoring NPU resource usage.

**Response Format:**
```json
{
  "total": 524288,
  "used": 131072,
  "remain": 393216
}
```

**Implementation:** [event_loop.cpp:229-291]()

---

#### `sys.lsmode` - List Configuration Modes

Scans the configuration directory (default: `/opt/m5stack/data/models/`) for JSON files prefixed with `mode_*.json`. Returns an array of parsed configuration objects.

**Implementation:** [event_loop.cpp:293-351]()

---

#### `sys.unit_call` - Unit RPC Forwarding

Forwards RPC calls to specific StackFlow units using the internal `unit_call()` function. The `object` field format is `"unit_name.function_name"`.

**Request Format:**
```json
{
  "action": "unit_call",
  "object": "llm-audio.get_volume",
  "data": {}
}
```

**Implementation:** [event_loop.cpp:198-227]()

---

#### `sys.push` / `sys.pull` - File Transfer

Binary-safe file transfer using base64 encoding and streaming support. Files can be transferred in chunks to avoid memory exhaustion.

**Object Format Syntax:**
- `sys.file./path/to/file` - Single chunk text file
- `sys.stream.file./path/to/file` - Multi-chunk text file
- `sys.base64.file./path/to/file` - Single chunk binary file
- `sys.base64.stream.file./path/to/file` - Multi-chunk binary file

**Streaming Protocol:**
```json
{
  "data": {
    "index": 0,
    "delta": "chunk_data_here",
    "finish": false
  }
}
```

The system creates a temporary directory `.tmp_file` for chunk reassembly and computes SHA256 checksums for verification.

**Implementation:** [event_loop.cpp:404-540]()

---

#### `sys.bashexec` - Shell Command Execution

Executes arbitrary bash commands in a pseudo-terminal (pty) and streams output in real-time or buffered mode. Supports both streaming and single-response modes.

**Security Note:** This function executes arbitrary commands with system privileges. Production deployments should implement access control.

**Features:**
- PTY allocation via `forkpty()` for proper terminal behavior
- ECHO disabled to prevent command echo in output
- Automatic exit injection to terminate shell session
- Streaming support with configurable chunk size

**Implementation:** [event_loop.cpp:593-694]()

---

#### `sys.upgrade` / `sys.update` - Package Management

`sys.update` searches `/mnt` for Debian packages matching `llm_update_*.deb` pattern.

`sys.upgrade` installs specified packages using `dpkg -i`, creating a lock file `/var/llm_update.lock` to track upgrade state across reboots.

**Implementation:** [event_loop.cpp:542-591]()

---

#### `sys.reset` / `sys.reboot` - System Control

`sys.reset` restarts all StackFlow services using systemd:
```bash
systemctl restart llm-*
```

`sys.reboot` performs a full system reboot:
```bash
reboot
```

Both create lock files (`/tmp/llm_reset.lock`, `/var/llm_update.lock`) to enable post-restart status reporting.

**Implementation:** [event_loop.cpp:696-741]()

---

## ZMQ Message Bus Architecture

The `llm-sys` component manages a complex ZMQ topology that connects external clients to internal units. Each communication path uses specific socket types optimized for its traffic pattern.

### Socket Topology

```mermaid
graph TB
    subgraph "Client Channels (Per Connection)"
        CLIENTPULL["ZMQ_PULL<br/>ipc:///tmp/llm_zmq_c_8000"]
        CLIENTPUSH["ZMQ_PUSH<br/>ipc:///tmp/llm_zmq_s_8000"]
    end
    
    subgraph "Unit Registration"
        UNIT1["unit_data: llm-audio<br/>inference_url"]
        UNIT2["unit_data: llm-kws<br/>inference_url"]
        UNIT3["unit_data: llm-asr<br/>inference_url"]
    end
    
    subgraph "Unit Publisher Channels"
        PUB1["ZMQ_PUB<br/>ipc:///tmp/llm_audio"]
        PUB2["ZMQ_PUB<br/>ipc:///tmp/llm_kws"]
        PUB3["ZMQ_PUB<br/>ipc:///tmp/llm_asr"]
    end
    
    CLIENTPULL -->|"unit_action_match()"| DISPATCHER["Command Dispatcher"]
    DISPATCHER -->|"zmq_com_send()"| CLIENTPUSH
    
    DISPATCHER -->|"inference action"| UNIT1
    DISPATCHER -->|"inference action"| UNIT2
    DISPATCHER -->|"inference action"| UNIT3
    
    UNIT1 -->|"send_msg()"| PUB1
    UNIT2 -->|"send_msg()"| PUB2
    UNIT3 -->|"send_msg()"| PUB3
    
    PUB1 -.->|"Subscribed by units"| UNITS["StackFlow Units"]
    PUB2 -.->|"Subscribed by units"| UNITS
    PUB3 -.->|"Subscribed by units"| UNITS
```

**Sources:** [projects/llm_framework/main_sys/src/zmq_bus.cpp:140-195](), [projects/llm_framework/main_sys/include/zmq_bus.h:23-41]()

### `unit_data` Class

Each registered unit has an associated `unit_data` instance stored in the key-value store. This object manages the unit's ZMQ PUB socket for broadcasting inference requests.

**Class Structure:**
```cpp
class unit_data {
    std::unique_ptr<pzmq> user_inference_chennal_;  // ZMQ_PUB socket
    std::string work_id;                             // Unit identifier
    std::string inference_url;                       // ipc:///tmp/llm_{work_id}
    
    void init_zmq(const std::string &url);
    void send_msg(const std::string &json_str);
};
```

Units register themselves by creating a `unit_data` instance and storing it in the global key-value store with their `work_id` as the key.

**Sources:** [projects/llm_framework/main_sys/include/zmq_bus.h:23-38](), [projects/llm_framework/main_sys/src/zmq_bus.cpp:140-158]()

### Message Format Augmentation

When forwarding `inference` actions to units, the dispatcher injects a `zmq_com` field containing the client's return channel URL:

```json
{
  "zmq_com": "ipc:///tmp/llm_zmq_s_8000",
  "request_id": "req_123",
  "work_id": "llm-audio",
  "action": "inference",
  "data": { ... }
}
```

This allows units to send responses directly back to the originating client without routing through the dispatcher.

**Sources:** [projects/llm_framework/main_sys/src/event_loop.cpp:815-829]()

---

## JSON Message Parsing

The `zmq_bus_com` class implements a sophisticated state machine for parsing JSON messages from stream-based transports (UART/TCP). It handles three message formats:

1. **Standard JSON** - Complete objects delimited by `{` and `}`
2. **RAW_JSON** - Binary data with length prefix: `{"RAW":1024}` followed by 1024 bytes
3. **RAW_BSON** - BSON data with length prefix: `{"BON":512}` followed by 512 bytes

### Parsing State Machine

```mermaid
stateDiagram-v2
    [*] --> RAW_NONE
    
    RAW_NONE --> RAW_NONE: "Accumulate JSON chars<br/>Track brace count"
    RAW_NONE --> Callback: "Brace count == 0<br/>Complete JSON object"
    RAW_NONE --> RAW_JSON: "Detect {\"RAW\":N}<br/>Extract length"
    RAW_NONE --> RAW_BSON: "Detect {\"BON\":N}<br/>Extract length"
    
    RAW_JSON --> RAW_JSON: "Accumulate N bytes"
    RAW_JSON --> on_raw_data: "N bytes received"
    on_raw_data --> RAW_NONE
    
    RAW_BSON --> RAW_BSON: "Accumulate N bytes"
    RAW_BSON --> on_bson_data: "N bytes received"
    on_bson_data --> RAW_NONE
    
    Callback --> RAW_NONE
```

The parser uses ARM NEON SIMD intrinsics when available to accelerate brace matching, processing 16 bytes per iteration instead of character-by-character scanning.

**Sources:** [projects/llm_framework/main_sys/src/zmq_bus.cpp:196-300](), [projects/llm_framework/main_sys/include/zmq_bus.h:43-77]()

### NEON-Optimized Parsing

The parser leverages ARM NEON instructions to compare 16 characters simultaneously for `{` and `}` delimiters:

```cpp
uint8x16_t target_open  = vdupq_n_u8('{');
uint8x16_t target_close = vdupq_n_u8('}');
uint8x16_t input_vector = vld1q_u8((const uint8_t *)&data[i]);
uint8x16_t result_open  = vceqq_u8(input_vector, target_open);
uint8x16_t result_close = vceqq_u8(input_vector, target_close);
uint8x16_t result_mask  = vorrq_u8(result_open, result_close);
```

If no delimiters are found in the 16-byte chunk, it's appended in bulk rather than character-by-character, significantly improving throughput for large JSON objects.

**Sources:** [projects/llm_framework/main_sys/src/zmq_bus.cpp:207-223]()

---

## Initialization and Lifecycle

The `llm-sys` service initialization follows a deterministic startup sequence to ensure all subsystems are ready before accepting client connections.

### Startup Sequence

```mermaid
sequenceDiagram
    participant Main as "main()"
    participant Server as "server_work()"
    participant Serial as "serial_work()"
    participant TCP as "tcp_work()"
    participant KV as "Key-Value Store"
    
    Main->>Server: "server_work()"
    Server->>KV: "Register sys.* handlers<br/>key_sql map"
    
    Main->>Serial: "serial_work()"
    Serial->>KV: "Load UART config"
    Serial->>Serial: "linux_uart_init()"
    Serial->>Serial: "zmq_bus_com::work()<br/>Start reader thread"
    
    Note over Serial: "Check lock files<br/>/var/llm_update.lock<br/>/tmp/llm_reset.lock"
    Serial->>Serial: "Send status message if rebooted"
    
    Main->>TCP: "tcp_work()"
    TCP->>KV: "Load TCP config"
    TCP->>TCP: "hv::TcpServer::start()<br/>Listen on port 10001"
    
    Note over Serial,TCP: "Services ready<br/>Accepting connections"
```

**Sources:** [projects/llm_framework/main_sys/src/event_loop.cpp:743-766](), [projects/llm_framework/main_sys/src/serial_com.cpp:88-123](), [projects/llm_framework/main_sys/src/tcp_com.cpp:95-109]()

### Post-Restart Status Reporting

After system upgrades or resets, the serial interface checks for lock files and sends automatic status messages to inform connected clients:

| Lock File | Message | Meaning |
|-----------|---------|---------|
| `/var/llm_update.lock` | `"upgrade over"` | Package installation completed |
| `/tmp/llm_reset.lock` | `"reset over"` | Service restart completed |

These lock files are created by the upgrade/reset handlers and removed after status reporting to prevent duplicate messages.

**Sources:** [projects/llm_framework/main_sys/src/serial_com.cpp:104-122]()

---

## Error Handling and Response Format

All system functions use a standardized response format that includes error codes and descriptive messages. The `usr_print_error()` helper function constructs these responses.

### Standard Response Format

```json
{
  "request_id": "req_123",
  "work_id": "sys",
  "created": 1640000000,
  "object": "sys.utf-8",
  "data": "response_data",
  "error": {
    "code": 0,
    "message": ""
  }
}
```

### Error Code Reference

| Code | Meaning | Typical Cause |
|------|---------|---------------|
| `0` | Success | Normal operation |
| `-1` | General error | Unexpected exception |
| `-2` | JSON format error | Invalid JSON syntax |
| `-3` | Action match false | Unknown system command |
| `-4` | Inference push failed | Unit not registered |
| `-9` | Unit call false | RPC to unit failed |
| `-10` | Not available | Function not implemented |
| `-17` | File error | File not found or permission denied |

**Sources:** [projects/llm_framework/main_sys/src/event_loop.cpp:44-74]()

### Thread Safety

All system handlers that perform long-running operations (file I/O, shell execution, hardware polling) spawn detached threads to prevent blocking the command dispatcher:

```cpp
int sys_hwinfo(int com_id, const nlohmann::json &json_obj) {
    std::thread t(_sys_hwinfo, com_id, json_obj);
    t.detach();
    return 0;
}
```

The `unit_action_match` function itself is protected by `unit_action_match_mtx` to ensure sequential processing of commands, preventing race conditions in the key-value store and ZMQ socket access.

**Sources:** [projects/llm_framework/main_sys/src/event_loop.cpp:767-772](), [projects/llm_framework/main_sys/src/event_loop.cpp:190-196]()