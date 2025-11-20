# Device.SoftwareModules Data Model

This page documents the Device.SoftwareModules data model from the TR-369/USP specification for lifecycle management of containerized applications.

!!! note "Documentation In Progress"
    This page is currently under development. Detailed data model documentation will be added in future updates.

## Overview

The Device.SoftwareModules data model, as defined in the [TR-369 USP specification](https://usp.technology/), provides a standardized interface for lifecycle management of software modules, including containerized applications, on CPE devices.

This data model enables remote management systems to:

- Install and deploy software modules/containers
- Update existing modules
- Remove modules
- Query module status and configuration
- Manage module lifecycle (start, stop, restart)

## Supported Operations

### Coming Soon

Documentation for the following operations will be added:

- **Install**: Deploy new software modules or containers
- **Update**: Upgrade existing modules to new versions
- **Uninstall**: Remove software modules from the device
- **Start/Stop**: Control module execution state
- **Query**: Retrieve module status and configuration

## Data Model Structure

The Device.SoftwareModules object hierarchy includes:

- `Device.SoftwareModules.ExecEnv.{i}.` - Execution environments (container runtimes)
- `Device.SoftwareModules.DeploymentUnit.{i}.` - Deployable software units
- `Device.SoftwareModules.ExecutionUnit.{i}.` - Running software instances

Detailed parameter descriptions will be added in future updates.

## Integration with Container Runtimes

This layer provides Device.SoftwareModules support for both:

- **DAC**: Dobby and DSM utilities from [meta-rdk](https://github.com/rdkcentral/meta-rdk)
- **LCM**: Lifecycle Management from [prplLCM](https://gitlab.com/prpl-foundation/prplrdkb/metalayers)

## Related Resources

- [TR-369 USP Specification](https://usp.technology/) - Official specification
- [Getting Started Guide](getting-started.md) - How to integrate this layer
- [TR-369/USP Data Models](tr369-usp-data-models.md) - Other supported data models

## Contributing

If you have implemented Device.SoftwareModules support or have corrections to this documentation, please contribute by opening a pull request or issue on the [GitHub repository](https://github.com/rdkcentral/meta-rdk-broadband-apps).
