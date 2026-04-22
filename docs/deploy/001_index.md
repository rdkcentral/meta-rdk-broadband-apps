# Lifecycle Management Overview

The Broadband Apps Toolkit follows the [Broadband Forum TR-369 USP specification](https://usp.technology/specification/#sec:lifecycle-management), which provides standard definitions for Deployment Units (Downloadable Apps, AKA Software Modules), Execution Units (Running Instances), and Execution Environments (e.g. Containers, Virtual Machines, etc...), as well as standard models for managing the state of Apps and Environments on CPE devices.

## Data Models

!!! tip "Note"
    This is up to date as of [TR-181 v2.20.1 (USP)](https://usp-data-models.broadband-forum.org/tr-181-2-20-1-usp.html). 

The RDK Broadband Apps Toolkit primarily implements the standard TR-369 (USP - User Services Platform) data models for managing, monitoring, and controlling containerised applications on CPE devices, following the Broadband Forum specification for lifecycle management.

Additionally, provisions have been made to bring feature parity to legacy remote management standards such as TR-069 (CPE WAN Management Protocol (CWMP)) as used by ACS (Auto Configuration Server) solutions. This has been done by defining a **new, custom data model** that can be utilised without requiring support for method invocation or notification events. 

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

## Key Terminology

The following sections provide an overview of the key terminology used in this wiki, with links to their definitions.

| Terminology | Description | Notes |
|---|---|---|
| [Software Modules](https://usp.technology/specification/#sec:software-modules) | Provides the framework for managing containerised applications through standardized data model objects. | |
| [Deployment Units](https://usp.technology/specification/#sec:deployment-units) (DU) | Represents installable software packages (e.g., OCI bundles or images) that can be deployed to the device. | The DU lifecycle follows a state machine with the following states:<br>- **Installed**: DU is installed on the device<br>- **Uninstalled**: DU has been removed from the device<br>- **Failed**: DU installation or operation failed<br><br>Key Operations:<br>- `Device.SoftwareModules.InstallDU()`: Install a new deployment unit from a URL<br>- `Device.SoftwareModules.DeploymentUnit.{i}.Update()`: Update an existing deployment unit<br>- `Device.SoftwareModules.DeploymentUnit.{i}.Uninstall()`: Remove a deployment unit from the device |
| [Execution Units](https://usp.technology/specification/#sec:execution-units) (EU) | Represents running instances of deployed software (containers). | The EU lifecycle follows a state machine with the following states:<br>- **Idle**: EU is installed but not running<br>- **Starting**: EU is in the process of starting<br>- **Active**: EU is running<br>- **Stopping**: EU is in the process of stopping<br>- **Failed**: EU failed to start or encountered a runtime error<br><br>Key Operations:<br>- `Device.SoftwareModules.ExecutionUnit.{i}.SetRequestedState()`: Request state transition (Active, Idle, etc.)<br>- `Device.SoftwareModules.ExecutionUnit.{i}.Restart()`: Restart the execution unit |
| [Execution Environments](https://usp.technology/specification/#sec:execution-environment-concepts) (EE) | Represents the container runtime environments (e.g., Dobby daemon, LXC runtime) where execution units run. | The EE lifecycle follows a state machine with the following states:<br>- **Up**: EE is operational and can run execution units<br>- **Down**: EE is not operational<br>- **Starting**: EE is initializing<br>- **Stopping**: EE is shutting down<br>- **Failed**: EE encountered an error<br><br>Key Operations:<br>- `Device.SoftwareModules.ExecEnv.{i}.Restart()`: Restart the execution environment |
| [Application Data Volumes](https://usp.technology/specification/#sec:application-data-volumes) | Provides persistent storage for containerised applications, allowing data to survive container restarts and upgrades. | Features:<br>- Persistent data storage across container lifecycle<br>- Volume mounting into containers<br>- Data retention policies<br><br>Related Data Models:<br>- `Device.SoftwareModules.ExecEnv.{i}.ApplicationData` |
| [Signing Deployment Units](https://usp.technology/specification/#sec:signing-deployment-units) | Provides security mechanisms to verify the authenticity and integrity of software modules before installation. | Features:<br>- Cryptographic signature verification<br>- Certificate chain validation<br>- Trust store management<br><br>Related Data Models:<br>- `Device.Security.Certificate` |
| [Deployment Unit Faults](https://usp.technology/specification/#sec:du-faults) | Describes errors that can occur during DU installation, update, or operation. | Common DU fault codes:<br>- Download failure<br>- Installation failure<br>- Insufficient storage<br>- Invalid package format<br>- Signature verification failure<br><br>Data Model Parameter:<br>- `Device.SoftwareModules.DeploymentUnit.{i}.ExecutionFaultCode` |
| [Execution Unit Faults](https://usp.technology/specification/#sec:eu-faults) | Describes errors that can occur during EU execution. | Common EU fault codes:<br>- Startup failure<br>- Runtime crash<br>- Resource exhaustion<br>- Configuration error<br>- Dependency failure<br><br>Data Model Parameters:<br>- `Device.SoftwareModules.ExecutionUnit.{i}.ExecutionFaultCode`<br>- `Device.SoftwareModules.ExecutionUnit.{i}.ExecutionFaultMessage` |
