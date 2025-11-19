# Getting Started

This guide will help you integrate the `meta-rdk-broadband-apps` layer into your RDK project and build containerized applications using either DAC (Dobby Application Container) or LCM (Lightweight Container Manager).

## Prerequisites

- A working Yocto/OpenEmbedded build environment
- An existing RDK project setup with repo tool
- Familiarity with BitBake and Yocto layer management
- **Reference Hardware**: Banana Pi BPI-R4 (examples in this guide use this platform)

## Adding the Layer to Your RDK Project

### Step 1: Add the Layer to Your Manifest

!!! tip "Use Release Tags"
    It is **strongly recommended** to use release-tagged versions of this layer rather than tracking `main` directly. This ensures build reproducibility and stability. Check the [releases page](https://github.com/rdkcentral/meta-rdk-broadband-apps/releases) for available versions.

Add `meta-rdk-broadband-apps` to your repo manifest. If using a tagged release:

```xml
<project name="rdkcentral/meta-rdk-broadband-apps" 
         path="meta-rdk-broadband-apps" 
         revision="refs/tags/v1.0.0" />
```

Or for development purposes (not recommended for production):

```xml
<project name="rdkcentral/meta-rdk-broadband-apps" 
         path="meta-rdk-broadband-apps" 
         revision="main" />
```

### Step 2: Sync Your Sources

```bash
repo sync
```

### Step 3: Add the Layer to Your Build Configuration

After sourcing your build environment:

```bash
source poky/oe-init-build-env
```

Edit your `conf/bblayers.conf` to include the layer. You can use the sample as a reference:

```bash
# Option 1: Copy the sample configuration
cp ../meta-rdk-broadband-apps/conf/bblayers.conf.sample conf/bblayers.conf

# Option 2: Manually add to existing bblayers.conf
bitbake-layers add-layer ../meta-rdk-broadband-apps
```

Your `BBLAYERS` should include at minimum:

```
BBLAYERS ?= " \
  ${TOPDIR}/../poky/meta \
  ${TOPDIR}/../poky/meta-poky \
  ${TOPDIR}/../meta-openembedded/meta-oe \
  ${TOPDIR}/../meta-openembedded/meta-networking \
  ${TOPDIR}/../meta-openembedded/meta-python \
  ${TOPDIR}/../meta-rdk-broadband-apps \
"
```

## Building with DAC (Dobby Application Container)

DAC (Dobby) is the default container runtime for this layer.

### Step 1: Configure for DAC

DAC is the default runtime. Ensure your `conf/layer.conf` or `conf/local.conf` has:

```bash
RDK_BB_APPS_TOOLKIT_CRUNTIME = "DAC"
```

### Step 2: Set Target Machine (Optional)

For Banana Pi BPI-R4 as the reference hardware:

```bash
echo 'MACHINE = "bananapi-r4"' >> conf/local.conf
```

### Step 3: Build Your Image

Build your target image which will include DAC support:

```bash
bitbake rdk-generic-broadband-image
```

Or include DAC in your custom image by adding the appropriate package groups.

### Step 4: Verify DAC Installation

After flashing your device with the built image, verify DAC is installed:

```bash
# Check if DobbyDaemon is running
ps aux | grep DobbyDaemon

# Check Dobby version
DobbyTool --version

# List available containers
DobbyTool list
```

## Building with LCM (Lightweight Container Manager)

LCM is the prpl Foundation's lightweight container manager, an alternative to DAC.

### Step 1: Add LCM Dependencies

LCM requires additional meta layers. Add the LCM manifest snippet:

```bash
mkdir -p .repo/local_manifests
cp meta-rdk-broadband-apps/manifests/rdkbb-apps-lcm.xml .repo/local_manifests/
repo sync
```

This will fetch:
- `meta-amx` - Ambiorix framework
- `meta-lcm` - LCM implementation

### Step 2: Add LCM Layers to Build Configuration

Update your `conf/bblayers.conf` to include the LCM layers:

```
BBLAYERS ?= " \
  ${TOPDIR}/../poky/meta \
  ${TOPDIR}/../poky/meta-poky \
  ${TOPDIR}/../meta-openembedded/meta-oe \
  ${TOPDIR}/../meta-openembedded/meta-networking \
  ${TOPDIR}/../meta-openembedded/meta-python \
  ${TOPDIR}/../meta-rdk-broadband-apps \
  ${TOPDIR}/../meta-amx \
  ${TOPDIR}/../meta-lcm \
"
```

### Step 3: Configure for LCM

Set the container runtime to LCM in your `conf/local.conf`:

```bash
RDK_BB_APPS_TOOLKIT_CRUNTIME = "LCM"
```

Optionally, set the target machine for Banana Pi BPI-R4:

```bash
echo 'MACHINE = "bananapi-r4"' >> conf/local.conf
```

### Step 4: Build Your Image

Build your target image with LCM support:

```bash
bitbake rdk-generic-broadband-image
```

### Step 5: Verify LCM Installation

After flashing your device with the built image, verify LCM is installed:

```bash
# Check if LCM daemon is running
ps aux | grep lcm

# Check LCM version (if available)
lcm --version

# List available containers (command may vary based on LCM version)
lcm list
```

## Verifying Layer Integration

You can verify that the layer has been properly added to your build:

### Check Layer Configuration

```bash
bitbake-layers show-layers
```

Look for `rdkbbapps` in the output. It should show the layer path and priority.

### Check Layer Dependencies

```bash
bitbake-layers show-layers | grep -E "rdkbbapps|meta-amx|meta-lcm"
```

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

### Build a Test Image

To verify everything is working correctly, build the reference image:

```bash
bitbake rdk-generic-broadband-image
```

If the build completes successfully, the layer is properly integrated.

## Troubleshooting

### Layer Not Found

If BitBake cannot find the layer, ensure:
- The layer path in `bblayers.conf` is correct
- You've run `repo sync` after adding the manifest
- The `layer.conf` file exists in the layer directory

### Missing Dependencies

If you get errors about missing layers (like `meta-amx` or `meta-lcm`):
- For LCM: Ensure you've added the `rdkbb-apps-lcm.xml` manifest and run `repo sync`
- Check that all required layers are in your `BBLAYERS` configuration

### Build Failures

- Check the BitBake error logs in `tmp/work/`
- Verify your Yocto version compatibility (see `LAYERSERIES_COMPAT_rdkbbapps` in `layer.conf`)
- Ensure all recommended layers are present

## Next Steps

- [How-to: Manage Containerized Apps](howto-manage-apps.md) - Learn to deploy and manage applications
- [TR-369/USP Data Models](tr369-usp-data-models.md) - Supported USP data models
- [TR-69/CWMP Data Models](tr69-cwmp-data-models.md) - Backwards compatible CWMP data models
