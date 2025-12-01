# Building Apps

This guide provides instructions for building containerized applications for the RDK Broadband Apps Framework.

!!! note "Documentation In Progress"
    This page is currently under development. Detailed tutorials and examples will be added in future updates.

**Reference Hardware**: All examples in this guide use the **Banana Pi BPI-R4** as the target device.

## Overview

The RDK Broadband Apps Framework supports two types of containerized applications:

- **OCI Bundles** - For DAC (Dobby) runtime
- **OCI Images** - For LCM (Lifecycle Management) runtime

## Prerequisites

Before building apps, ensure you have:

- Completed the [Installing the Toolkit](installing-toolkit.md) guide
- A built RDK image with either DAC or LCM support

## Building Apps for DAC

### OCI Bundle Structure

DAC applications are packaged as OCI bundles with the following structure:

```
myapp-bundle/
├── config.json          # OCI runtime configuration
└── rootfs/              # Container root filesystem
    ├── bin/
    ├── lib/
    ├── etc/
    └── ...
```

### Creating a Simple DAC Application

Coming soon: Step-by-step instructions for creating OCI bundles for DAC.

## Building Apps for LCM

### OCI Image Format

LCM applications use standard OCI images that can be:

- Built locally or pulled from container registries
- Stored in private registries

### Creating a Simple LCM Application

Coming soon: Step-by-step instructions for creating OCI images for LCM.

## Application Examples

### Demonstration Apps

Reference demonstration applications are available for both runtimes:

- **LCM Demo** - OCI Image example
- **DAC Demo** - OCI Bundle example

Details and build instructions coming soon.

## Best Practices

1. **Version your applications** - Use semantic versioning for releases
2. **Test locally first** - Validate on development hardware before deployment
3. **Document dependencies** - Clearly specify required libraries and services

## Related Resources

- [Installing the Toolkit](installing-toolkit.md) - Initial setup instructions
- [Deploying Apps](deploying-apps.md) - Deploy applications to devices
- [Data Models](data-models.md) - TR-369/USP data models for lifecycle management
- [System Architecture](architecture.md) - Architecture overview

## Contributing

If you have example applications or tutorials to share, please contribute by opening a pull request or issue on the [GitHub repository](https://github.com/rdkcentral/meta-rdk-broadband-apps).
