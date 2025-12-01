# meta-rdk-broadband-apps

Meta layer to add the Broadband Apps Framework to your existing RDK image.

## Overview

This Yocto/OpenEmbedded meta-layer provides containerization support for RDK (Reference Design Kit) broadband devices. It enables you to deploy and manage containerized applications using either:

- **DAC** - Dobby and DSM utilities from [meta-rdk](https://github.com/rdkcentral/meta-rdk)
- **LCM** - Lifecycle Management from [prplLCM](https://gitlab.com/prpl-foundation/prplrdkb/metalayers) (prpl Foundation's prplOS project)

## Quick Links

### Getting Started
- [**Getting Started Guide**](getting-started.md) - Complete build instructions for DAC and LCM on Raspberry Pi 4 and Banana Pi BPI-R4
- [**System Architecture**](architecture.md) - Reference system architecture and components
- [**Acceptance Testing**](acceptance-testing.md) - Testing procedures and validation

### Data Models
- [**Data Models**](data-models.md) - TR-369/USP data models for lifecycle management, including Software Modules, Deployment Units, Execution Units, and Execution Environments

### Guides & Tutorials
- [**How-to: Managing Containerized Apps**](howto-manage-apps.md) - Guide for deploying and managing containers (coming soon)

## Reference Hardware

All tutorials and guides in this documentation use the **Banana Pi BPI-R4** as the reference hardware platform.

## Features

- ✅ Support for both DAC and LCM container runtimes
- ✅ OCI-compliant container support via DAC (Dobby)
- ✅ Integration with prpl Foundation's LCM stack (prplLCM)
- ✅ TR-369/USP remote management capabilities
- ✅ Backwards compatibility with TR-69/CWMP
- ✅ Yocto/OpenEmbedded integration
- ✅ Multiple Yocto release compatibility (Kirkstone, Mickledore, Nanbield, Scarthgap)

## Repository

GitHub: [rdkcentral/meta-rdk-broadband-apps](https://github.com/rdkcentral/meta-rdk-broadband-apps)

## Contributing

Contributions are welcome! Please see our repository for guidelines on:
- Reporting issues
- Submitting pull requests
- Documentation improvements

## License

See the [LICENSE](https://github.com/rdkcentral/meta-rdk-broadband-apps/blob/main/LICENSE) file in the repository for license information.
