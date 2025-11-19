# TR-69/CWMP Data Models

This page documents the backwards-compatible TR-69 (CWMP) data models supported by the RDK Broadband Apps Framework.

!!! note "Documentation In Progress"
    This page is currently under development. Data model documentation will be added in future updates.

## Overview

TR-069 (CWMP - CPE WAN Management Protocol) is a widely-deployed protocol for remote management of customer-premises equipment (CPE). While TR-369 (USP) is the modern successor, many deployments still require TR-069 compatibility.

The `meta-rdk-broadband-apps` layer maintains backwards compatibility with key TR-069 data models to support legacy management systems and gradual migration paths.

## Backwards Compatibility

This layer provides backwards compatibility for TR-069/CWMP data models, allowing devices built with the RDK Broadband Apps Framework to be managed by existing TR-069 ACS (Auto Configuration Server) systems.

## Supported Data Models

### Device.DeviceInfo

*Details coming soon*

### Device.ManagementServer

*Details coming soon*

### Device.SoftwareModules

*Details coming soon*

### Device.Services

*Details coming soon*

## Migration from TR-069 to TR-369

For operators looking to migrate from TR-069 to TR-369, consider:

1. **Dual Stack Support**: Run both protocols during transition period
2. **Data Model Mapping**: Map legacy TR-069 parameters to USP equivalents
3. **Gradual Migration**: Migrate devices in phases

See the [TR-369/USP Data Models](tr369-usp-data-models.md) page for information on the modern USP implementation.

## Related Resources

- [TR-069 Specification](https://www.broadband-forum.org/technical/download/TR-069.pdf) - Official CWMP specification
- [Broadband Forum](https://www.broadband-forum.org/) - Standards organization
- [Getting Started Guide](getting-started.md) - How to integrate this layer into your project

## Contributing

If you have implemented additional TR-069 data models or have corrections to this documentation, please contribute by opening a pull request or issue on the [GitHub repository](https://github.com/rdkcentral/meta-rdk-broadband-apps).
