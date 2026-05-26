# Setting Up Your RDK Build

This guide provides detailed instructions to integrate the RDK Broadband Apps Toolkit into your RDK-B build.

## Prerequisites
- An existing RDK-B Yocto project
- Familiarity with BitBake, Yocto layer management, and the `repo` tool
- RDK-B Ready Hardware
    - NOTE: The `Banana Pi R4` is used as the reference hardware in this wiki.


## 1. Add `meta-rdk-broadband-apps` to your `repo` Manifest

!!! tip "Always Use Release Tags"
    It is **strongly recommended** to use release-tagged versions of this layer rather than tracking `main` directly. This ensures build reproducibility and stability. Check the [releases page](https://github.com/rdkcentral/meta-rdk-broadband-apps/releases) for available versions.

Add the following line to your RDK-B project manifest:
```bash
<project remote="rdkcentral" name="meta-rdk-broadband-apps" path="meta-rdk-broadband-apps" revision="<tag>"/>
```

## 2. Init Repos
```bash
repo init -u <your usual manifest repo> [-m <manifest file>]
repo sync
```

## 3. Sync DAC / LCM Repos

!!! warning "TO DO"
    Include specific release versions of DAC or LCM in the build. Don't just pull latest code. We need stable releases.

=== "DAC"

    !!! danger "DSM Bug Fix" 
        Before building with DAC, you must apply this commit to DSM: 
        [https://github.com/rdkcentral/DSM/commit/73c6a952786c8a7660b44389f96612e9a912456f](https://github.com/rdkcentral/DSM/commit/73c6a952786c8a7660b44389f96612e9a912456f)

    DAC is available in all RDK-B projects by default as part of the root `meta-rdk` meta-layer, so you don't need to do anything else to include it in your project.

=== "LCM"

    ```bash
    ## Extend the main manifest file with the LCM sub-manifest
    mkdir -p .repo/local_manifests
    cp manifests/rdkbb-apps-lcm.xml .repo/local_manifests/
    repo sync
    ```

## 4. Setup `local.conf`

Set the following variable in your `conf/local.conf`:

=== "DAC"

    ```bash
    RDK_BB_APPS_TOOLKIT_CRUNTIME = "DAC"
    ```

=== "LCM"

    ```bash
    RDK_BB_APPS_TOOLKIT_CRUNTIME = "LCM"
    ```


## 5. Set up the Build Environment

The following instruction is for a Banana Pi 4 Reference Board.
```bash
MACHINE=bananapi4-rdk-broadband source meta-cmf-bananapi/setup-environment-refboard-rdkb
```

## 6. Setup `bblayers.conf`

=== "DAC"

    ```bash
    echo 'BBLAYERS += "${RDKROOT}/meta-rdk-broadband-apps"' >> conf/bblayers.conf
    ```

=== "LCM"

    ```bash
    echo 'BBLAYERS += "${RDKROOT}/meta-lcm"' >> conf/bblayers.conf
    echo 'BBLAYERS += "${RDKROOT}/meta-amx"' >> conf/bblayers.conf
    echo 'BBLAYERS += "${RDKROOT}/meta-rdk-broadband-apps"' >> conf/bblayers.conf
    ```

## 7. Build the RDK-B image
```bash
bitbake <your-image>
```

## 8. Verify the Layer Integration

Run the following command and look for `rdkbbapps` in the output. If the layer has been properly added to your build, this command should show the layer path and priority.

```bash
bitbake-layers show-layers
```

## 9. Verify the Container Runtime Configuration

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