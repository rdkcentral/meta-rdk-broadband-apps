# Getting Started

This guide provides detailed instructions for building and configuring RDK Broadband devices with the Broadband Apps Framework for MVP 2025.

## Overview

This document is targeted at developers and architects wishing to understand and/or build the reference system for RDK Broadband Apps in its MVP 2025 version.

## Prerequisites

- A working Yocto/OpenEmbedded build environment
- An existing RDK project setup with repo tool
- Familiarity with BitBake and Yocto layer management
- **Reference Hardware**: Banana Pi BPI-R4 or Raspberry Pi 4

## Supported Platforms

| Device | Versions | Notes |
|--------|----------|-------|
| Raspberry Pi 4 (32bit/64bit) | 2025q1, 2025q2 | Confirmed Building - Official Support to be deprecated |
| Banana Pi BPI-R4 | 2025q2 | Intermittent Build Issues not due to Toolkit |

## Choosing Your Container Runtime

This layer supports two container runtime options:

- **DAC**: Dobby Application Container utilities (Dobby and DSM) from the RDK Central `meta-rdk` layer
- **LCM**: Lifecycle Management from the prpl Foundation's prplLCM project

The container runtime is configured using the `RDK_BB_APPS_TOOLKIT_CRUNTIME` variable in your build configuration.

!!! tip "Use Release Tags"
    It is **strongly recommended** to use release-tagged versions of this layer rather than tracking `main` directly. This ensures build reproducibility and stability. Check the [releases page](https://github.com/rdkcentral/meta-rdk-broadband-apps/releases) for available versions.

## Building with DAC (Dobby)

### Prerequisites for DAC

Before building with DAC, you must apply this commit to DSM:
```
https://github.com/rdkcentral/DSM/commit/73c6a952786c8a7660b44389f96612e9a912456f
```

### DAC Build Instructions

=== "Raspberry Pi 4"

    ```bash
    # 1) Grab the manifest for Raspberry Pi
    repo init -u https://code.rdkcentral.com/r/rdkcmf/manifests \
              -m rdkb-extsrc.xml \
              -b rdkb-2025q2-kirkstone
    
    # 2) Checkout the Broadband Apps Toolkit
    # Note: For DAC (unlike LCM) no manifest extension is required
    git clone git@github.com:rdkcentral/meta-rdk-broadband-apps.git
    # Optionally specify branch: -b <branch>
    
    # 3) Sync sources
    repo sync
    
    # 4) Set the build config
    # For 32-bit:
    MACHINE=raspberrypi4-rdk-broadband source meta-cmf-raspberrypi/setup-environment
    
    # For 64-bit:
    # MACHINE=raspberrypi4-64-rdk-broadband source meta-cmf-raspberrypi/setup-environment
    
    # 5) Add meta-rdk-broadband-apps to the build
    # Edit conf/bblayers.conf and add:
    echo 'BBLAYERS =+ "${RDKROOT}/meta-rdk-broadband-apps"' >> conf/bblayers.conf
    
    # 6) DAC is the default runtime (no configuration needed)
    # RDK_BB_APPS_TOOLKIT_CRUNTIME defaults to "DAC"
    
    # 7) Build
    bitbake rdk-generic-broadband-image
    ```

=== "Banana Pi BPI-R4"

    ```bash
    # 1) Grab the manifest for Banana Pi
    repo init -u https://code.rdkcentral.com/r/rdkcmf/manifests \
              -m rdkb-bpi-extsrc.xml \
              -b rdkb-2025q2-kirkstone
    
    # 2) Checkout the Broadband Apps Toolkit
    git clone git@github.com:rdkcentral/meta-rdk-broadband-apps.git
    
    # 3) Sync sources
    repo sync
    
    # 4) Set the build config
    MACHINE=bananapi4-rdk-broadband source meta-cmf-bananapi/setup-environment-refboard-rdkb
    
    # 5) Add meta-rdk-broadband-apps to the build
    echo 'BBLAYERS =+ "${RDKROOT}/meta-rdk-broadband-apps"' >> conf/bblayers.conf
    
    # 6) Build
    bitbake rdk-generic-broadband-image
    ```

## Building with LCM (Lifecycle Management)

### LCM Build Instructions

=== "Raspberry Pi 4"

    ```bash
    # 1) Grab the manifest for Raspberry Pi
    repo init -u https://code.rdkcentral.com/r/rdkcmf/manifests \
              -m rdkb-extsrc.xml \
              -b rdkb-2025q2-kirkstone
    
    # 2) Checkout the Broadband Apps Toolkit and Install Manifest Extension for LCM
    git clone --depth 1 git@github.com:rdkcentral/meta-rdk-broadband-apps.git
    # Optionally specify branch: -b <branch>
    
    # 3) Extend the main manifest with the toolkit manifest
    mkdir -p ./.repo/local_manifests/
    cp ./meta-rdk-broadband-apps/manifests/rdkbb-apps-lcm.xml \
       ./.repo/local_manifests/local_manifest.xml
    
    # 4) Sync sources
    repo sync -j`nproc` --no-clone-bundle
    # This adds meta-amx and meta-lcm layers
    
    # 5) Set the build config
    # For 32-bit:
    MACHINE=raspberrypi4-rdk-broadband source meta-cmf-raspberrypi/setup-environment
    
    # For 64-bit:
    # MACHINE=raspberrypi4-64-rdk-broadband source meta-cmf-raspberrypi/setup-environment
    
    # 6) Add the LCM layers to the build
    # Apply bblayers.patch if available, or manually add:
    echo 'BBLAYERS =+ "${RDKROOT}/meta-amx"' >> conf/bblayers.conf
    echo 'BBLAYERS =+ "${RDKROOT}/meta-lcm"' >> conf/bblayers.conf
    echo 'BBLAYERS =+ "${RDKROOT}/meta-rdk-broadband-apps"' >> conf/bblayers.conf
    
    # 7) Set RUNTIME type to LCM
    # Option 1: Edit meta-rdk-broadband-apps/conf/layer.conf and set:
    # RDK_BB_APPS_TOOLKIT_CRUNTIME = "LCM"
    
    # Option 2: Export in environment before building:
    export RDK_BB_APPS_TOOLKIT_CRUNTIME=LCM
    
    # 8) Build
    bitbake rdk-generic-broadband-image
    ```

=== "Banana Pi BPI-R4"

    ```bash
    # 1) BPI-R4 reference 2025q2 manifest
    repo init -u https://code.rdkcentral.com/r/rdkcmf/manifests \
              -b rdkb-2025q2-kirkstone \
              -m rdkb-bpi-extsrc.xml
    
    # 2) Add meta-rdk-broadband-apps to the tree
    git clone git@github.com:rdkcentral/meta-rdk-broadband-apps.git
    
    # 3) Add LCM and AMX layers to the tree
    mkdir -p ./.repo/local_manifests/
    cp ./meta-rdk-broadband-apps/manifests/rdkbb-apps-lcm.xml \
       ./.repo/local_manifests/local_manifest.xml
    
    # 4) Sync/download the sources
    repo sync -j`nproc` --no-clone-bundle
    
    # 5) (Optional) Bootloader files required for SD card build
    # See RDK-B BPI-R4 generic build instructions for more info
    mkdir -p downloads
    cp /path/to/your/copy/of/bpi-r4_sdmmc_* downloads/
    
    # 6) Switch from DAC (default) to LCM
    sed -i 's/^RDK_BB_APPS_TOOLKIT_CRUNTIME ?= "DAC"/#RDK_BB_APPS_TOOLKIT_CRUNTIME ?= "DAC"/' \
        meta-rdk-broadband-apps/conf/layer.conf
    sed -i 's/^# *RDK_BB_APPS_TOOLKIT_CRUNTIME ?= "LCM"/RDK_BB_APPS_TOOLKIT_CRUNTIME ?= "LCM"/' \
        meta-rdk-broadband-apps/conf/layer.conf
    
    # 7) Set up the MACHINE - choose either SD card or NAND:
    
    # For SD card:
    MACHINE=bananapi4-rdk-broadband source meta-cmf-bananapi/setup-environment-refboard-rdkb
    
    # For NAND:
    # MACHINE=bananapi4-rdk-broadband BPI_IMG_TYPE=nand source meta-cmf-bananapi/setup-environment-refboard-rdkb
    
    # 8) Add extra layers for bitbake
    echo 'BBLAYERS =+ "${RDKROOT}/meta-lcm"' >> conf/bblayers.conf
    echo 'BBLAYERS =+ "${RDKROOT}/meta-rdk-broadband-apps"' >> conf/bblayers.conf
    
    # 9) Build the image
    bitbake rdk-generic-broadband-image
    ```

## Verifying Layer Integration

You can verify that the layer has been properly added to your build:

### Check Layer Configuration

```bash
bitbake-layers show-layers
```

Look for `rdkbbapps` in the output. It should show the layer path and priority.

### Verify Container Runtime Configuration

Check which container runtime is configured:

```bash
bitbake -e | grep "^RDK_BB_APPS_TOOLKIT_CRUNTIME="
```

This should output either:
```
RDK_BB_APPS_TOOLKIT_CRUNTIME="DAC"
```
or
```
RDK_BB_APPS_TOOLKIT_CRUNTIME="LCM"
```

## Next Steps

- [System Architecture](architecture.md) - Understanding the reference system architecture
- [Acceptance Testing](acceptance-testing.md) - Testing and validation procedures
- [Data Models](data-models.md) - TR-369/USP data models for lifecycle management
