# meta-rdk-broadband-apps

Meta layer to add the Broadband Apps Framework to your existing RDK image.

## Overview

This Yocto/OpenEmbedded meta-layer provides containerization support for RDK (Reference Design Kit) broadband devices. It enables you to deploy and manage containerized applications using either:

- **DAC (Dobby Application Container)** - The default OCI-compliant container runtime
- **LCM (Lightweight Container Manager)** - The prpl Foundation's alternative container manager

## Quick Links

### Getting Started
- [**Getting Started Guide**](getting-started.md) - Complete setup instructions for integrating this layer into your RDK project
- Build with DAC or LCM container runtime
- Verify layer integration

### Data Models
- [**TR-369/USP Data Models**](tr369-usp-data-models.md) - Supported USP data models for remote management
- [**TR-69/CWMP Data Models**](tr69-cwmp-data-models.md) - Backwards-compatible CWMP data models

### Guides & Tutorials
- [**How-to: Managing Containerized Apps**](howto-manage-apps.md) - Comprehensive guide for deploying and managing containers with DAC or LCM

## Reference Hardware

All tutorials and guides in this documentation use the **Banana Pi BPI-R4** as the reference hardware platform.

## Features

- ✅ Support for both DAC and LCM container runtimes
- ✅ OCI-compliant container support (DAC)
- ✅ Integration with prpl Foundation's LCM stack
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
