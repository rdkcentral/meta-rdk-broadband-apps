# TR-369/USP Data Models

This page documents the TR-369 (USP - User Services Platform) data models supported by the RDK Broadband Apps Framework.

!!! note "Documentation In Progress"
    This page is currently under development. Data model documentation will be added in future updates.

## Overview

TR-369, also known as the User Services Platform (USP), is a standardized protocol for managing, monitoring, and controlling connected devices. It is the successor to TR-069 (CWMP) and provides enhanced capabilities for modern IoT and broadband devices.

The `meta-rdk-broadband-apps` layer provides support for various TR-369 data models to enable remote management and monitoring of containerized applications and device capabilities using either:

- **DAC**: Dobby and DSM utilities from [meta-rdk](https://github.com/rdkcentral/meta-rdk)
- **LCM**: Lifecycle Management from [prplLCM](https://gitlab.com/prpl-foundation/prplrdkb/metalayers)

## Supported Data Models

### Device.SoftwareModules

See the dedicated [Device.SoftwareModules](device-softwaremodules.md) page for lifecycle management via TR-369/USP.

### Device.LocalAgent

*Details coming soon*

### Device.ContainerManagement

*Details coming soon*

## Related Resources

- [TR-369 Specification](https://usp.technology/) - Official USP specification
- [Device.SoftwareModules](device-softwaremodules.md) - Lifecycle management data model
- [Broadband Forum](https://www.broadband-forum.org/) - Standards organization
- [Getting Started Guide](getting-started.md) - How to integrate this layer into your project

## Contributing

If you have implemented additional TR-369 data models or have corrections to this documentation, please contribute by opening a pull request or issue on the [GitHub repository](https://github.com/rdkcentral/meta-rdk-broadband-apps).
