# Toolkit Overview & Architecture

The RDK Broadband Apps Toolkit is delivered as a Yocto meta-layer ready to be integrated into any existing RDK-B build.

This meta-layer provides standard utilities for installing and launching Apps, aligned with industry protocols and community solutions. 

- ✅ Integrates into existing RDK-B projects without requiring a full uplift
- ✅ Supports both DAC (Dobby) and prplLCM as containerisation options
- ✅ OCI-compliant image generation
- ✅ Standardised TR-369/USP lifecycle management via the `Device.SoftwareModules` TR-181 Data Model
- ✅ Backwards compatibility with TR-069/CWMP, WebPA, and other custom remote management and telemetry solutions

!!! note
    View the Toolkit Source Code on GitHub: [**rdkcentral/meta-rdk-broadband-apps**](https://github.com/rdkcentral/meta-rdk-broadband-apps)


# Architecture

!!! danger
    TODO: toolkit arch w/ components, api gateway deployment methods, mtp/uds client, etc