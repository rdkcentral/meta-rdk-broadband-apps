# Installing the Toolkit

This guide provides detailed instructions to integrate the RDK Broadband Apps Toolkit into your RDK-B build.

## Prerequisites
- An existing RDK-B Yocto project
- Familiarity with BitBake, Yocto layer management, and the `repo` tool
- RDK-B Ready Hardware
    - NOTE: The recommended reference hardware is the `Banana Pi R4`


## 1. Set Up Your `repo` Manifest

### 1. Add `meta-rdk-broadband-apps` to your `repo` Manifest

!!! tip "Use Release Tags"
    It is **strongly recommended** to use release-tagged versions of this layer rather than tracking `main` directly. This ensures build reproducibility and stability. Check the [releases page](https://github.com/rdkcentral/meta-rdk-broadband-apps/releases) for available versions.

Add the following line to your RDK-B project manifest
```bash
<project remote="github" name="meta-rdk-broadband-apps" path="meta-rdk-broadband-apps" revision="<tag>"/>
```

### 2 Adding DAC/LCM Components to the `repo` Manifest

!!! tip "The following files are used in this guide:"
    - `conf/layer.conf` – marks this repo as a BitBake layer and recommends `meta-amx` and `meta-lcm`.
    - `manifests/rdkbb-apps-lcm.xml` – add-on submanifest to fetch prpl LCM dependencies.
    - `conf/bblayers.conf.sample` - a reference list of all necessary meta-layers to be added to your `bblayers.conf` file. 

<details>
<summary>Instructions for DAC</summary>

#### 1. Initialize and sync sources as you normally do for your Yocto setup
```bash
repo init -u <your usual manifest repo> [-m <their default manifest>]
repo sync
```

#### 2. Add DAC Components

Nothing to do here. DAC is available in all RDK-B projects by default as part of the root `meta-rdk` meta-layer.

#### 3. Enter the Yocto build environment
```bash
source poky/oe-init-build-env
```

#### 4. Seed BBLAYERS from the provided sample

!!! tip "Alternatively, you can manually copy the required meta-layers from `bblayers.conf.sample` into your existing `bblayers.conf`."

```bash
cp ../conf/bblayers.conf.sample conf/bblayers.conf
```

#### 5. (Optional) Pick a reference MACHINE for repeatable builds
```bash
echo 'MACHINE ?= "raspberrypi4-64"' >> conf/local.conf
```
</details>


<details
><summary>Instructions for LCM</summary>

#### 1. Initialize and sync sources as you normally do for your Yocto setup
```bash
repo init -u <your usual manifest repo> [-m <their default manifest>]
repo sync
```

#### 2. Add LCM Components
```bash
mkdir -p .repo/local_manifests
cp manifests/rdkbb-apps-lcm.xml .repo/local_manifests/
repo sync
```

#### 3. Enter the Yocto build environment
```bash
source poky/oe-init-build-env
```

#### 4. Seed BBLAYERS from the provided sample

!!! tip "Alternatively, you can manually copy the required meta-layers from `bblayers.conf.sample` into your existing `bblayers.conf`."

```bash
cp ../conf/bblayers.conf.sample conf/bblayers.conf
```

#### 5. (Optional) Pick a reference MACHINE for repeatable builds
```bash
echo 'MACHINE ?= "raspberrypi4-64"' >> conf/local.conf
```

#### 6. Build
```bash
bitbake <your-image>
```
</details>

## 2. Building The Image

This layer supports two containerisation solutions:
- **DAC**: Dobby Application Container utilities (Dobby and DSM) from the RDK Central `meta-rdk` layer
- **LCM**: Lifecycle Management from the prpl Foundation's prplLCM project

The container runtime is configured using the `RDK_BB_APPS_TOOLKIT_CRUNTIME` variable in your build configuration.

### 1. To Build DAC

#### 1. Prerequisites for DAC

!!! danger "DSM Bug Fix" 
    Before building with DAC, you must apply this commit to DSM: 
    https://github.com/rdkcentral/DSM/commit/73c6a952786c8a7660b44389f96612e9a912456f

#### 2. Set the following variable in your `conf/layers.conf`
```bash
RDK_BB_APPS_TOOLKIT_CRUNTIME = "DAC"
```

### 2. To Build LCM

#### 1. Set the following variable in your `conf/layers.conf`
```bash
RDK_BB_APPS_TOOLKIT_CRUNTIME = "LCM"
```


## 3. Verifying Layer Integration

Run the following command and look for `rdkbbapps` in the output. If the layer has been properly added to your build, this command should show the layer path and priority.

```bash
bitbake-layers show-layers
```

## 4. Verify Containerisation Technology Configuration

Run the following command to ensure you have correctly set your Containerisation Technology (either DAC or prplLCM):

```bash
bitbake -e | grep "^RDK_BB_APPS_TOOLKIT_CRUNTIME="
```

This should output either:
```bash
RDK_BB_APPS_TOOLKIT_CRUNTIME="DAC"
```
or
```bash
RDK_BB_APPS_TOOLKIT_CRUNTIME="LCM"
```