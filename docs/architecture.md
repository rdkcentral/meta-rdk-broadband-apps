# System Architecture

This page describes the reference system architecture for RDK Broadband Apps MVP 2025.

!!! note "MVP 2025 Scope"
    This document focuses on the device-side implementation. Backend components (USP Controller, Message Transport, OCI Registry, OCI Bundle Store) are **out of scope for 2025**.

## Overview

The RDK Broadband Apps reference system provides a framework for deploying and managing containerized applications on RDK broadband devices using standardized protocols and data models.

## Architecture Components

### Device-Side Components

The device-side implementation includes:

- **Container Runtime**: DAC (Dobby) or LCM (Lifecycle Management)
- **SoftwareModules Provider**: TR-369/USP data model implementation for lifecycle management
- **OCI Bundle/Image Support**: Standard container formats
- **Management Interface**: TR-369 USP protocol support

### Backend Components (Out of Scope for 2025)

The following backend components are documented for reference but not implemented in MVP 2025:

- **USP Controller**: Remote device management and orchestration
- **Message Transport**: MQTT/STOMP/WebSocket for USP communication
- **OCI Registry**: Container image registry
- **OCI Bundle Store**: Storage for OCI bundles and configurations

## Container Runtime Options

### DAC (Dobby Application Container)

DAC provides OCI-compliant container runtime capabilities using:

- **Dobby**: Container daemon and runtime
- **DSM**: Device Software Module manager

Key features:
- OCI bundle support
- Namespace isolation
- Resource management via cgroups
- Network configuration

Source: [meta-rdk/recipes-containers](https://github.com/rdkcentral/meta-rdk/tree/develop/recipes-containers)

### LCM (Lifecycle Management)

LCM provides container lifecycle management using the prpl Foundation's implementation:

- **LXC**: Linux Containers runtime
- **Ambiorix**: Data model framework
- **ba-cli**: Command-line interface

Key features:
- OCI image support (pulled from registries)
- Container lifecycle operations
- TR-369 data model integration

Source: [meta-lcm](https://gitlab.com/prpl-foundation/prplrdkb/metalayers/meta-lcm)

## Data Model Integration

Both DAC and LCM implementations provide support for the TR-369 **Device.SoftwareModules** data model, enabling:

- Remote container installation
- Container lifecycle management (start, stop, restart)
- Status monitoring and reporting
- Configuration management

See [Data Models](data-models.md) for detailed data model documentation.

## Supported Platforms

| Platform | Architecture | Container Runtime | Notes |
|----------|--------------|-------------------|-------|
| Raspberry Pi 4 | 32-bit/64-bit | DAC, LCM | Support to be deprecated |
| Banana Pi BPI-R4 | 64-bit | DAC, LCM | Recommended platform |

## Build Configuration

The container runtime is selected at build time using the `RDK_BB_APPS_TOOLKIT_CRUNTIME` variable:

```bash
# For DAC (default)
RDK_BB_APPS_TOOLKIT_CRUNTIME = "DAC"

# For LCM
RDK_BB_APPS_TOOLKIT_CRUNTIME = "LCM"
```

See [Getting Started](getting-started.md) for complete build instructions.

## Application Deployment

### DAC Application Deployment

DAC applications are deployed as **OCI bundles** containing:

- `config.json`: OCI runtime configuration
- `rootfs/`: Container root filesystem

### LCM Application Deployment

LCM applications are deployed as **OCI images** that are:

- Pulled from OCI-compliant registries (e.g., Docker Hub)
- Automatically converted to LXC containers
- Managed via TR-369 data model

## Management Interfaces

### Command Line

Both runtimes provide command-line tools:

#### DAC
```bash
# Using dmcli for Device.SoftwareModules access
dmcli eRT getv Device.SoftwareModules.

# Using rbuscli for operations
rbuscli method_values "Device.SoftwareModules.InstallDU()" \
    URL string http://example.com/app.tar.gz \
    ExecutionEnvRef string default
```

#### LCM
```bash
# Using ba-cli for Device.SoftwareModules access
ba-cli 'Device.SoftwareModules.?'

# Install container
ba-cli 'Device.SoftwareModules.InstallDU( \
    URL = "docker://index.docker.io/user/image:tag", \
    ExecutionEnvRef = "Device.SoftwareModules.ExecEnv.1." )'

# Control container state
ba-cli 'Device.SoftwareModules.ExecutionUnit.1.SetRequestedState( \
    RequestedState = "Active" )'
```

### USP Controller Integration (Out of Scope for 2025)

Future versions will support remote management via USP Controller using:

- MQTT/STOMP/WebSocket message transport
- TR-369 USP protocol operations
- Automated container deployment and updates

## Related Resources

- [Getting Started](getting-started.md) - Build instructions for DAC and LCM
- [Acceptance Testing](acceptance-testing.md) - Testing procedures
- [Data Models](data-models.md) - Data model specification
- [Getting Started](getting-started.md) - Build instructions for DAC and LCM
