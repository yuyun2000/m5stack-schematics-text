StackFlow Installation Methods

# Packaging System

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [README.md](README.md)
- [README_zh.md](README_zh.md)
- [doc/component_doc/StackFlow_en.md](doc/component_doc/StackFlow_en.md)
- [doc/component_doc/StackFlow_zh.md](doc/component_doc/StackFlow_zh.md)
- [projects/llm_framework/README.md](projects/llm_framework/README.md)
- [projects/llm_framework/main_llm/SConstruct](projects/llm_framework/main_llm/SConstruct)
- [projects/llm_framework/main_openai_api/SConstruct](projects/llm_framework/main_openai_api/SConstruct)
- [projects/llm_framework/main_vlm/SConstruct](projects/llm_framework/main_vlm/SConstruct)
- [projects/llm_framework/tools/llm_pack.py](projects/llm_framework/tools/llm_pack.py)

</details>



The StackFlow framework uses a Debian-based packaging system to distribute components, libraries, and AI models. This document outlines the structure, creation process, and management of Debian packages (.deb files) used in the StackFlow ecosystem. For information about the build system that generates the binaries packaged in these .deb files, see [Build System](#4.1).

## 1. Package Types

StackFlow's packaging system divides components into three distinct package types:

```mermaid
graph TD
    subgraph "StackFlow Package Types"
        LibraryPackage["Library Packages"]
        BinaryPackage["Binary Packages"]
        ModelPackage["Model Packages"]
    end
    
    LibraryPackage -->|"provides"| CoreLibraries["Core Libraries (lib-llm)"]
    BinaryPackage -->|"includes"| ServiceExecutables["Service Executables (llm-sys, llm-llm, etc.)"]
    ModelPackage -->|"contains"| AIModels["AI Models (llm-model-*)"]
    
    CoreLibraries -->|"dependency for"| ServiceExecutables
    CoreLibraries -->|"dependency for"| AIModels
```

| Package Type | Prefix | Purpose | Example |
|--------------|--------|---------|---------|
| Library | lib- | Core shared libraries and utilities | lib-llm |
| Binary | llm- | Service executables with systemd services | llm-sys, llm-audio, llm-llm |
| Model | llm-model- | AI model data and configurations | llm-model-qwen2.5-0.5B-prefill-20e |

Sources: [projects/llm_framework/tools/llm_pack.py:23-21]()

## 2. Package Structure

Each package type follows a standardized directory structure to organize files properly within the Debian package:

### 2.1 Library Package Structure

```mermaid
graph TD
    subgraph "lib-llm Package"
        DebianControl["DEBIAN/control"]
        DebianScripts["DEBIAN/postinst + prerm"]
        LibFiles["opt/m5stack/lib/*.so"]
        ShareFiles["opt/m5stack/share/*"]
        PythonLibs["usr/local/lib/python3.10/dist-packages/*"]
    end
```

Library packages contain shared libraries (.so files), support files, and Python dependencies needed by other components.

Sources: [projects/llm_framework/tools/llm_pack.py:24-149]()

### 2.2 Binary Package Structure

```mermaid
graph TD
    subgraph "Binary Package (e.g., llm-sys)"
        DebianControl["DEBIAN/control"]
        DebianScripts["DEBIAN/postinst + prerm"]
        Executable["opt/m5stack/bin/llm_*"]
        SystemdService["lib/systemd/system/*.service"]
        Scripts["opt/m5stack/scripts/*"]
    end
```

Binary packages include executable files, systemd service configurations, and optional script files.

Sources: [projects/llm_framework/tools/llm_pack.py:225-295]()

### 2.3 Model Package Structure

```mermaid
graph TD
    subgraph "Model Package (e.g., llm-model-qwen2.5)"
        DebianControl["DEBIAN/control"]
        DebianScripts["DEBIAN/postinst + prerm"]
        ModelData["opt/m5stack/data/models/*"]
        ModelConfig["opt/m5stack/data/models/mode_*.json"]
        Scripts["opt/m5stack/scripts/*"]
    end
```

Model packages contain model files and configuration data needed by specific AI components.

Sources: [projects/llm_framework/tools/llm_pack.py:151-223]()

## 3. Package Naming Convention

StackFlow packages follow a standardized naming convention:

```
{package_name}_{version}-{revision}_{architecture}.deb
```

For example:
- `lib-llm_1.6-m5stack1_arm64.deb`
- `llm-sys_1.5-m5stack1_arm64.deb`
- `llm-model-qwen2.5-0.5B-prefill-20e_0.2-m5stack1_arm64.deb`

Sources: [projects/llm_framework/tools/llm_pack.py:13-21]()

## 4. Package Creation Process

The packaging system automates the creation of Debian packages through specialized functions in the `llm_pack.py` script:

```mermaid
sequenceDiagram
    participant Build as Build System
    participant PackScript as llm_pack.py
    participant LibFunc as create_lib_deb()
    participant BinFunc as create_bin_deb()
    participant ModelFunc as create_data_deb()
    participant DebPkg as dpkg-deb
    
    Build->>PackScript: Generate binaries
    PackScript->>LibFunc: Create library package
    PackScript->>BinFunc: Create binary packages
    PackScript->>ModelFunc: Create model packages
    
    LibFunc->>LibFunc: Create package structure
    LibFunc->>LibFunc: Copy libraries and files
    LibFunc->>LibFunc: Create DEBIAN/control
    LibFunc->>LibFunc: Create scripts
    LibFunc->>DebPkg: Package using dpkg-deb
    
    BinFunc->>BinFunc: Create package structure
    BinFunc->>BinFunc: Copy executables
    BinFunc->>BinFunc: Create systemd service
    BinFunc->>BinFunc: Create DEBIAN/control
    BinFunc->>BinFunc: Create scripts
    BinFunc->>DebPkg: Package using dpkg-deb
    
    ModelFunc->>ModelFunc: Create package structure
    ModelFunc->>ModelFunc: Download/extract model data
    ModelFunc->>ModelFunc: Copy model configs
    ModelFunc->>ModelFunc: Create DEBIAN/control
    ModelFunc->>ModelFunc: Create scripts
    ModelFunc->>DebPkg: Package using dpkg-deb
```

### 4.1 Library Package Creation

The `create_lib_deb()` function generates library packages with the following steps:
1. Create a temporary Debian package structure
2. Copy library files to appropriate locations
3. Download and extract additional dependencies
4. Generate DEBIAN control files and scripts
5. Build the package using dpkg-deb

Sources: [projects/llm_framework/tools/llm_pack.py:24-149]()

### 4.2 Binary Package Creation

The `create_bin_deb()` function generates binary packages with the following steps:
1. Create a temporary Debian package structure
2. Copy executable files to appropriate locations
3. Generate systemd service files
4. Generate DEBIAN control files and scripts
5. Build the package using dpkg-deb

Sources: [projects/llm_framework/tools/llm_pack.py:225-295]()

### 4.3 Model Package Creation

The `create_data_deb()` function generates model packages with the following steps:
1. Create a temporary Debian package structure
2. Download model data from remote server
3. Extract and organize model files
4. Copy model configuration files
5. Generate DEBIAN control files and scripts
6. Build the package using dpkg-deb

Sources: [projects/llm_framework/tools/llm_pack.py:151-223]()

## 5. Package Dependencies

The packaging system establishes dependencies between packages to ensure proper installation order and component compatibility:

```mermaid
graph TD
    subgraph "Core Dependencies"
        libllm["lib-llm"]
        llmsys["llm-sys"]
    end
    
    subgraph "Service Modules"
        llmaudio["llm-audio"]
        llmkws["llm-kws"]
        llmasr["llm-asr"]
        llmllm["llm-llm"]
        llmtts["llm-tts"]
        llmcamera["llm-camera"]
        llmyolo["llm-yolo"]
        llmvlm["llm-vlm"]
        llmmelotts["llm-melotts"]
    end
    
    subgraph "Model Packages"
        llmmodelkws["llm-model-sherpa-onnx-kws-*"]
        llmmodellm["llm-model-qwen2.5-*"]
        llmmodelyolo["llm-model-yolo11n"]
        llmmodeltts["llm-model-melotts-zh-cn"]
    end
    
    libllm -->|"depends on"| llmsys
    libllm -->|"depends on"| llmaudio
    libllm -->|"depends on"| llmkws
    libllm -->|"depends on"| llmasr
    libllm -->|"depends on"| llmllm
    libllm -->|"depends on"| llmtts
    libllm -->|"depends on"| llmcamera
    libllm -->|"depends on"| llmyolo
    libllm -->|"depends on"| llmvlm
    libllm -->|"depends on"| llmmelotts
    
    llmsys -->|"required by"| llmaudio
    llmsys -->|"required by"| llmkws
    llmsys -->|"required by"| llmasr
    llmsys -->|"required by"| llmllm
    llmsys -->|"required by"| llmtts
    llmsys -->|"required by"| llmcamera
    llmsys -->|"required by"| llmyolo
    llmsys -->|"required by"| llmvlm
    llmsys -->|"required by"| llmmelotts
    
    llmkws -->|"uses"| llmmodelkws
    llmllm -->|"uses"| llmmodellm
    llmyolo -->|"uses"| llmmodelyolo
    llmmelotts -->|"uses"| llmmodeltts
```

Key dependencies defined in the control files:
- All packages depend on `lib-llm`
- All service packages depend on `llm-sys`
- Model packages have specific version requirements

Sources: [projects/llm_framework/tools/llm_pack.py:90-100](), [projects/llm_framework/tools/llm_pack.py:196-211](), [projects/llm_framework/tools/llm_pack.py:248-259]()

## 6. Service Management

Binary packages automatically configure systemd services during installation:

| Action | Script | Purpose |
|--------|--------|---------|
| Installation | postinst | Enable and start services |
| Removal | prerm | Stop and disable services |

Service files specify dependencies to ensure proper startup order:

```ini
[Unit]
Description=llm-* Service
After=llm-sys.service
Requires=llm-sys.service

[Service]
ExecStart=/opt/m5stack/bin/llm_*
WorkingDirectory=/opt/m5stack
Restart=always
RestartSec=1
StartLimitInterval=0

[Install]
WantedBy=multi-user.target
```

Sources: [projects/llm_framework/tools/llm_pack.py:101-122](), [projects/llm_framework/tools/llm_pack.py:123-142](), [projects/llm_framework/tools/llm_pack.py:271-287]()

## 7. Example: OpenAI API Package

The OpenAI API package demonstrates how specialized components are integrated into the packaging system:

```mermaid
graph TD
    subgraph "llm-openai-api Package"
        Executable["opt/m5stack/bin/llm_openai_api"]
        ServiceFile["lib/systemd/system/llm-openai-api.service"]
        PluginRepo["opt/m5stack/bin/ModuleLLM-OpenAI-Plugin/*"]
        PythonEnv["opt/m5stack/lib/openai-api/*"]
    end
    
    Executable -->|"sets PYTHONPATH"| PythonEnv
    Executable -->|"executes"| PluginRepo
    ServiceFile -->|"starts"| Executable
```

Special handling for the OpenAI API component:
1. Download GitHub repository for the API plugin
2. Download Python virtual environment with dependencies
3. Configure executable to set proper Python path
4. Set up service file to start the API server

Sources: [projects/llm_framework/main_openai_api/SConstruct:21-33](), [projects/llm_framework/main_openai_api/src/main.cpp:10-23](), [projects/llm_framework/tools/llm_pack.py:234-246]()

## 8. Version Management

The packaging system implements a versioning policy to manage compatibility:

```mermaid
graph TD
    subgraph "Version Management Policy"
        MajorVersion["Major Version"]
        MinorVersion["Minor Version"]
    end
    
    MajorVersion -->|"increment when"| Incompatible["Components become incompatible"]
    MinorVersion -->|"increment for"| Compatible["Compatible changes"]
    
    subgraph "Version Examples"
        LibVersion["lib-llm: 1.6"]
        BinVersion["llm-sys: 1.5"]
        ModelVersion["llm-model-*: 0.2-0.4"]
    end
```

Key versioning rules:
- Increment major version when units become incompatible with previous versions
- Increment major version when models become incompatible with previous versions
- Maintain consistent major version numbers between acceleration units and model units
- Model versions typically start at 0.1 and increment for updates

Sources: [projects/llm_framework/tools/llm_pack.py:323-363](), [projects/llm_framework/tools/llm_pack.py:366-413]()

## 9. Packaging Workflow

The packaging script supports both individual and batch package creation:

```mermaid
flowchart TD
    Start["Start llm_pack.py"] -->|"No arguments"| BatchMode["Batch Mode"]
    Start -->|"Package name argument"| SingleMode["Single Package Mode"]
    Start -->|"clean argument"| CleanMode["Clean Mode"]
    
    BatchMode -->|"create_lib=True"| CreateLib["Create Library Packages"]
    BatchMode -->|"create_bin=True"| CreateBin["Create Binary Packages"]
    BatchMode -->|"create_data=True"| CreateModel["Create Model Packages"]
    
    CreateLib --> ThreadPool["Thread Pool Executor"]
    CreateBin --> ThreadPool
    CreateModel --> ThreadPool
    
    ThreadPool -->|"Concurrent execution"| PackageCreation["Package Creation Functions"]
    PackageCreation --> OutputPackages["Output .deb Files"]
    
    SingleMode -->|"Lookup in Tasks dict"| SpecificPackage["Create Specific Package"]
    SpecificPackage --> OutputPackage["Output .deb File"]
    
    CleanMode -->|"Remove artifacts"| CleanUp["Clean Up Build Files"]
```

The packaging script uses concurrent execution to efficiently create multiple packages in parallel, with configurability for batch or individual package generation.

Sources: [projects/llm_framework/tools/llm_pack.py:297-441]()