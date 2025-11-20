# Getting Started

This guide will help you integrate the `meta-rdk-broadband-apps` layer into your RDK project and build containerized applications using either DAC (Dobby and DSM utilities from [meta-rdk](https://github.com/rdkcentral/meta-rdk)) or LCM (Lifecycle Management from [prplLCM](https://gitlab.com/prpl-foundation/prplrdkb/metalayers)).

## Prerequisites

- A working Yocto/OpenEmbedded build environment
- An existing RDK project setup with repo tool
- Familiarity with BitBake and Yocto layer management
- **Reference Hardware**: Banana Pi BPI-R4 (examples in this guide use this platform)

## Choosing Your Container Runtime

This layer supports two container runtime options:

- **DAC**: Dobby Application Container utilities (Dobby and DSM) from the RDK Central `meta-rdk` layer
- **LCM**: Lifecycle Management from the prpl Foundation's prplLCM project

The container runtime is configured using the `RDK_BB_APPS_TOOLKIT_CRUNTIME` variable in your build configuration.

!!! tip "Use Release Tags"
    It is **strongly recommended** to use release-tagged versions of this layer rather than tracking `main` directly. This ensures build reproducibility and stability. Check the [releases page](https://github.com/rdkcentral/meta-rdk-broadband-apps/releases) for available versions.

## Building with LCM (prplLCM)

### How to consume in a product build

```bash
# 1) Initialize and sync sources as you normally do for your Yocto setup
repo init -u <your usual manifest repo> [-m <their default manifest>]
repo sync

# 2) Install this repo's sub-manifest (adds prpl layers)
mkdir -p .repo/local_manifests
cp manifests/rdkbb-apps-lcm.xml .repo/local_manifests/
repo sync

# 3) Enter the Yocto build environment
source poky/oe-init-build-env

# 4) Seed BBLAYERS from the provided sample
cp ../meta-rdk-broadband-apps/conf/bblayers.conf.sample conf/bblayers.conf

# 5) Configure for LCM runtime
echo 'RDK_BB_APPS_TOOLKIT_CRUNTIME = "LCM"' >> conf/local.conf

# 6) (Optional) Pick a reference MACHINE for repeatable builds
echo 'MACHINE = "bananapi-r4"' >> conf/local.conf

# 7) Build
bitbake <your-image>
```

## Building with DAC (Dobby)

### How to consume in a product build

```bash
# 1) Initialize and sync sources as you normally do for your Yocto setup
repo init -u <your usual manifest repo> [-m <their default manifest>]
repo sync

# 2) Add this layer to your build (ensure meta-rdk is also present for DAC utilities)

# 3) Enter the Yocto build environment
source poky/oe-init-build-env

# 4) Add the layer to BBLAYERS
bitbake-layers add-layer ../meta-rdk-broadband-apps

# 5) Configure for DAC runtime (this is the default)
echo 'RDK_BB_APPS_TOOLKIT_CRUNTIME = "DAC"' >> conf/local.conf

# 6) (Optional) Pick a reference MACHINE for repeatable builds
echo 'MACHINE = "bananapi-r4"' >> conf/local.conf

# 7) Build
bitbake <your-image>
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

- [Device.SoftwareModules Data Model](device-softwaremodules.md) - Lifecycle management via TR-369/USP
- [TR-369/USP Data Models](tr369-usp-data-models.md) - Supported USP data models
- [TR-69/CWMP Data Models](tr69-cwmp-data-models.md) - Backwards compatible CWMP data models
