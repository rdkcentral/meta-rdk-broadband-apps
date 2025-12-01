# Deploying Apps

This guide provides walkthroughs for deploying and managing containerized applications on RDK broadband devices using either DAC (Dobby and DSM utilities from [meta-rdk](https://github.com/rdkcentral/meta-rdk/tree/develop/recipes-containers)) or LCM (Lifecycle Management from [prplLCM](https://gitlab.com/prpl-foundation/prplrdkb/metalayers/meta-lcm)).

!!! note "Documentation In Progress"
    This page is currently under development. Detailed tutorials and examples will be added in future updates.

**Reference Hardware**: All examples in this guide use the **Banana Pi BPI-R4** as the target device.

## Prerequisites

Before deploying apps, ensure you have:

- Completed the [Installing the Toolkit](installing-toolkit.md) guide
- Built and flashed an RDK image with either DAC or LCM enabled
- SSH or serial console access to your Banana Pi BPI-R4 device
- A container image or bundle ready to deploy (see [Building Apps](building-apps.md))

## Deploying with DAC

### Using Command Line Interface

DAC provides command-line tools for container management:

```bash
# Install a deployment unit using rbuscli
rbuscli method_values "Device.SoftwareModules.InstallDU()" \
    URL string http://example.com/app.tar.gz \
    ExecutionEnvRef string default

# Query all SoftwareModules
dmcli eRT getv Device.SoftwareModules.

# Start an execution unit
rbuscli method_values "Device.SoftwareModules.ExecutionUnit.1.SetRequestedState()" \
    RequestedState string Active

# Stop an execution unit
rbuscli method_values "Device.SoftwareModules.ExecutionUnit.1.SetRequestedState()" \
    RequestedState string Idle

# Uninstall a deployment unit
rbuscli method_values "Device.SoftwareModules.DeploymentUnit.1.Uninstall()" \
    RetainData bool false
```

### Deployment Workflow

1. **Prepare the OCI bundle** on your development machine
2. **Transfer bundle** to the device or make it accessible via HTTP
3. **Install** using `Device.SoftwareModules.InstallDU()`
4. **Start** the execution unit using `SetRequestedState()`
5. **Monitor** status via `Device.SoftwareModules` data model

## Deploying with LCM

### Using Command Line Interface

LCM provides the `ba-cli` tool for container management:

```bash
# Install a deployment unit from OCI registry
ba-cli 'Device.SoftwareModules.InstallDU( \
    URL = "docker://index.docker.io/user/image:latest", \
    ExecutionEnvRef = "Device.SoftwareModules.ExecEnv.1." )'

# Query all SoftwareModules
ba-cli 'Device.SoftwareModules.?'

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

### Using LXC Tools

LCM also provides direct LXC commands:

```bash
# List containers
lxc-ls -f

# Attach to a running container
lxc-attach <container-id>

# Check container status
lxc-info -n <container-id>
```

### Deployment Workflow

1. **Prepare the OCI image** (local build or registry)
2. **Install** from registry using `Device.SoftwareModules.InstallDU()`
3. **LCM pulls and converts** the image to LXC format
4. **Start** the execution unit using `SetRequestedState()`
5. **Monitor** status via `Device.SoftwareModules` data model or `lxc-ls`

## Managing Running Applications

### Lifecycle Operations

Both runtimes support standard lifecycle operations through the `Device.SoftwareModules` data model:

- **Install** - Deploy a new application
- **Start** - Begin execution of an installed application
- **Stop** - Halt a running application
- **Restart** - Stop and start an application
- **Update** - Replace an existing application with a new version
- **Uninstall** - Remove an application from the device

### Monitoring Application Status

Query application status using the data model:

=== "DAC"

    ```bash
    # Check execution unit status
    dmcli eRT getv Device.SoftwareModules.ExecutionUnit.1.Status
    
    # Get fault information if any
    dmcli eRT getv Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultCode
    dmcli eRT getv Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultMessage
    ```

=== "LCM"

    ```bash
    # Check execution unit details
    ba-cli 'Device.SoftwareModules.ExecutionUnit.1.?'
    
    # Check container status with lxc-ls
    lxc-ls -f
    ```

### Resource Management

Configure resource limits for applications:

- **Memory limits** - Control maximum memory usage
- **CPU shares** - Allocate CPU resources
- **Disk space** - Set storage quotas
- **Network** - Configure networking and ports

Details on resource configuration coming soon.

## Advanced Topics

### Auto-start Configuration

Configure applications to start automatically on boot:

- Set `AutoStart` parameter in the data model
- Configure execution environment settings

### Network Configuration

Configure application networking:

- Port mappings
- Network namespaces
- DNS configuration
- Firewall rules

### Persistent Data

Manage application data across updates and restarts:

- Application Data Volumes
- Volume mounting
- Data retention policies

### Security

Best practices for secure deployments:

- Signed deployment units
- Certificate verification
- Privilege restrictions
- Security scanning

## Troubleshooting

### Common Issues

**Application won't start:**
- Check execution fault codes in the data model
- Verify container runtime is operational
- Review system logs for errors

**Network connectivity issues:**
- Verify port mappings
- Check firewall rules
- Test DNS resolution

**Resource constraints:**
- Monitor memory and CPU usage
- Check disk space availability
- Review resource limit configuration

See [Acceptance Testing](acceptance-testing.md) for detailed troubleshooting procedures.

## Related Resources

- [Installing the Toolkit](installing-toolkit.md) - Initial setup instructions
- [Building Apps](building-apps.md) - Create containerized applications
- [Data Models](data-models.md) - TR-369/USP data models for lifecycle management
- [Acceptance Testing](acceptance-testing.md) - Testing procedures and validation
- [System Architecture](architecture.md) - Architecture overview

## Contributing

If you have deployment examples, tutorials, or corrections, please contribute by opening a pull request or issue on the [GitHub repository](https://github.com/rdkcentral/meta-rdk-broadband-apps).
