# Data Models

This page documents the data models supported by the RDK Broadband Apps Framework for lifecycle management of containerized applications.

## Overview

The RDK Broadband Apps Framework implements TR-369 (USP - User Services Platform) data models for managing, monitoring, and controlling containerized applications on CPE devices. This follows the Broadband Forum specification for lifecycle management.

## Container Runtime Support

This layer provides data model support for both:

- **DAC**: Dobby and DSM utilities from [meta-rdk](https://github.com/rdkcentral/meta-rdk/tree/develop/recipes-containers)
- **LCM**: Lifecycle Management from [prplLCM](https://gitlab.com/prpl-foundation/prplrdkb/metalayers/meta-lcm)

## Lifecycle Management

Lifecycle management follows the [Broadband Forum TR-369 USP specification](https://usp.technology/specification/#sec:lifecycle-management), which defines standardized mechanisms for deploying, executing, and managing software modules on CPE devices.

### Software Modules

[Software Modules](https://usp.technology/specification/#sec:software-modules) provide the framework for managing containerized applications through standardized data model objects.

#### Deployment Units (DUs)

[Deployment Units](https://usp.technology/specification/#sec:deployment-units) represent installable software packages (e.g., OCI bundles or images) that can be deployed to the device.

**Deployment Unit Lifecycle State Machine:**

The DU lifecycle follows a state machine with the following states:

- **Installed**: DU is installed on the device
- **Uninstalled**: DU has been removed from the device
- **Failed**: DU installation or operation failed

Operations:
- `InstallDU()`: Install a new deployment unit from a URL
- `Update()`: Update an existing deployment unit
- `Uninstall()`: Remove a deployment unit from the device

**Data Model Path:** `Device.SoftwareModules.DeploymentUnit.{i}.`

#### Execution Units (EUs)

[Execution Units](https://usp.technology/specification/#sec:execution-units) represent running instances of deployed software (containers).

**Execution Unit Lifecycle State Machine:**

The EU lifecycle follows a state machine with the following states:

- **Idle**: EU is installed but not running
- **Starting**: EU is in the process of starting
- **Active**: EU is running
- **Stopping**: EU is in the process of stopping
- **Failed**: EU failed to start or encountered a runtime error

Operations:
- `SetRequestedState()`: Request state transition (Active, Idle, etc.)
- `Restart()`: Restart the execution unit

**Data Model Path:** `Device.SoftwareModules.ExecutionUnit.{i}.`

### Execution Environments (EEs)

[Execution Environments](https://usp.technology/specification/#sec:execution-environment-concepts) represent the container runtime environments (e.g., Dobby daemon, LXC runtime) where execution units run.

**Execution Environment Lifecycle State Machine:**

The EE lifecycle follows a state machine with the following states:

- **Up**: EE is operational and can run execution units
- **Down**: EE is not operational
- **Starting**: EE is initializing
- **Stopping**: EE is shutting down
- **Failed**: EE encountered an error

**Data Model Path:** `Device.SoftwareModules.ExecEnv.{i}.`

#### Application Data Volumes

[Application Data Volumes](https://usp.technology/specification/#sec:application-data-volumes) provide persistent storage for containerized applications, allowing data to survive container restarts and upgrades.

Features:
- Persistent data storage across container lifecycle
- Volume mounting into containers
- Data retention policies

#### Signing Deployment Units

[Signing Deployment Units](https://usp.technology/specification/#sec:signing-deployment-units) provides security mechanisms to verify the authenticity and integrity of software modules before installation.

Features:
- Cryptographic signature verification
- Certificate chain validation
- Trust store management

### Fault Model

The fault model defines how errors and failures are reported and handled in the lifecycle management system.

#### Deployment Unit Faults

[Deployment Unit Faults](https://usp.technology/specification/#sec:du-faults) describe errors that can occur during DU installation, update, or operation.

Common DU fault codes:
- Download failure
- Installation failure
- Insufficient storage
- Invalid package format
- Signature verification failure

**Data Model Parameter:** `Device.SoftwareModules.DeploymentUnit.{i}.ExecutionFaultCode`

#### Execution Unit Faults

[Execution Unit Faults](https://usp.technology/specification/#sec:eu-faults) describe errors that can occur during EU execution.

Common EU fault codes:
- Startup failure
- Runtime crash
- Resource exhaustion
- Configuration error
- Dependency failure

**Data Model Parameters:**
- `Device.SoftwareModules.ExecutionUnit.{i}.ExecutionFaultCode`
- `Device.SoftwareModules.ExecutionUnit.{i}.ExecutionFaultMessage`

## Data Model Hierarchy

The complete object hierarchy for software module management:

```
Device.SoftwareModules.
├── ExecEnv.{i}.                    # Execution Environments
│   ├── Enable
│   ├── Status
│   ├── Type
│   ├── InitialRunLevel
│   ├── CurrentRunLevel
│   └── ...
├── DeploymentUnit.{i}.             # Deployment Units
│   ├── UUID
│   ├── DUID
│   ├── Name
│   ├── Status
│   ├── Resolved
│   ├── URL
│   ├── ExecutionUnitList
│   ├── ExecutionEnvRef
│   └── ...
└── ExecutionUnit.{i}.              # Execution Units
    ├── EUID
    ├── Name
    ├── Status
    ├── RequestedState
    ├── ExecutionFaultCode
    ├── ExecutionFaultMessage
    ├── AutoStart
    ├── RunLevel
    ├── ExecutionEnvRef
    └── ...
```

## Command-Line Interface Examples

### DAC Commands

```bash
# Query all SoftwareModules
dmcli eRT getv Device.SoftwareModules.

# Install a deployment unit
rbuscli method_values "Device.SoftwareModules.InstallDU()" \
    URL string http://example.com/app.tar.gz \
    ExecutionEnvRef string default

# Start an execution unit
rbuscli method_values "Device.SoftwareModules.ExecutionUnit.1.SetRequestedState()" \
    RequestedState string Active

# Uninstall a deployment unit
rbuscli method_values "Device.SoftwareModules.DeploymentUnit.1.Uninstall()" \
    RetainData bool false
```

### LCM Commands

```bash
# Query all SoftwareModules
ba-cli 'Device.SoftwareModules.?'

# Install a deployment unit from OCI registry
ba-cli 'Device.SoftwareModules.InstallDU( \
    URL = "docker://index.docker.io/user/image:latest", \
    ExecutionEnvRef = "Device.SoftwareModules.ExecEnv.1." )'

# Start an execution unit
ba-cli 'Device.SoftwareModules.ExecutionUnit.1.SetRequestedState( \
    RequestedState = "Active" )'

# Stop an execution unit
ba-cli 'Device.SoftwareModules.ExecutionUnit.1.SetRequestedState( \
    RequestedState = "Idle" )'

# Uninstall a deployment unit
ba-cli 'Device.SoftwareModules.DeploymentUnit.1.Uninstall( \
    RetainData = "false" )'
```

## Related Resources

- [TR-369 USP Specification](https://usp.technology/specification/) - Official specification
- [Lifecycle Management](https://usp.technology/specification/#sec:lifecycle-management) - Detailed specification
- [Broadband Forum](https://www.broadband-forum.org/) - Standards organization
- [Installing the Toolkit](installing-toolkit.md) - How to integrate this layer
- [System Architecture](architecture.md) - Architecture overview
- [Acceptance Testing](acceptance-testing.md) - Testing procedures

## Contributing

If you have implemented additional data models or have corrections to this documentation, please contribute by opening a pull request or issue on the [GitHub repository](https://github.com/rdkcentral/meta-rdk-broadband-apps).
