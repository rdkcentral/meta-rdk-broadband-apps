# Acceptance Testing

This page provides acceptance testing procedures for validating RDK Broadband Apps implementations on reference hardware.

!!! note "MVP 2025 Scope"
    Testing focuses on command-line interfaces. USP Controller integration testing is **out of scope for 2025**.

## Test Environments

### DAC on Banana Pi BPI-R4 with RDK-B 2025q2

Testing the DAC (Dobby) container runtime implementation.

### LCM on Banana Pi BPI-R4 with RDK-B 2025q2

Testing the LCM (Lifecycle Management) container runtime implementation.

## Testing Procedures

### Prerequisites

- Built and flashed RDK-B 2025q2 image with either DAC or LCM enabled
- SSH or serial console access to the device
- Network connectivity for pulling container images (LCM)
- Test container bundles/images prepared

### Kernel Configuration Verification

Before testing containers, verify required kernel configurations are enabled:

#### DAC Required Kernel Configs

```bash
# Verify cgroup configurations
grep -i "CONFIG_CGROUP_CPUACCT=y" /path/to/kernel/.config
grep -i "CONFIG_CGROUP_SCHED=y" /path/to/kernel/.config
grep -i "CONFIG_CGROUP_DEBUG=y" /path/to/kernel/.config

# Verify netfilter configuration
grep -i "CONFIG_IP_NF_RAW" /path/to/kernel/.config
grep -i "CONFIG_NETFILTER_XT_TARGET_CT" /path/to/kernel/.config
```

Expected configurations:
- `CONFIG_CGROUP_CPUACCT=y`
- `CONFIG_CGROUP_SCHED=y`
- `CONFIG_CGROUP_DEBUG=y`
- `CONFIG_IP_NF_RAW=m`
- `CONFIG_NETFILTER_XT_TARGET_CT=y` or `=m`

## Command Line Testing

### DAC Testing Procedures

#### Test 1: Verify DAC Installation

```bash
# Check if DobbyDaemon is running
ps aux | grep -i dobby

# Verify DAC layer is present
bitbake-layers show-layers | grep rdkbbapps
```

#### Test 2: Install Container via Device.SoftwareModules

```bash
# Install a container bundle using rbuscli
rbuscli method_values "Device.SoftwareModules.InstallDU()" \
    URL string http://10.26.60.86/busybox.tar.gz \
    ExecutionEnvRef string default
```

#### Test 3: Query SoftwareModules State

```bash
# Query all SoftwareModules objects
dmcli eRT getv Device.SoftwareModules.
```

Expected output should include:
- `Device.SoftwareModules.ExecEnv.X.*` - Execution environments
- `Device.SoftwareModules.DeploymentUnit.X.*` - Installed deployment units
- `Device.SoftwareModules.ExecutionUnit.X.*` - Running execution units

#### Test 4: Start Container

```bash
# Start the execution unit
rbuscli method_values "Device.SoftwareModules.ExecutionUnit.1.SetRequestedState()" \
    RequestedState string Active
```

#### Test 5: Verify Container Status

```bash
# Check container status
dmcli eRT getv Device.SoftwareModules.ExecutionUnit.1.Status
```

Expected status: `Active` or `Running`

#### Test 6: Stop and Remove Container

```bash
# Stop the container
rbuscli method_values "Device.SoftwareModules.ExecutionUnit.1.SetRequestedState()" \
    RequestedState string Idle

# Uninstall the deployment unit
rbuscli method_values "Device.SoftwareModules.DeploymentUnit.1.Uninstall()" \
    RetainData bool false
```

### LCM Testing Procedures

#### Test 1: Verify LCM Installation

```bash
# Check if LCM services are running
ps aux | grep -i lxc

# Verify LCM layers are present
bitbake-layers show-layers | grep -E "meta-lcm|meta-amx"
```

#### Test 2: Query Initial State

```bash
# Query SoftwareModules using ba-cli
ba-cli 'Device.SoftwareModules.?'
```

Expected output:
```
Device.SoftwareModules.
Device.SoftwareModules.DeploymentUnitNumberOfEntries=0
Device.SoftwareModules.ExecEnvNumberOfEntries=1
Device.SoftwareModules.ExecutionUnitNumberOfEntries=0
Device.SoftwareModules.ExecEnv.1.*
```

#### Test 3: Install Container from OCI Registry

```bash
# Install a container image from Docker Hub
ba-cli 'Device.SoftwareModules.InstallDU( \
    URL = "docker://index.docker.io/piotrnakraszewicz/alpine64:latest", \
    ExecutionEnvRef = "Device.SoftwareModules.ExecEnv.1." )'
```

#### Test 4: Verify Installation

```bash
# Query after installation
ba-cli 'Device.SoftwareModules.?'

# Check with lxc-ls
lxc-ls -f
```

Expected: Container should appear in lxc-ls output with STATE = STOPPED

#### Test 5: Start Container

```bash
# Set requested state to Active
ba-cli 'Device.SoftwareModules.ExecutionUnit.1.SetRequestedState( \
    RequestedState = "Active" )'

# Verify container is running
lxc-ls -f
```

Expected: Container STATE should be RUNNING with IP addresses assigned

#### Test 6: Attach to Container and Test Connectivity

```bash
# Attach to running container
lxc-attach <container-id>

# Inside container - test network connectivity
ping google.com

# Test DNS resolution
wget google.com

# Exit container
exit
```

#### Test 7: Check Container Details

```bash
# Query execution unit details
ba-cli 'Device.SoftwareModules.ExecutionUnit.1.?'
```

Verify fields:
- `Status="Active"` or `"Running"`
- `EUID` matches container ID
- `MemoryInUse`, `DiskSpaceInUse` show resource usage
- `ExecutionEnvRef` points to correct ExecEnv

#### Test 8: Stop Container

```bash
# Set requested state to Idle
ba-cli 'Device.SoftwareModules.ExecutionUnit.1.SetRequestedState( \
    RequestedState = "Idle" )'

# Verify container stopped
lxc-ls -f
```

Expected: Container STATE should be STOPPED

#### Test 9: Uninstall Container

```bash
# Uninstall the deployment unit
ba-cli 'Device.SoftwareModules.DeploymentUnit.1.Uninstall( \
    RetainData = "false" )'

# Verify removal
ba-cli 'Device.SoftwareModules.?'
lxc-ls -f
```

Expected:
- `DeploymentUnitNumberOfEntries=0`
- `ExecutionUnitNumberOfEntries=0`
- Container no longer appears in lxc-ls

## Acceptance Criteria

### DAC Acceptance Criteria

✅ **Pass Criteria:**

1. DobbyDaemon service is running
2. Container bundle can be installed via `Device.SoftwareModules.InstallDU()`
3. `Device.SoftwareModules` objects are correctly populated
4. Container can be started via `SetRequestedState("Active")`
5. Container status is accurately reflected in data model
6. Container can be stopped and uninstalled cleanly
7. All kernel configurations are properly enabled

### LCM Acceptance Criteria

✅ **Pass Criteria:**

1. LXC runtime is available and functional
2. Container image can be pulled from OCI registry
3. `Device.SoftwareModules` data model is fully implemented
4. Container lifecycle operations work correctly:
   - Install from OCI registry
   - Start/Stop via SetRequestedState
   - Status monitoring
   - Uninstall with data cleanup
5. Container networking functions properly
6. Container resource usage is tracked
7. `ba-cli` command-line interface works correctly

## Known Issues and Limitations

### Banana Pi BPI-R4

- Intermittent build issues (not related to Broadband Apps Toolkit)
- Some kernel configurations may require manual verification

### Raspberry Pi 4

- Platform support scheduled for deprecation
- Testing should prioritize Banana Pi BPI-R4

## USP Controller Testing (Out of Scope for 2025)

Future testing will include:

- Remote container deployment via USP Controller
- MQTT/STOMP message transport validation
- End-to-end lifecycle management scenarios
- Multi-device orchestration

## Troubleshooting

### DAC Issues

**Container fails to start:**
- Verify kernel cgroup configurations are enabled
- Check Dobby daemon logs: `journalctl -u dobby`
- Verify OCI bundle format is correct

**InstallDU fails:**
- Ensure bundle URL is accessible
- Check network connectivity
- Verify bundle integrity

### LCM Issues

**Container image pull fails:**
- Verify network connectivity to registry
- Check DNS resolution
- Verify image name and tag are correct

**lxc-attach issues:**
- Note: `lxc.seccomp` warnings can be ignored
- Container must be in RUNNING state

**Container networking issues:**
- Verify network interfaces are created
- Check IP address assignment
- Test DNS resolution inside container

## Related Resources

- [Getting Started](getting-started.md) - Build instructions
- [System Architecture](architecture.md) - Architecture overview
- [Device.SoftwareModules](device-softwaremodules.md) - Data model specification
