# Advanced Features

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [docs/en/refs/module.llm.ref](docs/en/refs/module.llm.ref)
- [docs/en/refs/unit.angle.ref](docs/en/refs/unit.angle.ref)
- [docs/en/refs/unit.env.ref](docs/en/refs/unit.env.ref)
- [docs/en/refs/unit.rgb.ref](docs/en/refs/unit.rgb.ref)
- [docs/en/units/env.rst](docs/en/units/env.rst)
- [docs/en/units/rgb.rst](docs/en/units/rgb.rst)
- [docs/zh_CN/refs/unit.angle.ref](docs/zh_CN/refs/unit.angle.ref)
- [docs/zh_CN/refs/unit.dlight.ref](docs/zh_CN/refs/unit.dlight.ref)
- [docs/zh_CN/refs/unit.dual_button.ref](docs/zh_CN/refs/unit.dual_button.ref)
- [docs/zh_CN/refs/unit.env.ref](docs/zh_CN/refs/unit.env.ref)
- [docs/zh_CN/refs/unit.ir.ref](docs/zh_CN/refs/unit.ir.ref)
- [docs/zh_CN/refs/unit.light.ref](docs/zh_CN/refs/unit.light.ref)
- [docs/zh_CN/refs/unit.rgb.ref](docs/zh_CN/refs/unit.rgb.ref)
- [docs/zh_CN/unit/angle.rst](docs/zh_CN/unit/angle.rst)
- [docs/zh_CN/unit/env.rst](docs/zh_CN/unit/env.rst)
- [docs/zh_CN/unit/index.rst](docs/zh_CN/unit/index.rst)
- [docs/zh_CN/unit/ir.rst](docs/zh_CN/unit/ir.rst)
- [docs/zh_CN/unit/rgb.rst](docs/zh_CN/unit/rgb.rst)
- [examples/module/llm/kws_asr.m5f2](examples/module/llm/kws_asr.m5f2)
- [examples/module/llm/kws_asr_zh_CN.m5f2](examples/module/llm/kws_asr_zh_CN.m5f2)
- [examples/module/llm/llm_voice_assista_zh_CN.m5f2](examples/module/llm/llm_voice_assista_zh_CN.m5f2)
- [examples/module/llm/llm_voice_assistant.m5f2](examples/module/llm/llm_voice_assistant.m5f2)
- [examples/module/llm/text_assistant.m5f2](examples/module/llm/text_assistant.m5f2)
- [examples/module/llm/tts.m5f2](examples/module/llm/tts.m5f2)
- [examples/module/llm/tts_zh_CN.m5f2](examples/module/llm/tts_zh_CN.m5f2)
- [examples/module/llm/yolo.m5f2](examples/module/llm/yolo.m5f2)
- [examples/unit/env/env_cores3.py](examples/unit/env/env_cores3.py)
- [m5stack/libs/module/llm.py](m5stack/libs/module/llm.py)

</details>



This document provides an overview of specialized features that extend the UIFlow MicroPython firmware beyond basic hardware control. It covers the AI/LLM integration system for natural language processing and computer vision tasks, and the multi-language documentation infrastructure that supports both text-based and visual programming workflows.

For detailed information about the LLM module API and usage patterns, see [LLM and AI Module](#6.1). For documentation authoring guidelines and the RST-based system, see [Documentation System](#6.2).

## Overview

The firmware includes two major specialized subsystems:

1. **AI/LLM Integration** - A UART-based module system ([m5stack/libs/module/llm.py]()) that provides access to external AI accelerators running large language models (LLM), vision-language models (VLM), speech recognition (ASR/Whisper), text-to-speech (TTS), keyword spotting (KWS), voice activity detection (VAD), and object detection (YOLO). The system uses JSON-based message passing with work ID tracking to manage multiple concurrent AI pipelines.

2. **Documentation System** - A multi-language (English/Chinese) documentation infrastructure using reStructuredText (RST) format with reusable reference files ([docs/en/refs/*.ref](), [docs/zh_CN/refs/*.ref]()), Python code examples with `literalinclude` directives, and UIFLOW2 visual programming projects ([examples/**/*.m5f2]()). This system generates API documentation synchronized with working code.

## LLM Module Architecture

The LLM module provides a comprehensive API for AI inference tasks on external hardware via UART communication. The architecture separates concerns into communication layer, message queue management, and specialized API classes for different AI functions.

**LLM Module Class Structure**

```mermaid
graph TB
    subgraph "Core Communication Layer"
        LlmModule["LlmModule<br/>(llm.py:904-1307+)"]
        ModuleComm["ModuleComm<br/>(llm.py:10-37)"]
        ModuleMsg["ModuleMsg<br/>(llm.py:40-92)"]
    end
    
    subgraph "System Management API"
        ApiSys["ApiSys<br/>(llm.py:94-211)<br/>ping/reset/version/lsmode"]
    end
    
    subgraph "Language Model APIs"
        ApiLlm["ApiLlm<br/>(llm.py:213-305)<br/>setup/inference"]
        ApiVlm["ApiVlm<br/>(llm.py:307-407)<br/>setup/inference/inference_img"]
    end
    
    subgraph "Audio Processing APIs"
        ApiAudio["ApiAudio<br/>(llm.py:410-458)<br/>setup"]
        ApiTts["ApiTts<br/>(llm.py:509-580)<br/>setup/inference"]
        ApiMelotts["ApiMelotts<br/>(llm.py:582-651)<br/>setup/inference"]
    end
    
    subgraph "Speech Recognition APIs"
        ApiKws["ApiKws<br/>(llm.py:653-700)<br/>setup keyword spotting"]
        ApiAsr["ApiAsr<br/>(llm.py:702-753)<br/>setup streaming ASR"]
        ApiWhisper["ApiWhisper<br/>(llm.py:800-845)<br/>setup batch ASR"]
        ApiVad["ApiVad<br/>(llm.py:755-798)<br/>setup voice detection"]
    end
    
    subgraph "Computer Vision API"
        ApiYolo["ApiYolo<br/>(llm.py:847-902)<br/>setup/inference_img"]
        ApiCamera["ApiCamera<br/>(llm.py:460-507)<br/>setup"]
    end
    
    LlmModule -->|"__init__<br/>uart,comm,msg"| ModuleComm
    LlmModule -->|"creates"| ModuleMsg
    ModuleComm -->|"used by"| ModuleMsg
    
    LlmModule -->|"self.sys"| ApiSys
    LlmModule -->|"self.llm"| ApiLlm
    LlmModule -->|"self.vlm"| ApiVlm
    LlmModule -->|"self.audio"| ApiAudio
    LlmModule -->|"self.tts"| ApiTts
    LlmModule -->|"self.melotts"| ApiMelotts
    LlmModule -->|"self.kws"| ApiKws
    LlmModule -->|"self.asr"| ApiAsr
    LlmModule -->|"self.whisper"| ApiWhisper
    LlmModule -->|"self.vad"| ApiVad
    LlmModule -->|"self.yolo"| ApiYolo
    LlmModule -->|"self.camera"| ApiCamera
    
    ApiSys -.->|"passes"| ModuleMsg
    ApiLlm -.->|"passes"| ModuleMsg
    ApiVlm -.->|"passes"| ModuleMsg
    ApiAudio -.->|"passes"| ModuleMsg
    ApiTts -.->|"passes"| ModuleMsg
    ApiMelotts -.->|"passes"| ModuleMsg
    ApiKws -.->|"passes"| ModuleMsg
    ApiAsr -.->|"passes"| ModuleMsg
    ApiWhisper -.->|"passes"| ModuleMsg
    ApiVad -.->|"passes"| ModuleMsg
    ApiYolo -.->|"passes"| ModuleMsg
    ApiCamera -.->|"passes"| ModuleMsg
```

Sources: [m5stack/libs/module/llm.py:10-1307+]()

**Message Queue and Work ID Tracking**

The LLM module uses a JSON-based request/response protocol with unique identifiers for tracking concurrent operations:

```mermaid
sequenceDiagram
    participant App as "User Application"
    participant LlmMod as "LlmModule"
    participant Msg as "ModuleMsg<br/>response_msg_list"
    participant Comm as "ModuleComm<br/>UART"
    participant Module as "External AI Module"
    
    App->>LlmMod: llm_setup(prompt, model)
    LlmMod->>Comm: send_cmd(JSON)<br/>{"request_id":"llm_setup","work_id":"llm",...}
    Comm->>Module: UART write
    
    Module-->>Comm: JSON response
    Comm-->>Msg: get_response()
    Msg->>Msg: add_msg_from_response()<br/>append to response_msg_list
    
    LlmMod->>Msg: wait_and_take_msg(request_id)
    Msg-->>LlmMod: Return work_id="llm_abc123"
    LlmMod-->>App: Return latest_llm_work_id
    
    Note over App,Module: Multiple setup calls create different work_ids
    
    App->>LlmMod: llm_inference(work_id, "Hello")
    LlmMod->>Comm: send_cmd({"work_id":"llm_abc123",...})
    Comm->>Module: UART write
    
    loop Streaming Response
        Module-->>Comm: {"work_id":"llm_abc123","data":{"delta":"H"}}
        Msg->>Msg: append to response_msg_list
        App->>LlmMod: update() + take_msg()
        Msg-->>App: Process delta
    end
    
    Module-->>Comm: {"work_id":"llm_abc123","data":{"finish":true}}
    App->>LlmMod: clear_response_msg_list()
```

Sources: [m5stack/libs/module/llm.py:40-92](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/libs/module/llm.py#L40-L92), [m5stack/libs/module/llm.py:213-305](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/libs/module/llm.py#L213-L305)

## Documentation System Architecture

The documentation system supports multiple user personas (text programmers, visual programmers, international users) through a layered architecture combining RST files, reference definitions, executable examples, and visual programming projects.

**Documentation Generation Flow**

```mermaid
graph TB
    subgraph "Source Files"
        RST_EN["RST Files<br/>docs/en/units/*.rst<br/>docs/en/module/*.rst"]
        RST_ZH["RST Files<br/>docs/zh_CN/unit/*.rst<br/>docs/zh_CN/module/*.rst"]
        REF_EN["Reference Files<br/>docs/en/refs/*.ref<br/>Image URLs, Links"]
        REF_ZH["Reference Files<br/>docs/zh_CN/refs/*.ref<br/>Image URLs, Links"]
    end
    
    subgraph "Code Examples"
        PY_EX["Python Examples<br/>examples/unit/*.py<br/>examples/module/*.py"]
        M5F2["UIFLOW2 Projects<br/>examples/**/*.m5f2<br/>Visual blocks"]
    end
    
    subgraph "Implementation"
        IMPL["Library Code<br/>m5stack/libs/unit/*.py<br/>m5stack/libs/module/*.py"]
    end
    
    subgraph "Build Process"
        SPHINX["Sphinx Build<br/>RST to HTML"]
    end
    
    subgraph "Output"
        HTML_EN["English HTML<br/>API Documentation"]
        HTML_ZH["Chinese HTML<br/>API Documentation"]
        UIFLOW2["UIFLOW2 IDE<br/>Block Examples"]
    end
    
    RST_EN -->|".. include::"| REF_EN
    RST_ZH -->|".. include::"| REF_ZH
    
    RST_EN -->|".. literalinclude::"| PY_EX
    RST_ZH -->|".. literalinclude::"| PY_EX
    
    RST_EN -->|"documents API"| IMPL
    RST_ZH -->|"documents API"| IMPL
    
    PY_EX -->|"imports from"| IMPL
    
    RST_EN -->|"links to"| M5F2
    RST_ZH -->|"links to"| M5F2
    
    RST_EN --> SPHINX
    RST_ZH --> SPHINX
    REF_EN --> SPHINX
    REF_ZH --> SPHINX
    
    SPHINX --> HTML_EN
    SPHINX --> HTML_ZH
    
    M5F2 --> UIFLOW2
```

Sources: [docs/en/units/env.rst:1-93](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/en/units/env.rst#L1-L93), [docs/zh_CN/unit/env.rst:1-92](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/zh_CN/unit/env.rst#L1-L92), [docs/en/refs/unit.env.ref:1-28](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/en/refs/unit.env.ref#L1-L28), [docs/zh_CN/refs/unit.env.ref:1-28](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/zh_CN/refs/unit.env.ref#L1-L28), [examples/unit/env/env_cores3.py:1-50](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/examples/unit/env/env_cores3.py#L1-L50)

**Reference File Pattern**

The `.ref` files define reusable image URLs, product links, and UIFLOW2 example links that can be included in multiple RST documents:

| Component | Purpose | Example |
|-----------|---------|---------|
| **Product Images** | Hardware photos with links to documentation | `\|ENV\| image:: https://static-cdn.m5stack.com/...` |
| **Block Diagrams** | UIFLOW2 visual programming blocks | `\|init.png\| image:: https://static-cdn.m5stack.com/mpy_docs/...` |
| **Method Diagrams** | Visual representation of API methods | `\|read_temperature.png\| image:: ...` |
| **Example Links** | Clickable links to load UIFLOW2 projects | `\|env_cores3_example.m5f2\| raw:: html` |

Sources: [docs/en/refs/unit.env.ref:1-28](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/en/refs/unit.env.ref#L1-L28), [docs/zh_CN/refs/unit.env.ref:1-28](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/zh_CN/refs/unit.env.ref#L1-L28)

**Multi-Language Synchronization Strategy**

```mermaid
graph LR
    subgraph "Shared Resources"
        PY["Python Examples<br/>Language-agnostic code"]
        M5F2["UIFLOW2 Projects<br/>Visual blocks"]
        IMPL["Implementation<br/>API signatures"]
    end
    
    subgraph "English Documentation"
        RST_EN["docs/en/units/env.rst"]
        REF_EN["docs/en/refs/unit.env.ref<br/>PNG images"]
    end
    
    subgraph "Chinese Documentation"
        RST_ZH["docs/zh_CN/unit/env.rst"]
        REF_ZH["docs/zh_CN/refs/unit.env.ref<br/>SVG images"]
    end
    
    PY -->|"literalinclude"| RST_EN
    PY -->|"literalinclude"| RST_ZH
    
    M5F2 -->|"linked from"| REF_EN
    M5F2 -->|"linked from"| REF_ZH
    
    IMPL -->|"documents"| RST_EN
    IMPL -->|"documents"| RST_ZH
    
    REF_EN -->|"include"| RST_EN
    REF_ZH -->|"include"| RST_ZH
```

Sources: [docs/en/units/env.rst:13-30](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/en/units/env.rst#L13-L30), [docs/zh_CN/unit/env.rst:13-30](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/zh_CN/unit/env.rst#L13-L30)

## Integration Patterns

### Voice Assistant Preset Pipeline

The LLM module provides a preset voice assistant workflow that chains multiple AI components:

```mermaid
graph TB
    User["User Speech"]
    
    subgraph "Audio Capture"
        Audio["ApiAudio.setup()<br/>(llm.py:410-458)<br/>cap/play devices"]
    end
    
    subgraph "Keyword Detection"
        KWS["ApiKws.setup()<br/>(llm.py:653-700)<br/>keyword='HI JIMMY'"]
    end
    
    subgraph "Speech Recognition"
        ASR["ApiAsr.setup()<br/>(llm.py:702-753)<br/>streaming transcription"]
    end
    
    subgraph "Language Model"
        LLM["ApiLlm.setup()<br/>(llm.py:213-305)<br/>qwen2.5-0.5B"]
    end
    
    subgraph "Text-to-Speech"
        TTS["ApiTts.setup()<br/>(llm.py:509-580)<br/>single_speaker_english_fast"]
    end
    
    Output["Speaker Output"]
    
    User --> Audio
    Audio --> KWS
    KWS -->|"work_id forwarding"| ASR
    ASR -->|"transcribed text"| LLM
    LLM -->|"response text"| TTS
    TTS --> Audio
    Audio --> Output
    
    KWS -.->|"on_keyword_detected"| APP["User Callback"]
    ASR -.->|"on_asr_data_input"| APP
    LLM -.->|"on_llm_data_input"| APP
```

Sources: [m5stack/libs/module/llm.py:1195-1307+](), [examples/module/llm/llm_voice_assistant.m5f2:1](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/examples/module/llm/llm_voice_assistant.m5f2#L1)

### Documentation Cross-References

The documentation system maintains bidirectional links between different artifact types:

| Source Type | Target Type | Mechanism | Example |
|-------------|-------------|-----------|---------|
| **RST → .ref** | Include images/links | `.. include:: ../refs/unit.env.ref` | [docs/en/units/env.rst:4]() |
| **RST → Python** | Embed code | `.. literalinclude:: ../../../examples/unit/env/env_cores3.py` | [docs/en/units/env.rst:13-30]() |
| **RST → .m5f2** | Link visual examples | `\|env_cores3_example.m5f2\|` | [docs/en/refs/unit.env.ref:24-27]() |
| **Python → Implementation** | Import statements | `from unit import ENVUnit` | [examples/unit/env/env_cores3.py:9]() |
| **.m5f2 → Implementation** | Generated code | `blockly` JSON field | [examples/module/llm/llm_voice_assistant.m5f2:1]() |

Sources: [docs/en/units/env.rst:1-93](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/en/units/env.rst#L1-L93), [docs/en/refs/unit.env.ref:1-28](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/en/refs/unit.env.ref#L1-L28), [examples/unit/env/env_cores3.py:1-50](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/examples/unit/env/env_cores3.py#L1-L50)

## Work ID Management for Multi-Pipeline Scenarios

The LLM module tracks work IDs to support concurrent AI pipelines. Each `setup()` call returns a unique work ID that subsequent `inference()` calls must reference:

```mermaid
graph TB
    subgraph "Setup Phase - Returns work_ids"
        S1["llm.llm.setup()<br/>→ latest_llm_work_id"]
        S2["llm.vlm.setup()<br/>→ latest_vlm_work_id"]
        S3["llm.tts.setup()<br/>→ latest_tts_work_id"]
        S4["llm.yolo.setup()<br/>→ latest_yolo_work_id"]
    end
    
    subgraph "Inference Phase - Uses work_ids"
        I1["llm.llm.inference(work_id, text)"]
        I2["llm.vlm.inference_img(work_id, image)"]
        I3["llm.tts.inference(work_id, text)"]
        I4["llm.yolo.inference_img(work_id, image)"]
    end
    
    subgraph "Response Processing"
        MSG["msg.response_msg_list<br/>[{work_id, request_id, data}]"]
    end
    
    S1 -->|"llm_work_id_1"| I1
    S2 -->|"vlm_work_id_1"| I2
    S3 -->|"tts_work_id_1"| I3
    S4 -->|"yolo_work_id_1"| I4
    
    I1 --> MSG
    I2 --> MSG
    I3 --> MSG
    I4 --> MSG
    
    MSG -->|"filter by work_id"| APP["Application<br/>take_msg(request_id)"]
```

Sources: [m5stack/libs/module/llm.py:904-1307+](), [m5stack/libs/module/llm.py:40-92](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/libs/module/llm.py#L40-L92)

## Use Cases and Examples

### LLM Integration Examples

The firmware includes multiple example patterns for AI integration:

| Example | Primary APIs Used | Description |
|---------|-------------------|-------------|
| **llm_voice_assistant.m5f2** | KWS → ASR → LLM → TTS | Complete voice assistant with callbacks | 
| **text_assistant.m5f2** | LLM only | Text-based Q&A without audio |
| **kws_asr.m5f2** | KWS → ASR | Speech recognition triggered by keyword |
| **tts.m5f2** | TTS only | Text-to-speech synthesis |
| **yolo.m5f2** | Camera → YOLO | Object detection pipeline |

Sources: [examples/module/llm/llm_voice_assistant.m5f2:1](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/examples/module/llm/llm_voice_assistant.m5f2#L1), [examples/module/llm/text_assistant.m5f2:1](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/examples/module/llm/text_assistant.m5f2#L1), [examples/module/llm/kws_asr.m5f2:1](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/examples/module/llm/kws_asr.m5f2#L1), [examples/module/llm/tts.m5f2:1](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/examples/module/llm/tts.m5f2#L1), [examples/module/llm/yolo.m5f2:1](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/examples/module/llm/yolo.m5f2#L1)

### Documentation Examples

Documentation is organized by hardware package with consistent patterns:

| Package | Index File | Example Unit | Chinese Support |
|---------|-----------|--------------|-----------------|
| **Unit** | [docs/en/units/index.rst]() | env.rst, angle.rst, rgb.rst | [docs/zh_CN/unit/index.rst:1-24]() |
| **Module** | [docs/en/module/index.rst]() | llm.rst | [docs/zh_CN/module/index.rst]() |
| **HAT** | [docs/en/hats/index.rst]() | servo.rst, pir.rst | [docs/zh_CN/hat/index.rst]() |
| **M5UI** | [docs/en/m5ui/index.rst]() | bar.rst, label.rst | [docs/zh_CN/m5ui/index.rst]() |

Sources: [docs/zh_CN/unit/index.rst:1-24](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/zh_CN/unit/index.rst#L1-L24), [docs/en/units/env.rst:1-93](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/en/units/env.rst#L1-L93), [docs/zh_CN/unit/env.rst:1-92](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/docs/zh_CN/unit/env.rst#L1-L92)