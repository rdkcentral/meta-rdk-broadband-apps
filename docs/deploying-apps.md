# Deploying Apps

This guide provides walkthroughs for deploying containerized applications for RDK-B devices. 

!!! warning "Documentation In Progress"
    This page is currently under development. Detailed tutorials and examples will be added in future updates.

## Contributing

If you have deployment examples, tutorials, or corrections, please contribute by opening a pull request or issue on the [GitHub repository](https://github.com/rdkcentral/meta-rdk-broadband-apps).


## Prerequisites

Before deploying apps, ensure you have:

- Completed the [Installing the Toolkit](installing-toolkit.md) guide
- Built and flashed an RDK-B image with either DAC or LCM enabled
- SSH or serial console access to your RDK-B device
- An OCI Image or Bundle ready to deploy (see [Building Apps](building-apps.md))

## Deployment Steps

#### 1. Upload your app to remote storage

!!! warning "TODO"

#### 2. Install the app on a device
```bash
Device.SoftwareModules.InstallDU()
```

#### 3. Run the app

!!! warning "TODO"

#### 4. Monitor the status of your app and execution environment

```bash
dmcli eRT getv Device.SoftwareModules.
```

#### 5. Stop the app

!!! warning "TODO"

#### 6. Uninstall the app
```bash
Device.SoftwareModules.DeploymentUnit.1.Uninstall()
```

## Lifecycle Management

The standard `Device.SoftwareModules` data model supports the following application lifecycle commands:

- **Install** - Install a new application on a device
- **Start** - Launch an installed application in a container
- **Stop** - Stop a running container
- **Restart** - Stop and restart an application container
- **Update** - Replace an existing application with a new version
- **Uninstall** - Remove an application from the device

### Monitoring Status

```bash
# Check execution unit status
dmcli eRT getv Device.SoftwareModules.ExecutionUnit.1.Status

# Get fault information if any
dmcli eRT getv Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultCode
dmcli eRT getv Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultMessage
```

### Resource Management

Configure resource limits for applications:

- **Memory limits** - Control maximum memory usage
- **CPU shares** - Allocate CPU resources
- **Disk space** - Set storage quotas
- **Network** - Configure networking and ports

!!! warning "Details on resource configuration coming soon."

## Advanced Topics

!!! warning "Documentation in progress..."

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

### Application won't start:
- Check execution fault codes in the data model
- Verify container runtime is operational
- Review system logs for errors

### Network connectivity issues:
- Verify port mappings
- Check firewall rules
- Test DNS resolution

### Resource constraints:
- Monitor memory and CPU usage
- Check disk space availability
- Review resource limit configuration

!!! tip "More Troubleshooting Tips"
    See [Acceptance Testing](acceptance-testing.md) for detailed troubleshooting procedures.