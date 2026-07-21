StackFlow EngineWrapper and Model Execution

# EngineWrapper and Model Execution

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [projects/llm_framework/main/src/main.cpp](projects/llm_framework/main/src/main.cpp)
- [projects/llm_framework/main_depth_anything/src/EngineWrapper.cpp](projects/llm_framework/main_depth_anything/src/EngineWrapper.cpp)
- [projects/llm_framework/main_depth_anything/src/EngineWrapper.hpp](projects/llm_framework/main_depth_anything/src/EngineWrapper.hpp)
- [projects/llm_framework/main_depth_anything/src/main.cpp](projects/llm_framework/main_depth_anything/src/main.cpp)
- [projects/llm_framework/main_melotts/src/main.cpp](projects/llm_framework/main_melotts/src/main.cpp)
- [projects/llm_framework/main_melotts/src/runner/EngineWrapper.cpp](projects/llm_framework/main_melotts/src/runner/EngineWrapper.cpp)
- [projects/llm_framework/main_melotts/src/runner/Lexicon.hpp](projects/llm_framework/main_melotts/src/runner/Lexicon.hpp)
- [projects/llm_framework/main_tts/src/main.cpp](projects/llm_framework/main_tts/src/main.cpp)
- [projects/llm_framework/main_whisper/src/runner/EngineWrapper.cpp](projects/llm_framework/main_whisper/src/runner/EngineWrapper.cpp)
- [projects/llm_framework/main_yolo/src/EngineWrapper.cpp](projects/llm_framework/main_yolo/src/EngineWrapper.cpp)
- [projects/llm_framework/main_yolo/src/EngineWrapper.hpp](projects/llm_framework/main_yolo/src/EngineWrapper.hpp)
- [projects/llm_framework/main_yolo/src/main.cpp](projects/llm_framework/main_yolo/src/main.cpp)

</details>



This document describes the `EngineWrapper` class, which provides a high-level C++ abstraction for loading and executing neural network models on the Axera NPU using the AX_ENGINE API. `EngineWrapper` is used across multiple StackFlow units that require NPU-accelerated inference, including YOLO object detection, depth estimation, MeloTTS synthesis, and Whisper ASR.

For information about specific models and their configurations, see [Computer Vision Units](#5). For LLM and VLM inference which uses different execution mechanisms, see [Language Model Units](#4).

## Class Overview

The `EngineWrapper` class is defined in unit-specific header files but shares a common interface across implementations. It encapsulates the complete lifecycle of NPU model execution from loading through inference to cleanup.

**Core Responsibilities:**
- Model file loading and memory management
- Virtual NPU (VNPU) configuration and validation
- AX_ENGINE handle and context management
- Input/output buffer allocation and management
- Synchronous model inference execution
- Model-specific post-processing (YOLO, depth estimation)

```mermaid
classDiagram
    class EngineWrapper {
        -bool m_hasInit
        -AX_ENGINE_HANDLE m_handle
        -AX_ENGINE_IO_INFO_T* m_io_info
        -AX_ENGINE_IO_T m_io
        -int m_input_num
        -int m_output_num
        +Init(strModelPath, nNpuType, npuMode) int
        +SetInput(pInput, index) int
        +Run() int
        +GetOutput(pOutput, index) int
        +GetInputSize(index) int
        +GetOutputSize(index) int
        +GetOutputPtr(index) void*
        +Release() int
        +Post_Process(...) int
    }
    
    class llm_task_yolo {
        +unique_ptr~EngineWrapper~ yolo_
        +inference(src, bgr2rgb) bool
        +load_model(config_body) int
    }
    
    class llm_task_melotts {
        +unique_ptr~EngineWrapper~ decoder_
        +TTS(msg_str, finish) bool
        +load_model(config_body) int
    }
    
    class llm_task_depth {
        +unique_ptr~EngineWrapper~ depth_anything_
        +inference(src, bgr2rgb) bool
        +load_model(config_body) int
    }
    
    class AX_ENGINE_API {
        <<Axera SDK>>
        +AX_ENGINE_Init()
        +AX_ENGINE_CreateHandle()
        +AX_ENGINE_CreateContext()
        +AX_ENGINE_GetIOInfo()
        +AX_ENGINE_RunSync()
    }
    
    llm_task_yolo --> EngineWrapper
    llm_task_melotts --> EngineWrapper
    llm_task_depth --> EngineWrapper
    EngineWrapper --> AX_ENGINE_API
```

**Sources:**
- [projects/llm_framework/main_yolo/src/EngineWrapper.hpp:11-70]()
- [projects/llm_framework/main_depth_anything/src/EngineWrapper.hpp:11-56]()
- [projects/llm_framework/main_melotts/src/main.cpp:77-78]()

## Initialization Process

Model initialization in `EngineWrapper::Init()` follows a multi-stage process that validates hardware compatibility and prepares the execution environment.

### Initialization Stages

```mermaid
sequenceDiagram
    participant App as "Application"
    participant EW as "EngineWrapper"
    participant Utils as "utils namespace"
    participant AXE as "AX_ENGINE API"
    participant Mem as "Memory"
    
    App->>EW: Init(strModelPath, nNpuType, npuMode)
    
    Note over EW: Stage 0: Engine Initialization
    EW->>AXE: AX_ENGINE_Init(&npu_attr)
    AXE-->>EW: return ret
    
    Note over EW: Stage 1: Model Loading
    EW->>Utils: read_file(strModelPath, ...)
    Utils->>Mem: AX_SYS_MemAlloc (if CMM mode)
    Mem-->>Utils: pModelBufferVirAddr
    Utils-->>EW: model buffer
    
    Note over EW: Stage 1.1: Get Model Type
    EW->>AXE: AX_ENGINE_GetModelType(...)
    AXE-->>EW: eModelType (TYPE0/TYPE1/TYPE2)
    
    Note over EW: Stage 1.2: Check VNPU
    EW->>EW: CheckModelVNpu(...)
    EW->>AXE: AX_ENGINE_GetVNPUAttr(&stNpuAttr)
    AXE-->>EW: NPU hardware mode
    EW->>EW: Validate model vs hardware
    EW-->>EW: nNpuSet configured
    
    Note over EW: Stage 2: Create Handle
    EW->>AXE: AX_ENGINE_CreateHandle(&handle, buffer, size)
    AXE-->>EW: handle
    EW->>Mem: Free model buffer
    
    Note over EW: Stage 3: Create Context
    EW->>AXE: AX_ENGINE_CreateContext(handle)
    AXE-->>EW: context created
    
    Note over EW: Stage 4: Get IO Info
    EW->>AXE: AX_ENGINE_GetIOInfo(handle, &m_io_info)
    AXE-->>EW: m_io_info populated
    
    Note over EW: Stage 6: Prepare IO Buffers
    EW->>Utils: prepare_io(path, m_io_info, m_io, strategy)
    Utils->>Mem: Allocate input/output buffers
    Mem-->>Utils: buffers allocated
    Utils-->>EW: m_io ready
    
    EW-->>App: return 0 (success)
```

**Sources:**
- [projects/llm_framework/main_yolo/src/EngineWrapper.cpp:182-316]()
- [projects/llm_framework/main_depth_anything/src/EngineWrapper.cpp:181-316]()

### Model Type and Hardware Validation

The AXERA platform supports different model types with varying computational requirements:

| Platform | Model Types | Description |
|----------|-------------|-------------|
| AX650C | TYPE0 (3.6T), TYPE1 (7.2T), TYPE2 (18T) | Different TOPS ratings |
| AX620E/AX620Q | TYPE0 (HalfOCM), TYPE1 (FullOCM) | On-Chip Memory modes |

The `CheckModelVNpu()` function validates model compatibility with the configured VNPU mode:

```mermaid
graph TD
    A["CheckModelVNpu(strModel, eModelType, nNpuType)"] --> B["AX_ENGINE_GetVNPUAttr(&stNpuAttr)"]
    B --> C{Hardware Mode?}
    
    C -->|"VNPU_DISABLE"| D["nNpuSet = 0x01<br/>(Non-VNPU mode)"]
    C -->|"VIRTUAL_NPU_STD"| E{Model Type?}
    C -->|"VIRTUAL_NPU_BIG_LITTLE"| F{Model Type?}
    
    E -->|"TYPE1/TYPE2"| G["Return -1<br/>(Incompatible)"]
    E -->|"TYPE0"| H["Configure STD VNPU<br/>Default: VNPU2"]
    
    F -->|"TYPE2"| I["Return -1<br/>(10.8T incompatible)"]
    F -->|"TYPE1"| J["7.2T: BL VNPU1 only"]
    F -->|"TYPE0"| K["3.6T: BL VNPU1 or VNPU2"]
    
    H --> L["Set nNpuSet based on nNpuType flags"]
    J --> L
    K --> L
    
    L --> M["Return 0 (Success)"]
    D --> M
    G --> N["Fail"]
    I --> N
```

**VNPU Type Flags:**

| Flag | Value | Description |
|------|-------|-------------|
| AX_NPU_DEFAULT | 0 | Use system default NPU |
| AX_STD_VNPU_1 | 1 << 0 | Standard VNPU1 |
| AX_STD_VNPU_2 | 1 << 1 | Standard VNPU2 |
| AX_STD_VNPU_3 | 1 << 2 | Standard VNPU3 |
| AX_BL_VNPU_1 | 1 << 3 | Big-Little VNPU1 |
| AX_BL_VNPU_2 | 1 << 4 | Big-Little VNPU2 |

**Sources:**
- [projects/llm_framework/main_yolo/src/EngineWrapper.cpp:26-134]()
- [projects/llm_framework/main_depth_anything/src/EngineWrapper.cpp:26-179]()
- [projects/llm_framework/main_melotts/src/runner/EngineWrapper.cpp:26-175]()

## Model Execution Flow

Model inference follows a three-step pattern: set inputs, run synchronously, retrieve outputs.

### Basic Execution Pattern

```mermaid
flowchart LR
    A["Preprocessed<br/>Input Data"] --> B["EngineWrapper::SetInput(data, 0)"]
    B --> C["utils::push_io_input()"]
    C --> D["Copy to m_io.pInputs[index]"]
    
    D --> E["EngineWrapper::Run()"]
    E --> F["AX_ENGINE_RunSync(m_handle, &m_io)"]
    F --> G["NPU Execution"]
    
    G --> H["EngineWrapper::GetOutput(buffer, 0)"]
    H --> I["utils::push_io_output()"]
    I --> J["Copy from m_io.pOutputs[index]"]
    J --> K["Post-processing"]
```

### YOLO Inference Example

The YOLO object detection unit demonstrates typical `EngineWrapper` usage:

```mermaid
sequenceDiagram
    participant App as "llm_task::inference"
    participant CV as "OpenCV/Common"
    participant EW as "EngineWrapper"
    participant NPU as "Axera NPU"
    participant PP as "Post_Process"
    
    App->>CV: get_input_data_letterbox(src, image, h, w)
    CV-->>App: letterboxed RGB image
    
    App->>EW: SetInput(image.data(), 0)
    EW-->>App: 0 (success)
    
    App->>EW: Run()
    EW->>NPU: AX_ENGINE_RunSync()
    NPU-->>EW: inference complete
    EW-->>App: 0 (success)
    
    App->>EW: Post_Process(img_mat, ...)
    EW->>PP: post_process(m_io_info, &m_io, ...)
    
    alt detect mode
        PP->>PP: generate_proposals_yolov8_native (3 scales)
        PP->>PP: get_out_bbox(proposals, objects, nms_threshold)
    else segment mode
        PP->>PP: generate_proposals_yolov8_seg_native
        PP->>PP: get_out_bbox_mask(proposals, mask_proto)
    else pose mode
        PP->>PP: generate_proposals_yolov8_pose_native
        PP->>PP: get_out_bbox_kps(proposals, objects)
    else obb mode
        PP->>PP: generate_proposals_yolov8_obb_native
        PP->>PP: get_out_obb_bbox(proposals, objects)
    end
    
    PP-->>EW: objects vector populated
    EW-->>App: 0 (success)
    App->>App: out_callback_(output, finish)
```

**Sources:**
- [projects/llm_framework/main_yolo/src/main.cpp:225-289]()
- [projects/llm_framework/main_yolo/src/EngineWrapper.cpp:319-336]()
- [projects/llm_framework/main_yolo/src/EngineWrapper.cpp:427-492]()

### MeloTTS Decoder Execution

MeloTTS uses `EngineWrapper` for its decoder model, processing encoded phoneme features:

```mermaid
graph LR
    A["Encoder Output<br/>(zp_data)"] --> B["Slice into chunks<br/>(dec_len per slice)"]
    B --> C["decoder_->SetInput(zp.data(), 0)"]
    C --> D["decoder_->SetInput(g_matrix.data(), 1)"]
    D --> E["decoder_->Run()"]
    E --> F["decoder_->GetOutput(decoder_output.data(), 0)"]
    F --> G["Audio crossfade<br/>blending"]
    G --> H["Accumulate to pcmlist"]
    H --> I{More slices?}
    I -->|Yes| B
    I -->|No| J["Resample audio<br/>mode_rate to audio_rate"]
    J --> K["Convert float to int16"]
    K --> L["Output PCM data"]
```

The decoder processes audio in slices with overlap and crossfading to avoid artifacts:

**Slice Processing Parameters:**

| Parameter | Value | Description |
|-----------|-------|-------------|
| overlap_size | 1024 | Samples overlap between slices |
| fade_size | 512 | Crossfade length in samples |
| dec_len | Calculated | Decoder input size / channels |
| audio_slice_len | Calculated | Decoder output size |

**Sources:**
- [projects/llm_framework/main_melotts/src/main.cpp:307-418]()
- [projects/llm_framework/main_melotts/src/main.cpp:208-209]()

## IO Buffer Management

`EngineWrapper` manages input and output buffers through the `AX_ENGINE_IO_T` structure. Buffer allocation is handled by utility functions in the `utils` namespace.

### Buffer Structure

```mermaid
graph TB
    subgraph "AX_ENGINE_IO_T m_io"
        A["pInputs[]<br/>AX_ENGINE_IO_BUFFER_T*"]
        B["pOutputs[]<br/>AX_ENGINE_IO_BUFFER_T*"]
        C["nInputSize<br/>uint32_t"]
        D["nOutputSize<br/>uint32_t"]
    end
    
    subgraph "AX_ENGINE_IO_BUFFER_T"
        E["pVirAddr<br/>void*"]
        F["phyAddr<br/>AX_U64"]
        G["nSize<br/>AX_U32"]
    end
    
    A --> E
    B --> E
    
    subgraph "Operations"
        H["utils::prepare_io()"]
        I["utils::push_io_input()"]
        J["utils::push_io_output()"]
        K["utils::cache_io_flush()"]
        L["utils::free_io()"]
    end
    
    H -.->|Allocates| E
    I -.->|Writes to| E
    J -.->|Reads from| E
    K -.->|Flushes cache| E
    L -.->|Frees| E
```

### Buffer Allocation Strategy

The `utils::prepare_io()` function supports multiple allocation strategies:

| Strategy | Description | Use Case |
|----------|-------------|----------|
| IO_BUFFER_STRATEGY_DEFAULT | Standard allocation | General purpose |
| IO_BUFFER_STRATEGY_CACHED | CPU-cached memory | Frequent CPU access |

Buffer memory is allocated using `AX_SYS_MemAlloc()` for physical-contiguous memory required by NPU DMA operations.

**Sources:**
- [projects/llm_framework/main_yolo/src/EngineWrapper.cpp:272-316]()
- [projects/llm_framework/main_yolo/src/EngineWrapper.cpp:319-341]()

## Multi-Unit Integration

Different StackFlow units use `EngineWrapper` for their specific model types. The integration pattern is consistent across units.

### Integration Pattern Per Unit

```mermaid
graph TB
    subgraph "llm-yolo Unit"
        Y1["llm_task"] --> Y2["unique_ptr<EngineWrapper> yolo_"]
        Y2 --> Y3["Init: yolo11n.axmodel"]
        Y3 --> Y4["inference: detect/segment/pose/obb"]
        Y4 --> Y5["Post_Process: NMS + bbox"]
    end
    
    subgraph "llm-depth-anything Unit"
        D1["llm_task"] --> D2["unique_ptr<EngineWrapper> depth_anything_"]
        D2 --> D3["Init: depth_anything.axmodel"]
        D3 --> D4["inference: depth estimation"]
        D4 --> D5["Post_Process: colormap + JPEG"]
    end
    
    subgraph "llm-melotts Unit"
        M1["llm_task"] --> M2["unique_ptr<EngineWrapper> decoder_"]
        M2 --> M3["Init: decoder.axmodel"]
        M3 --> M4["TTS: phoneme decoding"]
        M4 --> M5["Audio slice processing"]
    end
    
    subgraph "llm-whisper Unit"
        W1["llm_task"] --> W2["unique_ptr<EngineWrapper> encoder_"]
        W3["unique_ptr<EngineWrapper> decoder_"]
        W2 --> W4["Init: encoder.axmodel"]
        W3 --> W5["Init: decoder.axmodel"]
        W4 --> W6["ASR: audio encoding"]
        W5 --> W7["ASR: token decoding"]
    end
    
    style Y2 fill:#f9f9f9
    style D2 fill:#f9f9f9
    style M2 fill:#f9f9f9
    style W2 fill:#f9f9f9
    style W3 fill:#f9f9f9
```

### Model Configuration and Loading

Each unit loads models through a configuration-driven pattern:

| Unit | Model Config Parameter | Typical Model Size | Model Format |
|------|----------------------|-------------------|--------------|
| llm-yolo | `yolo_model` | 2.8-3.2 MB | .axmodel (YOLO11n) |
| llm-depth-anything | `depth_anything_model` | ~29 MB | .axmodel |
| llm-melotts | `decoder` | ~102 MB | .axmodel |
| llm-whisper | `encoder`, `decoder` | 201-725 MB total | .axmodel |

**Configuration Flow:**

```mermaid
sequenceDiagram
    participant Config as "JSON Config"
    participant Task as "llm_task"
    participant EW as "EngineWrapper"
    participant FS as "Filesystem"
    
    Config->>Task: load_model(config_body)
    Task->>Task: parse_config(): extract model path
    Task->>FS: Read mode_*.json from /opt/m5stack/data/models/
    FS-->>Task: file_body with mode_param
    
    Task->>Task: Construct full path:<br/>base_model_path + model + "/" + model_file
    
    Task->>EW: new EngineWrapper()
    Task->>EW: Init(full_model_path, npu_type, npu_mode)
    EW->>FS: Load .axmodel file
    FS-->>EW: Model binary data
    EW->>EW: Initialize NPU context
    EW-->>Task: 0 (success)
    
    Task-->>Config: Model ready for inference
```

**Sources:**
- [projects/llm_framework/main_yolo/src/main.cpp:100-147]()
- [projects/llm_framework/main_depth_anything/src/main.cpp:89-131]()
- [projects/llm_framework/main_melotts/src/main.cpp:131-222]()

## Memory Management

`EngineWrapper` implements RAII (Resource Acquisition Is Initialization) for automatic resource cleanup.

### Resource Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Uninitialized: Constructor
    Uninitialized --> ModelLoaded: Init() - Load model
    ModelLoaded --> HandleCreated: AX_ENGINE_CreateHandle()
    HandleCreated --> ContextCreated: AX_ENGINE_CreateContext()
    ContextCreated --> IOPrepared: prepare_io()
    IOPrepared --> Ready: m_hasInit = true
    
    Ready --> Running: Run()
    Running --> Ready: Inference complete
    
    Ready --> Cleaning: Release() or Destructor
    Cleaning --> IOFreed: free_io()
    IOFreed --> HandleDestroyed: AX_ENGINE_DestroyHandle()
    HandleDestroyed --> [*]: m_handle = nullptr
```

### Memory Allocation Methods

Two methods for loading models:

**1. CMM (Contiguous Memory Manager) Mode:**
```
utils::read_file() → AX_SYS_MemAlloc() → Physical contiguous memory
```
- Used by default (`bLoadModelUseCmm = AX_TRUE`)
- Required for zero-copy NPU access
- Freed with `AX_SYS_MemFree(u64ModelBufferPhyAddr, &pModelBufferVirAddr)`

**2. Standard Heap Mode:**
```
utils::read_file() → std::vector<char> → Virtual memory
```
- Fallback option
- Model copied during handle creation
- Freed with vector destructor

**Sources:**
- [projects/llm_framework/main_yolo/src/EngineWrapper.cpp:195-227]()
- [projects/llm_framework/main_yolo/src/EngineWrapper.cpp:359-367]()

## Async Inference Pattern

Units like YOLO and depth-anything implement asynchronous inference using a thread-safe queue pattern:

```mermaid
sequenceDiagram
    participant Main as "Main Thread<br/>(Data Reception)"
    participant Queue as "async_list_<br/>thread_safe::list"
    participant Worker as "Worker Thread<br/>(inference_run_)"
    participant EW as "EngineWrapper"
    
    Note over Main,Worker: Initialization
    Main->>Worker: Create std::thread(llm_task::run)
    Worker->>Queue: Wait for items
    
    Note over Main,Worker: Frame Processing
    Main->>Main: Receive camera frame
    Main->>Main: inference_async(src)
    
    alt Queue not full (< 3 items)
        Main->>Queue: put(inference_async_par)
        Queue-->>Worker: Item available
        Worker->>Queue: get()
        Queue-->>Worker: inference_async_par
        Worker->>Worker: inference(src, bgr2rgb)
        Worker->>EW: SetInput() → Run() → Post_Process()
        Worker->>Worker: out_callback_(results)
    else Queue full
        Main->>Main: SLOGE("inference list is full")
    end
    
    Note over Main,Worker: Shutdown
    Main->>Queue: put(empty inference_async_par)
    Worker->>Queue: get()
    Queue-->>Worker: empty item (src.empty() == true)
    Worker->>Worker: Break loop, exit thread
```

**Queue Management:**

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Max queue size | 3 | Prevent memory overflow from fast input |
| Queue type | `thread_safe::list<inference_async_par>` | Lock-free producer-consumer |
| Stop signal | Empty cv::Mat in queue item | Signal thread termination |

**Sources:**
- [projects/llm_framework/main_yolo/src/main.cpp:200-223]()
- [projects/llm_framework/main_yolo/src/main.cpp:312-333]()
- [projects/llm_framework/main_depth_anything/src/main.cpp:181-204]()

## Hardware Initialization

All units using `EngineWrapper` must initialize the Axera system APIs before creating `EngineWrapper` instances:

```mermaid
graph LR
    A["llm_task constructor"] --> B["_ax_init()"]
    B --> C{ax_init_flage_ == 0?}
    C -->|Yes| D["AX_SYS_Init()"]
    D --> E["AX_ENGINE_Init(&npu_attr)"]
    E --> F["ax_init_flage_++"]
    C -->|No| F
    
    G["llm_task destructor"] --> H["_ax_deinit()"]
    H --> I["ax_init_flage_--"]
    I --> J{ax_init_flage_ == 0?}
    J -->|Yes| K["AX_ENGINE_Deinit()"]
    K --> L["AX_SYS_Deinit()"]
    J -->|No| M["Keep running"]
```

The reference counting pattern (`ax_init_flage_`) ensures proper initialization/deinitialization when multiple `llm_task` instances exist.

**Initialization Order:**
1. `AX_SYS_Init()` - System-level initialization
2. `AX_ENGINE_Init(&npu_attr)` - NPU engine initialization (may be called within `EngineWrapper::Init()` depending on version)
3. `EngineWrapper::Init()` - Model-specific initialization

**Sources:**
- [projects/llm_framework/main_yolo/src/main.cpp:291-310]()
- [projects/llm_framework/main_melotts/src/main.cpp:473-499]()

## Error Handling

`EngineWrapper` methods return integer error codes following Axera SDK conventions:

| Return Value | Meaning | Common Causes |
|--------------|---------|---------------|
| 0 | Success | Operation completed successfully |
| -1 | Generic failure | File not found, allocation failure |
| Non-zero AX error code | SDK-specific error | `AX_ENGINE_RunSync()` failures, context errors |

**Error Propagation Pattern:**

```mermaid
graph TB
    A["EngineWrapper::Init()"] --> B{Model file exists?}
    B -->|No| C["printf error message<br/>return -1"]
    B -->|Yes| D{AX_ENGINE_GetModelType success?}
    D -->|No| E["freeModelBuffer()<br/>return -1"]
    D -->|Yes| F{CheckModelVNpu success?}
    F -->|No| G["freeModelBuffer()<br/>return -1"]
    F -->|Yes| H{AX_ENGINE_CreateHandle success?}
    H -->|No| I["deinit_handle()<br/>return -1"]
    H -->|Yes| J{AX_ENGINE_CreateContext success?}
    J -->|No| I
    J -->|Yes| K{prepare_io success?}
    K -->|No| L["free_io()<br/>deinit_handle()<br/>return -1"]
    K -->|Yes| M["m_hasInit = true<br/>return 0"]
```

Units wrap `EngineWrapper` errors in their own error response format:

```
EngineWrapper returns -1
  → llm_task::load_model() returns -5
    → llm_unit::setup() sends error_body:
       {"code": -5, "message": "Model loading failed."}
```

**Sources:**
- [projects/llm_framework/main_yolo/src/EngineWrapper.cpp:182-316]()
- [projects/llm_framework/main_yolo/src/main.cpp:481-519]()