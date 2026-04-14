# Advanced Configurations

!!! danger
    3 obuspa deployment methods. usp-agent as an app. libuspclient as MTP/UDS socket. 

!!! danger
    BREAK THIS OUT INTO SEPARATE PAGES!

This page documents the data models supported by the RDK Broadband Apps Toolkit for managing the lifecycle of containerized applications. 

## Overview

The RDK Broadband Apps Toolkit primarily implements the standard TR-369 (USP - User Services Platform) data models for managing, monitoring, and controlling containerized applications on CPE devices, following the Broadband Forum specification for lifecycle management.

Additionally, provisions have been made to bring feature parity to legacy remote management standards such as TR-069 (CPE WAN Management Protocol (CWMP)) as used by ACS (Auto Configuration Server) solutions. This has been done by defining a **new, custom data model** that can be utilised without requiring support for method invocation or notification events. 

## Contributing

If you have implemented additional data models or have corrections to this documentation, please contribute by opening a pull request or issue on the [GitHub repository](https://github.com/rdkcentral/meta-rdk-broadband-apps).

## Data Models

!!! tip "Note"
    This is up to date as of [TR-181 v2.20.1 (USP)](https://usp-data-models.broadband-forum.org/tr-181-2-20-1-usp.html). 

=== "TR-369/USP"

    ```bash
    Device.SoftwareModules.
    ├── InstallDU()                     # Method - not available in CWMP-compatible version
    ├── DUStateChange!                  # Notification - not available in CWMP-compatible version
    ├── ExecEnvClass.{i}.               # ~Execution Environments~
    │   ├── AddExecEnv()                # Method - not available in CWMP-compatible version
    │   └── Capability.{i}.
    │       └── Specification           
    ├── ExecEnv.{i}.                    # ~Execution Environments~
    │   ├── SetRunLevel()               # Method - not available in CWMP-compatible version
    │   ├── Reset()                     # Method - not available in CWMP-compatible version
    │   ├── Enable
    │   ├── Status
    │   ├── Name
    │   ├── Type
    │   ├── InitialRunLevel
    │   ├── CurrentRunLevel
    │   ├── AllocatedDiskSpace
    │   ├── AvailableDiskSpace
    │   ├── AllocatedMemory
    │   ├── AvailableMemory
    │   └── ...
    ├── DeploymentUnit.{i}.             # ~Deployment Units~
    │   ├── Update()                    # Method - not available in CWMP-compatible version
    │   ├── Uninstall()                 # Method - not available in CWMP-compatible version
    │   ├── UUID
    │   ├── DUID
    │   ├── Name
    │   ├── Status
    │   ├── Resolved
    │   ├── URL
    │   ├── ExecutionUnitList
    │   ├── ExecutionEnvRef
    │   └── ...
    └── ExecutionUnit.{i}.              # ~Execution Units~
        ├── SetRequestedState()         # Method - not available in CWMP-compatible version
        ├── Restart()                   # Method - not available in CWMP-compatible version
        ├── EUID
        ├── Name
        ├── ExecEnvLabel
        ├── Status
        ├── ExecutionFaultCode
        ├── ExecutionFaultMessage
        ├── AutoStart
        ├── RunLevel
        ├── DiskSpaceInUse
        ├── MemoryInUse
        └── ...
    ```

=== "TR-069/CWMP Compatible"

    ```bash
    Device.X_RDK_SoftwareModules.
    └── ...                             # COMING SOON...
    ```


## Lifecycle Management

Lifecycle management follows the [Broadband Forum TR-369 USP specification](https://usp.technology/specification/#sec:lifecycle-management), which defines standardized mechanisms for deploying, executing, and managing software modules on CPE devices.

### Software Modules

[Software Modules](https://usp.technology/specification/#sec:software-modules) provide the framework for managing containerized applications through standardized data model objects.

### Deployment Units (DUs)

[Deployment Units](https://usp.technology/specification/#sec:deployment-units) represent installable software packages (e.g., OCI bundles or images) that can be deployed to the device.

#### Deployment Unit Lifecycle State Machine:

The DU lifecycle follows a state machine with the following states:

- **Installed**: DU is installed on the device
- **Uninstalled**: DU has been removed from the device
- **Failed**: DU installation or operation failed

#### Operations:
- `Device.SoftwareModules.InstallDU()`: Install a new deployment unit from a URL
- `Device.SoftwareModules.DeploymentUnit.{i}.Update()`: Update an existing deployment unit
- `Device.SoftwareModules.DeploymentUnit.{i}.Uninstall()`: Remove a deployment unit from the device

### Execution Units (EUs)

[Execution Units](https://usp.technology/specification/#sec:execution-units) represent running instances of deployed software (containers).

#### Execution Unit Lifecycle State Machine:

The EU lifecycle follows a state machine with the following states:

- **Idle**: EU is installed but not running
- **Starting**: EU is in the process of starting
- **Active**: EU is running
- **Stopping**: EU is in the process of stopping
- **Failed**: EU failed to start or encountered a runtime error

#### Operations:
- `Device.SoftwareModules.ExecutionUnit.{i}.SetRequestedState()`: Request state transition (Active, Idle, etc.)
- `Device.SoftwareModules.ExecutionUnit.{i}.Restart()`: Restart the execution unit

### Execution Environments (EEs)

[Execution Environments](https://usp.technology/specification/#sec:execution-environment-concepts) represent the container runtime environments (e.g., Dobby daemon, LXC runtime) where execution units run.

#### Execution Environment Lifecycle State Machine:

The EE lifecycle follows a state machine with the following states:

- **Up**: EE is operational and can run execution units
- **Down**: EE is not operational
- **Starting**: EE is initializing
- **Stopping**: EE is shutting down
- **Failed**: EE encountered an error

#### Operations:
- `Device.SoftwareModules.ExecEnv.{i}.Restart()`: Restart the execution environment

### Application Data Volumes

[Application Data Volumes](https://usp.technology/specification/#sec:application-data-volumes) provide persistent storage for containerized applications, allowing data to survive container restarts and upgrades.

#### Features:
- Persistent data storage across container lifecycle
- Volume mounting into containers
- Data retention policies

#### Related Data Models
- `Device.SoftwareModules.ExecEnv.{i}.ApplicationData`

### Signing Deployment Units

[Signing Deployment Units](https://usp.technology/specification/#sec:signing-deployment-units) provides security mechanisms to verify the authenticity and integrity of software modules before installation.

#### Features:
- Cryptographic signature verification
- Certificate chain validation
- Trust store management

#### Related Data Models
- `Device.Security.Certificate`

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

