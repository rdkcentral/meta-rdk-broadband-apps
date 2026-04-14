# RDK Broadband Apps Toolkit

A Yocto meta-layer to add the Broadband Apps Toolkit to RDK-B builds.

# System Architecture

!!! warning "Documentation in progress"
    All documentation is currently being written in the [RDKCentral Wiki](https://wiki.rdkcentral.com/pages/viewpage.action?spaceKey=WG&title=Broadband+Apps+Framework+-+Working+Group)

## Overview

The RDK Broadband Apps Toolkit provides a standardized framework for building, deploying, and managing containerized applications for RDK Broadband devices using standardized and community-aligned protocols and technology.

### Goals

<table>
    <tr>
        <th>1</th>
        <th>Fast time-to-market for broadband features, utilising apps & containers to ship solutions quickly and independently of full firmware upgrades.</th>
    </tr>
    <tr>
        <th>2</th>
        <th>Deliver a reference solution into mainline RDK-B to enable all and any RDK-B users to start deploying apps in a standard way as soon as possible.</th>
    </tr>
    <tr>
        <th>3</th>
        <th>Define an App Catalogue of apps and their use cases from the community (currently in the <a href="https://wiki.rdkcentral.com/display/WG/App+Use+Cases">wiki</a>)</th>
    </tr>
</table>

## Architecture

!!! warning "Documentation in progress"

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