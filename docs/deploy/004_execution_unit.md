# Launching An App

!!! danger "TODO"
    Add details on calling the set requested state method via bacli Vs dmcli AND USP Vs webpa/acs. Add info on full data model settings including memory and disk quotas. Add screenshots on how to validate with `hello-rdk-app`

This section covers the following steps:

- **Start** - Launching an installed App (Deployment Unit) as an instance (Execution Unit) in a container (Execution Environment)
- **Stop** - Stopping a running App
- **Restart** - Restarting a running App

## Starting

### Resource Management

Configure resource limits for applications:

- **Memory limits** - Control maximum memory usage
- **CPU shares** - Allocate CPU resources
- **Disk space** - Set storage quotas
- **Network** - Configure networking and ports

!!! warning "Details on resource configuration coming soon."

### Monitoring 

```bash
# Check execution unit status
dmcli eRT getv Device.SoftwareModules.ExecutionUnit.1.Status

# Get fault information if any
dmcli eRT getv Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultCode
dmcli eRT getv Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultMessage
```


## Stopping

## Restarting
