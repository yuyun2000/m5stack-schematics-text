# Build and Deployment System

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [.github/workflows/build-release.yml](.github/workflows/build-release.yml)
- [.github/workflows/code_formatting.yml](.github/workflows/code_formatting.yml)
- [.github/workflows/nightly-build.yml](.github/workflows/nightly-build.yml)
- [.github/workflows/ports_m5stack.yml](.github/workflows/ports_m5stack.yml)
- [.gitlab-ci.yml](.gitlab-ci.yml)
- [README.md](README.md)
- [m5stack/Makefile](m5stack/Makefile)
- [m5stack/boards/M5STACK_AtomS3R_CAM/board.json](m5stack/boards/M5STACK_AtomS3R_CAM/board.json)
- [m5stack/boards/M5STACK_AtomS3R_CAM/mpconfigboard.cmake](m5stack/boards/M5STACK_AtomS3R_CAM/mpconfigboard.cmake)
- [m5stack/boards/M5STACK_AtomS3R_CAM/mpconfigboard.h](m5stack/boards/M5STACK_AtomS3R_CAM/mpconfigboard.h)
- [m5stack/boards/M5STACK_AtomS3R_CAM/sdkconfig.board](m5stack/boards/M5STACK_AtomS3R_CAM/sdkconfig.board)
- [m5stack/boards/M5STACK_Atom_Lite/mpconfigboard.h](m5stack/boards/M5STACK_Atom_Lite/mpconfigboard.h)
- [m5stack/boards/M5STACK_Atom_Lite/sdkconfig.board](m5stack/boards/M5STACK_Atom_Lite/sdkconfig.board)
- [m5stack/boards/M5STACK_CoreInk/mpconfigboard.cmake](m5stack/boards/M5STACK_CoreInk/mpconfigboard.cmake)
- [m5stack/boards/M5STACK_CoreInk/mpconfigboard.h](m5stack/boards/M5STACK_CoreInk/mpconfigboard.h)
- [m5stack/boards/M5STACK_CoreInk/sdkconfig.board](m5stack/boards/M5STACK_CoreInk/sdkconfig.board)
- [m5stack/libs/driver/neopixel/__init__.py](m5stack/libs/driver/neopixel/__init__.py)
- [m5stack/libs/driver/neopixel/ws2812.py](m5stack/libs/driver/neopixel/ws2812.py)
- [m5stack/libs/hardware/rgb.py](m5stack/libs/hardware/rgb.py)
- [m5stack/modules/startup/__init__.py](m5stack/modules/startup/__init__.py)
- [m5stack/modules/startup/atoms3.py](m5stack/modules/startup/atoms3.py)
- [m5stack/modules/startup/atoms3lite.py](m5stack/modules/startup/atoms3lite.py)
- [m5stack/modules/startup/atoms3u.py](m5stack/modules/startup/atoms3u.py)
- [m5stack/modules/startup/manifest_coreink.py](m5stack/modules/startup/manifest_coreink.py)
- [m5stack/modules/startup/stamps3.py](m5stack/modules/startup/stamps3.py)
- [third-party/Makefile](third-party/Makefile)
- [tools/ci.sh](tools/ci.sh)

</details>



## Purpose and Scope

This document describes the multi-platform build and deployment infrastructure for the UIFlow MicroPython firmware, which supports 40+ ESP32-based board variants. The system orchestrates:

- **Build System Architecture** ([Section 5.1](#5.1)): Makefile-based build orchestration, board configuration mapping, filesystem packaging, and dependency management
- **CI/CD Pipeline** ([Section 5.2](#5.2)): Automated continuous integration using GitHub Actions and GitLab CI with ESP-IDF caching and parallel builds
- **Board Configurations and Firmware Assembly** ([Section 5.3](#5.3)): Hierarchical configuration composition, board-specific customizations, and final firmware packaging

For information about the runtime boot sequence that follows deployment, see [Boot Process and ESP32 Features](#4.2).

---

## Build System Overview

The build system uses GNU Make as the primary orchestration layer, wrapping ESP-IDF's CMake-based `idf.py` tool. It manages 40+ board variants across two build trees: `m5stack/` for M5Stack devices and `third-party/` for partner boards.

### Build Target Hierarchy

```mermaid
graph TB
    all["all (default)"]
    nvs["nvs"]
    fs["fs"]
    pack["pack"]
    pack_all["pack_all"]
    build["build"]
    deploy["deploy"]
    flash["flash"]
    flash_all["flash_all"]
    clean["clean"]
    
    all --> nvs
    all --> fs
    all --> pack
    
    nvs --> nvs_bin["$(BUILD)/nvs.bin<br/>0x6000 bytes"]
    
    fs --> build
    build --> bootloader["$(BUILD)/bootloader/bootloader.bin"]
    build --> partition["$(BUILD)/partition_table/partition-table.bin"]
    build --> firmware["$(BUILD)/micropython.bin"]
    
    fs --> fs_system["$(BUILD)/fs-system.bin"]
    fs --> fs_user["$(BUILD)/fs-user.bin"]
    
    pack --> nvs
    pack --> fs
    pack --> pack_bin["$(BUILD)/uiflow-$(GIT_VERSION).bin<br/>Without user fs"]
    
    pack_all --> nvs
    pack_all --> fs
    pack_all --> pack_all_bin["$(BUILD)/uiflow-$(GIT_VERSION).bin<br/>With user fs<br/>$(BUILD)/uiflow-Sx-$(GIT_VERSION).uf2"]
    
    deploy --> build
    deploy --> idf_flash["idf.py flash"]
    
    flash --> pack
    flash --> esptool["esptool.py write_flash 0x0"]
    
    flash_all --> pack_all
    flash_all --> esptool
    
    clean --> idf_clean["idf.py fullclean"]
    
    style nvs_bin fill:#f9f9f9
    style fs_system fill:#f9f9f9
    style fs_user fill:#f9f9f9
    style pack_bin fill:#f9f9f9
    style pack_all_bin fill:#f9f9f9
```

**Target Descriptions:**

| Target | Purpose | Output Files |
|--------|---------|--------------|
| `nvs` | Generate NVS partition for configuration storage | `$(BUILD)/nvs.bin` (24KB fixed) |
| `build` | Compile MicroPython firmware via `idf.py build` | `bootloader.bin`, `partition-table.bin`, `micropython.bin` |
| `fs` | Package filesystem partitions using LittleFS2 | `fs-system.bin`, `fs-user.bin` |
| `pack` | Assemble complete firmware without user filesystem | `uiflow-$(GIT_VERSION).bin` |
| `pack_all` | Assemble firmware with user filesystem | `uiflow-$(GIT_VERSION).bin`, `uiflow-Sx-$(GIT_VERSION).uf2` |
| `flash` | Flash firmware via esptool | - |
| `deploy` | Flash firmware via idf.py (development) | - |
| `clean` | Remove build artifacts | - |

Sources: [m5stack/Makefile:173-261](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/Makefile#L173-L261)

---

### Board Configuration System

The build system maps board names to board types and configures build flags accordingly:

```mermaid
graph LR
    subgraph "Board Name to Type Mapping"
        BOARD["BOARD variable<br/>M5STACK_CoreInk"]
        boards_list["boards list<br/>M5STACK_CoreInk:coreink"]
        find_board["find_board function"]
        BOARD_TYPE["BOARD_TYPE=coreink"]
        
        BOARD --> find_board
        boards_list --> find_board
        find_board --> BOARD_TYPE
    end
    
    subgraph "Tiny Board Detection"
        BOARD --> tiny_check["Check in TINY_BOARD_TYPE_DEF"]
        tiny_check -->|match| TINY_FLAG_1["TINY_FLAG=1"]
        tiny_check -->|no match| TINY_FLAG_0["TINY_FLAG=0"]
    end
    
    subgraph "Build Directory"
        BOARD --> BUILD["BUILD=build-$(BOARD)<br/>build-M5STACK_CoreInk"]
    end
    
    subgraph "IDF Flags"
        BOARD_TYPE --> IDFPY["IDFPY_FLAGS<br/>-DMICROPY_BOARD=$(BOARD)<br/>-DBOARD_TYPE=$(BOARD_TYPE)<br/>-B$(BUILD)"]
    end
    
    TINY_FLAG_1 -.affects.-> fs_tiny["Tiny FS Build<br/>Single combined partition"]
    TINY_FLAG_0 -.affects.-> fs_normal["Normal FS Build<br/>Separate system/user"]
```

**Board Type Definitions:**

The `boards` variable maps board names to types using the pattern `BOARD_NAME:board-type`:

```
M5STACK_AtomS3:atoms3
M5STACK_CoreInk:coreink
M5STACK_CoreS3:cores3
M5STACK_NanoC6:nanoc6
...
```

The `find_board` function extracts the type from this mapping. Board types determine which directory in `fs/system/` is packaged into `fs-system.bin`.

**Tiny Board Handling:**

Boards with limited flash (4MB or less) have `TINY_FLAG=1`:

```
TINY_BOARD_TYPE_DEF = \
    M5STACK_StickC_PLUS \
    M5STACK_Basic_4MB   \
    M5STACK_CoreInk     \
    M5STACK_StickC      \
    M5STACK_Atom_Lite   \
    M5STACK_Stamp_PICO  \
    M5STACK_Atom_Matrix \
    M5STACK_AtomU       \
    M5STACK_Atom_Echo   \
    M5STACK_NanoC6
```

For tiny boards, the filesystem build combines base files into a single user partition instead of maintaining separate system and user partitions.

Sources: [m5stack/Makefile:11-116](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/Makefile#L11-L116), [m5stack/Makefile:223-252](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/Makefile#L223-L252)

---

### Patch Management System

The build system applies custom patches to upstream dependencies to fix bugs and add features:

```mermaid
graph TB
    subgraph "Patch Targets"
        LV_BINDING["lv_binding_micropython<br/>$(LV_BINDING_PATH)"]
        MICROPYTHON["micropython<br/>$(MICROPYTHON_PATH)"]
        IDF["esp-idf<br/>$(IDF_PATH)"]
        M5UNIFIED["M5Unified<br/>$(M5UNIFIED_PATH)"]
        ADF["esp-adf<br/>$(ADF_PATH)"]
        M5GFX["M5GFX<br/>$(M5GFX_PATH)"]
        ESP32CAM["esp32-camera<br/>$(ESP32_CAMERA_PATH)"]
    end
    
    subgraph "Patch Series"
        LV_PATCHES["LV_BINDING_PATCH_SERIES<br/>0003-avoid-lv_bindings-compile-error.patch<br/>0018-avoid-lvgl-font-redefine.patch"]
        
        MP_PATCHES["MICROPYTHON_PATCH_SERIES<br/>0006-modtime-add-timezone-method.patch<br/>0009-micropython-1.25.0-add-esp32p4-pins.patch<br/>0010-micropython-1.25.0-machine-adc-v5.x.patch<br/>0011-micropython-1.25.0-fix-esp32-p4-pwm.patch<br/>...8 more patches"]
        
        IDF_PATCHES["IDF_PATH_PATCH_SERIES<br/>1004-idf_v5.4_freertos.patch"]
        
        M5U_PATCHES["M5UNIFIED_PATCH_SERIES<br/>2006-Support-LTR553.patch"]
        
        ADF_PATCHES["ADF_PATCH_SERIES<br/>3002-Modify-i2s_stream_idf5.patch"]
        
        M5G_PATCHES["M5GFX_PATCH_SERIES<br/>4002-M5GFX-use-i2c-driver.patch"]
        
        CAM_PATCHES["ESP32_CAMERA_PATCH_SERIES<br/>5001-Add-software-i2c-support.patch"]
    end
    
    subgraph "Patch Operations"
        patch_cmd["make patch"]
        unpatch_cmd["make unpatch"]
        prepare_cmd["make PKG prepare"]
        update_cmd["make PKG update"]
    end
    
    LV_BINDING --> LV_PATCHES
    MICROPYTHON --> MP_PATCHES
    IDF --> IDF_PATCHES
    M5UNIFIED --> M5U_PATCHES
    ADF --> ADF_PATCHES
    M5GFX --> M5G_PATCHES
    ESP32CAM --> CAM_PATCHES
    
    LV_PATCHES --> patch_cmd
    MP_PATCHES --> patch_cmd
    IDF_PATCHES --> patch_cmd
    M5U_PATCHES --> patch_cmd
    ADF_PATCHES --> patch_cmd
    M5G_PATCHES --> patch_cmd
    CAM_PATCHES --> patch_cmd
    
    patch_cmd -.applies.-> LV_BINDING
    patch_cmd -.applies.-> MICROPYTHON
    patch_cmd -.applies.-> IDF
    patch_cmd -.applies.-> M5UNIFIED
    patch_cmd -.applies.-> ADF
    patch_cmd -.applies.-> M5GFX
    patch_cmd -.applies.-> ESP32CAM
```

**Key Patch Functions:**

The patch system uses utility functions defined in `m5stack/include/files.mk`:

- `Patch/prepare`: Applies a series of patches to a package
- `Patch/clean`: Unapplies patches from a package  
- `Patch/update`: Updates patch files from modified package

**Example: MicroPython Patches**

The 12 MicroPython patches add critical functionality:

1. `0006-modtime-add-timezone-method.patch`: Adds timezone support to `time` module
2. `0009-micropython-1.25.0-add-esp32p4-pins.patch`: Enables ESP32-P4 support
3. `0010-micropython-1.25.0-machine-adc-v5.x.patch`: Fixes ADC for ESP-IDF v5.x
4. `0011-micropython-1.25.0-fix-esp32-p4-pwm.patch`: PWM fixes for ESP32-P4
5. `0017-micropython-1.25.0-add-uart-mode.patch`: UART mode configuration
6. `0018-micropython-1.25.0-support-esp-idf-v5.4.2.patch`: ESP-IDF v5.4.2 compatibility

Sources: [m5stack/Makefile:298-404](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/Makefile#L298-L404)

---

### Filesystem Packaging

The filesystem packaging process creates LittleFS2 partitions from directory trees:

```mermaid
graph TB
    subgraph "Source Directories"
        fs_system["./fs/system/<br/>Board-specific system files"]
        fs_user["./fs/user/<br/>User application files"]
        board_type_dir["./fs/system/$(BOARD_TYPE)/<br/>e.g., ./fs/system/coreink/"]
    end
    
    subgraph "Packaging Tool"
        fs_packed["tools/fs_packed.py"]
        littlefs2["tools/littlefs/prebuilt/littlefs2<br/>LittleFS2 image creator"]
        partition_table["$(BUILD)/partition_table/partition-table.bin<br/>Partition layout"]
    end
    
    subgraph "Output Images"
        fs_system_bin["$(BUILD)/fs-system.bin<br/>System partition"]
        fs_user_bin["$(BUILD)/fs-user.bin<br/>User partition"]
    end
    
    subgraph "Tiny Board Path"
        base_files["$(BUILD)/base-files/<br/>Merged files"]
        base_files_install["base-files/install function<br/>Copies board-specific files"]
        tiny_fs_user["$(BUILD)/fs-user.bin<br/>Combined partition"]
    end
    
    fs_system --> fs_packed
    fs_user --> fs_packed
    board_type_dir -.selected by BOARD_TYPE.-> fs_packed
    
    littlefs2 --> fs_packed
    partition_table --> fs_packed
    
    fs_packed -->|TINY_FLAG=0| fs_system_bin
    fs_packed -->|TINY_FLAG=0| fs_user_bin
    
    fs_packed -->|TINY_FLAG=1| base_files_install
    base_files_install --> base_files
    base_files --> fs_packed
    fs_packed -->|TINY_FLAG=1| tiny_fs_user
```

**Normal Filesystem Build (TINY_FLAG=0):**

For boards with sufficient flash, two separate LittleFS2 partitions are created:

```python
# System partition
python tools/fs_packed.py \
    tools/littlefs/prebuilt/littlefs2 \
    $(BOARD_TYPE) \
    ./fs/system \
    $(BUILD)/fs-system.bin \
    $(BUILD)/partition_table/partition-table.bin

# User partition
python tools/fs_packed.py \
    tools/littlefs/prebuilt/littlefs2 \
    $(BOARD_TYPE) \
    ./fs/user \
    $(BUILD)/fs-user.bin \
    $(BUILD)/partition_table/partition-table.bin
```

**Tiny Filesystem Build (TINY_FLAG=1):**

For flash-constrained boards, system files are merged into the user partition:

```make
@if [ ! -d $(BUILD)/base-files ]; then \
    mkdir -p $(BUILD)/base-files; \
fi
$(call base-files/install,$(BOARD_TYPE),$(BUILD)/base-files)
@$(PYTHON) \
    ./../tools/fs_packed.py \
    ./../tools/littlefs/prebuilt/littlefs2 \
    $(BOARD_TYPE) \
    $(BUILD)/base-files \
    $(BUILD)/fs-user.bin \
    $(BUILD)/partition_table/partition-table.bin
```

The `base-files/install` function (defined in `m5stack/include/files.mk`) copies board-specific startup modules and configurations into the merged directory.

Sources: [m5stack/Makefile:222-252](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/Makefile#L222-L252)

---

### Firmware Assembly

The final firmware assembly combines all binary components into flashable images:

```mermaid
graph LR
    subgraph "Input Components"
        sdkconfig["$(BUILD)/sdkconfig<br/>Build configuration"]
        bootloader_bin["$(BUILD)/bootloader/bootloader.bin<br/>First-stage bootloader"]
        partition_table["$(BUILD)/partition_table/partition-table.bin<br/>Partition layout"]
        nvs_bin["$(BUILD)/nvs.bin<br/>NVS configuration (24KB)"]
        micropython_bin["$(BUILD)/micropython.bin<br/>MicroPython firmware"]
        fs_system_bin["$(BUILD)/fs-system.bin<br/>System filesystem"]
        fs_user_bin["$(BUILD)/fs-user.bin<br/>User filesystem (optional)"]
    end
    
    subgraph "Assembly Tool"
        makeimg["tools/makeimg.py"]
        GIT_VERSION["GIT_VERSION=$(shell git rev-parse --short HEAD)"]
        BOARD_TYPE_var["BOARD_TYPE variable"]
        LVGL_FLAG_var["LVGL_FLAG variable"]
    end
    
    subgraph "Output Formats"
        final_bin["$(BUILD)/uiflow-$(GIT_VERSION).bin<br/>Complete flashable image"]
        final_uf2["$(BUILD)/uiflow-Sx-$(GIT_VERSION).uf2<br/>USB MSC flashable image"]
    end
    
    sdkconfig --> makeimg
    bootloader_bin --> makeimg
    partition_table --> makeimg
    nvs_bin --> makeimg
    micropython_bin --> makeimg
    fs_system_bin --> makeimg
    fs_user_bin -.pack_all only.-> makeimg
    
    GIT_VERSION --> makeimg
    BOARD_TYPE_var --> makeimg
    LVGL_FLAG_var --> makeimg
    
    makeimg --> final_bin
    makeimg --> final_uf2
```

**pack_fw Function:**

The Makefile defines a `pack_fw` function that invokes `makeimg.py`:

```make
define pack_fw
	$(1) makeimg.py \
		$(BUILD)/sdkconfig \
		$(BUILD)/bootloader/bootloader.bin \
		$(BUILD)/partition_table/partition-table.bin \
		$(BUILD)/nvs.bin \
		$(BUILD)/micropython.bin \
		$(BUILD)/fs-system.bin \
		$(2) \
		$(BOARD_TYPE) \
		$(LVGL_FLAG) \
		$(BUILD)/uiflow-$(GIT_VERSION).bin \
		$(BUILD)/uiflow-Sx-$(GIT_VERSION).uf2
endef
```

**Usage:**

```make
# Pack without user filesystem (release builds)
pack: fs
	$(call pack_fw,$(PYTHON),none)

# Pack with user filesystem (development builds)
pack_all: fs
	$(call pack_fw,$(PYTHON),$(BUILD)/fs-user.bin)
```

**Output Files:**

- `uiflow-$(GIT_VERSION).bin`: Complete binary image flashable at address 0x0
- `uiflow-Sx-$(GIT_VERSION).uf2`: UF2 format for boards with USB MSC bootloader support

Sources: [m5stack/Makefile:156-169](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/Makefile#L156-L169), [m5stack/Makefile:254-261](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/Makefile#L254-L261)

---

## CI/CD Pipeline Architecture

The CI/CD system provides automated builds across multiple platforms using GitHub Actions and GitLab CI, with aggressive caching to optimize build times.

### CI Function Organization

The `tools/ci.sh` script provides modular shell functions for different CI stages:

```mermaid
graph TB
    subgraph "Setup Functions"
        ci_code_formatting_setup["ci_code_formatting_setup<br/>Install uncrustify, black, ruff"]
        ci_esp32_idf542_setup["ci_esp32_idf542_setup<br/>Clone ESP-IDF v5.4.2<br/>Install toolchains"]
    end
    
    subgraph "Build Functions"
        ci_esp32_nightly_build["ci_esp32_nightly_build<br/>Build all 40+ boards<br/>m5stack + third-party"]
        ci_esp32_quick_build["ci_esp32_quick_build<br/>Build subset of boards"]
        ci_unit_build["ci_unit_build<br/>Build unit testing boards"]
        ci_module_build["ci_module_build<br/>Build module testing boards"]
        ci_base_build["ci_base_build<br/>Build base testing boards"]
        ci_hat_build["ci_hat_build<br/>Build HAT testing boards"]
    end
    
    subgraph "Formatting Functions"
        ci_code_formatting_run["ci_code_formatting_run<br/>Run codeformat.py -c -f"]
    end
    
    subgraph "Common Steps"
        source_idf["source esp-idf/export.sh"]
        pip_install["pip install future"]
        make_submodules["make -C m5stack submodules"]
        make_unpatch["make -C m5stack unpatch"]
        make_patch["make -C m5stack patch"]
        make_littlefs["make -C m5stack littlefs"]
        make_mpy_cross["make -C m5stack mpy-cross"]
    end
    
    ci_esp32_nightly_build --> source_idf
    ci_esp32_quick_build --> source_idf
    ci_unit_build --> source_idf
    ci_module_build --> source_idf
    ci_base_build --> source_idf
    ci_hat_build --> source_idf
    
    source_idf --> pip_install
    pip_install --> make_unpatch
    make_unpatch --> make_submodules
    make_submodules --> make_patch
    make_patch --> make_littlefs
    make_littlefs --> make_mpy_cross
    
    make_mpy_cross --> board_builds["make BOARD=XXX pack_all<br/>Parallel board builds"]
```

**Build Function Patterns:**

Each build function follows a consistent pattern:

```bash
function ci_esp32_nightly_build {
    source esp-idf/export.sh
    pip install future
    make ${MAKEOPTS} -C m5stack unpatch
    make ${MAKEOPTS} -C m5stack submodules
    make ${MAKEOPTS} -C m5stack patch
    make ${MAKEOPTS} -C m5stack littlefs
    make ${MAKEOPTS} -C m5stack mpy-cross
    make ${MAKEOPTS} -C m5stack BOARD=M5STACK_AirQ pack_all
    make ${MAKEOPTS} -C m5stack BOARD=M5STACK_AtomS3 pack_all
    # ... 40+ boards
    make ${MAKEOPTS} -C third-party BOARD=ESPRESSIF_ESP32_S3_BOX_3 pack_all
}
```

Sources: [tools/ci.sh:185-370](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/tools/ci.sh#L185-L370)

---

### GitHub Actions Workflow

The GitHub Actions workflows use a matrix strategy to parallelize board builds:

```mermaid
graph TB
    subgraph "Workflow Triggers"
        push["push event"]
        pr["pull_request event"]
        schedule["schedule: cron 0 0 * * *"]
        workflow_dispatch["workflow_dispatch (manual)"]
    end
    
    subgraph "Setup Job"
        setup_checkout["actions/checkout@v4"]
        setup_deps["Install dependencies<br/>apt-get install git wget flex bison..."]
        setup_cache["actions/cache@v4<br/>key: ${{runner.os}}-idf-v5.4.2"]
        setup_idf["Install ESP-IDF v5.4.2<br/>if cache miss"]
        setup_env["Setup environment<br/>ci_esp32_idf542_setup"]
    end
    
    subgraph "Build Job Matrix"
        matrix_def["strategy.matrix.board<br/>40+ board variants<br/>max-parallel: 4"]
        
        build_m5stack["Build M5Stack boards<br/>make -C m5stack BOARD=${{matrix.board}} pack_all"]
        build_third_party["Build third-party boards<br/>make -C third-party BOARD=${{matrix.board}} pack_all"]
    end
    
    subgraph "Artifact Management"
        upload_artifact["actions/upload-artifact@v4<br/>name: firmware-${{matrix.board}}"]
        upload_release["softprops/action-gh-release@v2<br/>Upload to GitHub Release"]
    end
    
    push --> setup_checkout
    pr --> setup_checkout
    schedule --> setup_checkout
    workflow_dispatch --> setup_checkout
    
    setup_checkout --> setup_deps
    setup_deps --> setup_cache
    setup_cache --> setup_idf
    setup_idf --> setup_env
    
    setup_env -.provides cache.-> matrix_def
    
    matrix_def -->|startsWith 'M5STACK'| build_m5stack
    matrix_def -->|not startsWith 'M5STACK'| build_third_party
    
    build_m5stack --> upload_artifact
    build_third_party --> upload_artifact
    
    build_m5stack -.on tag push.-> upload_release
    build_third_party -.on tag push.-> upload_release
```

**Matrix Board List:**

The workflow defines 40+ boards in the build matrix:

```yaml
strategy:
  matrix:
    board:
      - M5STACK_AirQ
      - M5STACK_Atom_Echo
      - M5STACK_Atom_Lite
      - M5STACK_AtomS3
      - M5STACK_CoreS3
      - M5STACK_NanoC6
      # ... 34 more boards
      - ESPRESSIF_ESP32_S3_BOX_3
      - SEEED_STUDIO_XIAO_ESP32S3
  max-parallel: 4
```

**ESP-IDF Caching Strategy:**

The cache significantly reduces build times:

```yaml
- name: Cache esp-idf
  uses: actions/cache@v4
  id: cache-esp-idf
  with:
    path: |
      ~/.espressif
      ${{ github.workspace }}/esp-idf
    key: ${{ runner.os }}-idf-v5.4.2
```

This caches:
- `~/.espressif`: Toolchains, Python packages (~2GB)
- `esp-idf`: ESP-IDF source tree (~500MB)

Sources: [.github/workflows/nightly-build.yml:1-149](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/.github/workflows/nightly-build.yml#L1-L149), [.github/workflows/build-release.yml:1-153](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/.github/workflows/build-release.yml#L1-L153)

---

### GitLab CI Pipeline

The GitLab CI provides an alternative pipeline with similar functionality:

```mermaid
graph TB
    subgraph "Stages"
        code_format_stage["Stage: code_format"]
        docs_stage["Stage: docs"]
        build_stage["Stage: build"]
        release_stage["Stage: release"]
    end
    
    subgraph "code_format Job"
        cf_script["ci_code_formatting_setup<br/>ci_code_formatting_run<br/>git diff --exit-code"]
    end
    
    subgraph "build_docs Job"
        docs_script["sphinx-build zh_CN<br/>sphinx-build en"]
        docs_artifacts["artifacts:<br/>docs/build/"]
    end
    
    subgraph "build-job"
        build_cache["cache: ESP-IDF v5.4.2"]
        build_script["ci_esp32_idf542_setup<br/>ci_esp32_nightly_build"]
        build_artifacts["artifacts:<br/>m5stack/build-*/uiflow-*-*.bin<br/>third-party/build-*/uiflow-*-*.bin"]
    end
    
    subgraph "release_job"
        release_condition["only: tags matching<br/>release/[0-9]+.[0-9]+.[0-9]+"]
        release_script["python ./tools/release.py"]
    end
    
    code_format_stage --> cf_script
    docs_stage --> docs_script
    docs_script --> docs_artifacts
    
    build_stage --> build_cache
    build_cache --> build_script
    build_script --> build_artifacts
    
    release_stage --> release_condition
    release_condition --> release_script
```

**GitLab Cache Configuration:**

```yaml
cache:
  key: "$CI_PROJECT_ID-esp-idf-v542"
  paths:
    - ${ESP_IDF_SRC_DIR}
  policy: pull-push
  when: on_success
```

**Workflow Control:**

```yaml
workflow:
  auto_cancel:
    on_new_commit: conservative
```

This prevents redundant builds when new commits are pushed during an ongoing build.

**Release Job Trigger:**

```yaml
release_job:
  stage: release
  script:
    - python ./tools/release.py
  only:
    refs:
      - tags
    variables:
      - $CI_COMMIT_TAG =~ /^release\/[0-9]+\.[0-9]+\.[0-9]+$/
```

Sources: [.gitlab-ci.yml:1-85](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/.gitlab-ci.yml#L1-L85)

---

### Code Formatting Enforcement

Both CI systems enforce code formatting using multiple tools:

```mermaid
graph LR
    subgraph "Formatting Tools"
        uncrustify["uncrustify 0.72.0<br/>C/C++ formatting"]
        black["black<br/>Python formatting"]
        ruff["ruff 0.3.0<br/>Python linting"]
        codespell["codespell 2.2.6<br/>Spell checking"]
    end
    
    subgraph "Setup Process"
        uncrustify_setup["uncrustify_setup<br/>Build from source<br/>0.72.0 specific version"]
        pipx_install["pipx install uv"]
        uv_venv["uv venv"]
        uv_packages["uv pip install black ruff codespell"]
    end
    
    subgraph "Execution"
        codeformat["tools/codeformat.py -v -c -f"]
        git_diff["git diff --exit-code"]
    end
    
    uncrustify_setup --> uncrustify
    pipx_install --> uv_venv
    uv_venv --> uv_packages
    uv_packages --> black
    uv_packages --> ruff
    uv_packages --> codespell
    
    uncrustify --> codeformat
    black --> codeformat
    ruff --> codeformat
    codespell --> codeformat
    
    codeformat --> git_diff
```

**ci_code_formatting_setup Function:**

```bash
function ci_code_formatting_setup {
    uncrustify_setup
    sudo apt install pipx -y
    pipx install uv
    uv venv
    source .venv/bin/activate
    uv pip install black
    uv pip install micropython-typesheds
    uv pip install ruff==0.3.0
    uv pip install codespell==2.2.6 tomli==2.0.1
    uv pip install pre-commit==3.6.2
    uncrustify --version
    black --version
}
```

**Uncrustify Setup:**

The system requires a specific version (0.72.0) and builds it from source if not present:

```bash
function uncrustify_setup {
    if [ uncrustify --version | grep -q "Uncrustify-0.72.0_f" ]; then
        echo "uncrustify 0.72.0 is already installed."
        return 0
    fi

    wget https://github.com/uncrustify/uncrustify/archive/refs/tags/uncrustify-0.72.0.tar.gz
    tar -xvf uncrustify-0.72.0.tar.gz
    cd uncrustify-uncrustify-0.72.0
    # ... CMake configuration fixes
    mkdir build && cd build
    cmake -DCMAKE_BUILD_TYPE=Release ..
    make -j$(nproc)
    sudo make install
}
```

Sources: [tools/ci.sh:16-58](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/tools/ci.sh#L16-L58)

---

## Board Configuration and Firmware Assembly

### Board Configuration File Hierarchy

Each board defines its configuration through a three-file hierarchy:

```mermaid
graph TB
    subgraph "Board: M5STACK_CoreInk"
        mpconfigboard_cmake["mpconfigboard.cmake<br/>CMake configuration"]
        sdkconfig_board["sdkconfig.board<br/>ESP-IDF menuconfig"]
        mpconfigboard_h["mpconfigboard.h<br/>C preprocessor defines"]
    end
    
    subgraph "mpconfigboard.cmake Contents"
        board_id["BOARD_ID = 6"]
        lvgl_flag["MICROPY_PY_LVGL = 0"]
        sdkconfig_defaults["SDKCONFIG_DEFAULTS<br/>Layered composition"]
        tiny_flag_cmake["TINY_FLAG = 1"]
        frozen_manifest["MICROPY_FROZEN_MANIFEST"]
        lv_cflags["LV_CFLAGS (if LVGL enabled)"]
    end
    
    subgraph "Layered sdkconfig"
        base["sdkconfig.base<br/>Common settings"]
        version_specific["${{SDKCONFIG_IDF_VERSION_SPECIFIC}}<br/>ESP-IDF version"]
        flash["sdkconfig.flash_4mb<br/>Flash size"]
        ble["sdkconfig.ble<br/>Bluetooth"]
        freq["sdkconfig.240mhz<br/>CPU frequency"]
        iram["sdkconfig.disable_iram<br/>IRAM optimization"]
        freertos["sdkconfig.freertos<br/>FreeRTOS config"]
        board_specific["M5STACK_CoreInk/sdkconfig.board<br/>Board-specific"]
    end
    
    subgraph "mpconfigboard.h Contents"
        board_name["MICROPY_HW_BOARD_NAME<br/>M5STACK CoreInk"]
        mcu_name["MICROPY_HW_MCU_NAME<br/>ESP32-S3"]
        lvgl_include["#include mpconfiglvgl.h<br/>(if LVGL enabled)"]
    end
    
    mpconfigboard_cmake --> board_id
    mpconfigboard_cmake --> lvgl_flag
    mpconfigboard_cmake --> sdkconfig_defaults
    mpconfigboard_cmake --> tiny_flag_cmake
    mpconfigboard_cmake --> frozen_manifest
    mpconfigboard_cmake --> lv_cflags
    
    sdkconfig_defaults --> base
    sdkconfig_defaults --> version_specific
    sdkconfig_defaults --> flash
    sdkconfig_defaults --> ble
    sdkconfig_defaults --> freq
    sdkconfig_defaults --> iram
    sdkconfig_defaults --> freertos
    sdkconfig_defaults --> board_specific
    
    mpconfigboard_h --> board_name
    mpconfigboard_h --> mcu_name
    mpconfigboard_h --> lvgl_include
```

**mpconfigboard.cmake Example (M5STACK_CoreInk):**

```cmake
# BOARD_ID from M5Stack board registry
set(BOARD_ID 6)
set(MICROPY_PY_LVGL 0)

set(SDKCONFIG_DEFAULTS
    ./boards/sdkconfig.base
    ${SDKCONFIG_IDF_VERSION_SPECIFIC}
    ./boards/sdkconfig.flash_4mb
    ./boards/sdkconfig.ble
    ./boards/sdkconfig.240mhz
    ./boards/sdkconfig.disable_iram
    ./boards/sdkconfig.freertos
    ./boards/M5STACK_CoreInk/sdkconfig.board
)

set(TINY_FLAG 1)

if(NOT MICROPY_FROZEN_MANIFEST)
    set(MICROPY_FROZEN_MANIFEST ${CMAKE_SOURCE_DIR}/boards/manifest.py)
endif()
```

Sources: [m5stack/boards/M5STACK_CoreInk/mpconfigboard.cmake:1-40](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/boards/M5STACK_CoreInk/mpconfigboard.cmake#L1-L40)

---

### Layered sdkconfig Composition

The `SDKCONFIG_DEFAULTS` list creates a layered configuration system:

| Layer | Purpose | Example Settings |
|-------|---------|------------------|
| `sdkconfig.base` | Common ESP32 settings | Compiler flags, optimization level |
| `${SDKCONFIG_IDF_VERSION_SPECIFIC}` | ESP-IDF version compatibility | Version-specific patches |
| `sdkconfig.flash_4mb` / `sdkconfig.flash_8mb` | Flash memory size | Partition sizes, app size limits |
| `sdkconfig.spiram` / `sdkconfig.spiram_oct` | PSRAM configuration | PSRAM size, access mode |
| `sdkconfig.ble` | Bluetooth configuration | BLE stack, NimBLE options |
| `sdkconfig.usb` / `sdkconfig.usb_cdc` | USB support | USB OTG, CDC-ACM console |
| `sdkconfig.240mhz` | CPU frequency | 240MHz operation |
| `sdkconfig.disable_iram` | Memory optimization | Disable IRAM for larger code size |
| `sdkconfig.freertos` | FreeRTOS tuning | Task priorities, stack sizes |
| `sdkconfig.board` | Board-specific overrides | Flash mode, SSL config |

**Example: M5STACK_AtomS3R_CAM Configuration**

This board requires specific flash and camera settings:

```cmake
set(SDKCONFIG_DEFAULTS
    ./boards/sdkconfig.base
    ${SDKCONFIG_IDF_VERSION_SPECIFIC}
    ./boards/sdkconfig.240mhz
    ./boards/sdkconfig.disable_iram
    ./boards/sdkconfig.ble
    ./boards/sdkconfig.usb
    ./boards/sdkconfig.usb_cdc
    ./boards/sdkconfig.flash_8mb
    ./boards/sdkconfig.spiram
    ./boards/sdkconfig.spiram_oct
    ./boards/sdkconfig.freertos
    ./boards/M5STACK_AtomS3R_CAM/sdkconfig.board
)
```

The board-specific `sdkconfig.board` adds camera support:

```
CONFIG_FLASHMODE_DIO=y
CONFIG_ESPTOOLPY_FLASHMODE_DIO=y
CONFIG_ESPTOOLPY_FLASHFREQ_80M=y
CONFIG_SPIRAM_MEMTEST=y

# M5STACK UiFlow USB description
CONFIG_TINYUSB_DESC_CDC_STRING="M5Stack AtomS3R-CAM(UiFlow2)"

# for component/esp32-camera
CONFIG_SCCB_SOFTWARE_SUPPORT=y
```

Sources: [m5stack/boards/M5STACK_AtomS3R_CAM/mpconfigboard.cmake:1-43](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/boards/M5STACK_AtomS3R_CAM/mpconfigboard.cmake#L1-L43), [m5stack/boards/M5STACK_AtomS3R_CAM/sdkconfig.board:1-24](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/boards/M5STACK_AtomS3R_CAM/sdkconfig.board#L1-L24)

---

### Board-Specific Startup Integration

Boards integrate with the runtime startup system through board type mappings:

```mermaid
graph LR
    subgraph "Build Time"
        BOARD_TYPE_build["BOARD_TYPE=coreink<br/>From Makefile"]
        fs_system_dir["fs/system/coreink/<br/>Board-specific files"]
        startup_manifest["modules/startup/manifest_coreink.py"]
    end
    
    subgraph "Startup Module"
        startup_init["startup/__init__.py"]
        board_id["M5.getBoard()<br/>Returns BOARD_ID"]
        coreink_startup["startup/coreink.py<br/>CoreInk_Startup class"]
    end
    
    subgraph "Runtime"
        _boot["_boot.py"]
        board_init["board_init()"]
        startup_call["startup(boot_opt, timeout)"]
        coreink_instance["CoreInk_Startup().startup()"]
    end
    
    BOARD_TYPE_build -.packages.-> fs_system_dir
    startup_manifest -.frozen into.-> fs_system_dir
    
    fs_system_dir -.mounted at.-> startup_init
    
    _boot --> board_init
    board_init --> startup_call
    startup_call --> board_id
    board_id -.matches BOARD_ID 6.-> coreink_startup
    coreink_startup --> coreink_instance
```

**Startup Manifest Files:**

Each board type has a corresponding manifest file that packages its startup module:

```python
# modules/startup/manifest_coreink.py
package(
    "startup",
    (
        "__init__.py",
        "coreink.py",
    ),
    base_path="..",
    opt=3,
)
```

**Board ID Mapping:**

The `BOARD_ID` set in `mpconfigboard.cmake` matches the runtime `M5.getBoard()` return value:

```python
# startup/__init__.py
board_id = M5.getBoard()
if board_id == M5.BOARD.M5StackCoreInk:
    from .coreink import CoreInk_Startup
    coreink = CoreInk_Startup()
    coreink.startup(ssid, pswd, timeout)
```

Sources: [m5stack/modules/startup/__init__.py:68-194](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/modules/startup/__init__.py#L68-L194), [m5stack/modules/startup/manifest_coreink.py:1-14](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/modules/startup/manifest_coreink.py#L1-L14)

---

### Final Firmware Assembly Process

The `makeimg.py` tool assembles all components into the final flashable firmware:

```mermaid
graph TB
    subgraph "Input Files"
        sdkconfig_in["sdkconfig<br/>Parse flash size, partition layout"]
        bootloader_in["bootloader.bin<br/>First-stage bootloader"]
        partition_in["partition-table.bin<br/>Partition map"]
        nvs_in["nvs.bin<br/>0x6000 bytes at 0x9000"]
        firmware_in["micropython.bin<br/>Application firmware"]
        fs_system_in["fs-system.bin<br/>System partition"]
        fs_user_in["fs-user.bin<br/>User partition (optional)"]
    end
    
    subgraph "makeimg.py Processing"
        parse_partitions["Parse partition table<br/>Extract offsets and sizes"]
        validate["Validate sizes<br/>Check against flash capacity"]
        assemble_bin["Assemble .bin<br/>Write components at offsets"]
        generate_uf2["Generate .uf2<br/>Convert to UF2 blocks"]
    end
    
    subgraph "Output Files"
        final_bin_out["uiflow-$(GIT_VERSION).bin<br/>Complete firmware image"]
        final_uf2_out["uiflow-Sx-$(GIT_VERSION).uf2<br/>USB MSC bootloader format"]
    end
    
    sdkconfig_in --> parse_partitions
    partition_in --> parse_partitions
    
    parse_partitions --> validate
    
    bootloader_in --> assemble_bin
    partition_in --> assemble_bin
    nvs_in --> assemble_bin
    firmware_in --> assemble_bin
    fs_system_in --> assemble_bin
    fs_user_in -.optional.-> assemble_bin
    
    validate --> assemble_bin
    assemble_bin --> final_bin_out
    assemble_bin --> generate_uf2
    generate_uf2 --> final_uf2_out
```

**Partition Layout Example:**

For a typical M5Stack board with 8MB flash:

| Partition | Offset | Size | Source |
|-----------|--------|------|--------|
| bootloader | 0x1000 | ~28KB | `bootloader.bin` |
| partition_table | 0x8000 | 3KB | `partition-table.bin` |
| nvs | 0x9000 | 24KB | `nvs.bin` |
| phy_init | 0xF000 | 4KB | (auto-generated) |
| factory | 0x10000 | ~3MB | `micropython.bin` |
| vfs | varies | ~3MB | `fs-system.bin` |
| user | varies | ~2MB | `fs-user.bin` |

**UF2 Format:**

The UF2 (USB Flashing Format) enables drag-and-drop firmware updates on boards with USB MSC bootloader support. Each UF2 block contains:

- 512-byte block size
- Target flash address
- Payload data (476 bytes)
- Family ID (ESP32-S3: 0xc47e5767)
- CRC32 checksum

Sources: [m5stack/Makefile:156-169](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/Makefile#L156-L169)

---

## Build System Variables Reference

### Makefile Variables

| Variable | Default | Purpose | Example |
|----------|---------|---------|---------|
| `BOARD` | `M5STACK_AtomS3` | Target board name | `M5STACK_CoreInk` |
| `BOARD_TYPE` | (auto-detected) | Board type for filesystem selection | `coreink` |
| `TINY_FLAG` | (auto-detected) | Memory-constrained board indicator | `0` or `1` |
| `BUILD` | `build-$(BOARD)` | Build output directory | `build-M5STACK_CoreInk` |
| `PORT` | `/dev/ttyUSB0` | Serial port for flashing | `/dev/ttyACM0` |
| `BAUD` | `1500000` | Flash baud rate | `921600` |
| `CHIP` | `auto` | ESP32 chip type | `esp32`, `esp32s3`, `esp32c3` |
| `LVGL` | (undefined) | Enable LVGL build | `1` |
| `GIT_VERSION` | (auto-detected) | Git commit hash | `a1b2c3d` |
| `PYTHON` | `python3` | Python interpreter | `python3.11` |

### CMake Variables

| Variable | Set By | Purpose |
|----------|--------|---------|
| `MICROPY_BOARD` | Makefile | Board name for CMake | 
| `BOARD_TYPE` | Makefile | Board type for filesystem |
| `BUILD_WITH_LVGL` | Makefile | LVGL enable flag |
| `USER_C_MODULES` | Makefile | Custom C modules path |
| `BOARD_ID` | mpconfigboard.cmake | M5Stack board registry ID |
| `MICROPY_PY_LVGL` | mpconfigboard.cmake | LVGL Python binding |
| `TINY_FLAG` | mpconfigboard.cmake | Tiny board flag |

Sources: [m5stack/Makefile:11-152](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/m5stack/Makefile#L11-L152)

---

## CI/CD Environment Variables

### GitHub Actions

| Variable | Purpose | Example |
|----------|---------|---------|
| `${{ runner.os }}` | Cache key OS component | `Linux` |
| `${{ matrix.board }}` | Current board in matrix | `M5STACK_CoreS3` |
| `${{ github.workspace }}` | Workspace root | `/home/runner/work/uiflow-micropython` |
| `${{ github.ref }}` | Git reference | `refs/tags/2.3.6` |
| `IDF_VERSION` | ESP-IDF version | `v5.4.2` |

### GitLab CI

| Variable | Purpose | Example |
|----------|---------|---------|
| `$CI_PROJECT_DIR` | Project directory | `/builds/m5stack/uiflow-micropython` |
| `$CI_PROJECT_ID` | Project ID for cache key | `12345` |
| `$CI_COMMIT_TAG` | Git tag | `release/2.3.6` |
| `$ESP_IDF_SRC_DIR` | ESP-IDF source path | `/builds/m5stack/uiflow-micropython/esp-idf` |

Sources: [.github/workflows/nightly-build.yml:1-149](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/.github/workflows/nightly-build.yml#L1-L149), [.gitlab-ci.yml:1-85](https://github.com/m5stack/uiflow-micropython/blob/7af4551a/.gitlab-ci.yml#L1-L85)