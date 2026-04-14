# RDK Broadband Apps Toolkit

A Yocto meta-layer to add the Broadband Apps Toolkit to RDK-B builds.

## Overview

This Yocto meta-layer provides containerization support for RDK Broadband devices. It enables you to deploy and manage containerized applications using either:

- **DAC** - Dobby and DSM utilities from [meta-rdk](https://github.com/rdkcentral/meta-rdk/tree/main/recipes-containers).
- **LCM** - Lifecycle Management from [prplLCM](https://gitlab.com/prpl-foundation/prplrdkb/metalayers/meta-lcm) (prpl Foundation's prplOS project).

## Features

- ✅ Supports either DAC or prplLCM as the core containerization solution
- ✅ OCI-compliant container generation
- ✅ Standardized TR-369/USP remote management via Device.SoftwareModules
- ✅ Backwards compatibility with TR-69/CWMP
- ✅ Integrates into existing RDK-B projects without requiring a full uplift

## Repository

GitHub: [rdkcentral/meta-rdk-broadband-apps](https://github.com/rdkcentral/meta-rdk-broadband-apps)

## Contributing

Contributions are welcome! Please see our repository for guidelines on:

- Reporting issues
- Submitting pull requests
- Documentation improvements

## License

See the [LICENSE](https://github.com/rdkcentral/meta-rdk-broadband-apps/blob/main/LICENSE) file in the repository for license information.

## Quick Links

### Getting Started
- [**Device Prerequisites**](device-prerequisites.md) - Hardware and storage requirements for containerized applications.
- [**Installing the Toolkit**](installing-toolkit.md) - Complete build instructions for DAC and LCM.
- [**Building Apps**](building-apps.md) - Learn how to create containerized applications.
- [**Deploying Apps**](deploying-apps.md) - Deploy and manage applications on your device.

### Architecture & Testing
- [**System Architecture**](architecture.md) - Reference system architecture and components.
- [**Acceptance Testing**](acceptance-testing.md) - Testing procedures and validation.

### Data Models
- [**Data Models**](data-models.md) - TR-369/USP data models for lifecycle management, including Software Modules, Deployment Units, Execution Units, and Execution Environments.