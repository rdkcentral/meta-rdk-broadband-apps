# How-to: Manage Containerized Apps

This guide provides step-by-step walkthroughs for running and managing containerized applications on RDK broadband devices using either DAC (Dobby Application Container) or LCM (Lightweight Container Manager).

!!! note "Documentation In Progress"
    This page is currently under development. Additional tutorials and examples will be added in future updates.

**Reference Hardware**: All examples in this guide use the **Banana Pi BPI-R4** as the target device.

## Prerequisites

Before following these tutorials, ensure you have:

- Completed the [Getting Started Guide](getting-started.md)
- Built and flashed an RDK image with either DAC or LCM enabled
- SSH or serial console access to your Banana Pi BPI-R4 device
- A container image or bundle ready to deploy

## Deploying Your First Container

=== "DAC (Dobby)"

    ### Using DAC to Deploy a Container

    #### Step 1: Prepare Your Container Bundle
    
    DAC uses OCI-compliant container bundles. Prepare your bundle with a `config.json` file:
    
    ```bash
    # On your development machine
    mkdir -p /tmp/myapp-bundle
    cd /tmp/myapp-bundle
    
    # Create a basic config.json (example for a busybox container)
    cat > config.json << 'EOF'
    {
      "ociVersion": "1.0.0",
      "process": {
        "terminal": false,
        "user": {
          "uid": 0,
          "gid": 0
        },
        "args": [
          "/bin/sh",
          "-c",
          "echo 'Hello from DAC' && sleep infinity"
        ],
        "env": [
          "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "cwd": "/"
      },
      "root": {
        "path": "rootfs",
        "readonly": false
      },
      "hostname": "myapp"
    }
    EOF
    ```
    
    #### Step 2: Transfer Bundle to Device
    
    ```bash
    # Copy to your Banana Pi BPI-R4
    scp -r /tmp/myapp-bundle root@<device-ip>:/tmp/
    ```
    
    #### Step 3: Start the Container
    
    ```bash
    # SSH into your Banana Pi BPI-R4
    ssh root@<device-ip>
    
    # Start the container using DobbyTool
    DobbyTool start myapp /tmp/myapp-bundle/config.json
    ```
    
    #### Step 4: Verify Container is Running
    
    ```bash
    # List running containers
    DobbyTool list
    
    # Check container info
    DobbyTool info myapp
    ```

=== "LCM (Lightweight Container Manager)"

    ### Using LCM to Deploy a Container
    
    #### Step 1: Prepare Your Container Configuration
    
    LCM uses its own configuration format. Create a configuration file:
    
    ```bash
    # On your development machine
    mkdir -p /tmp/myapp-lcm
    cd /tmp/myapp-lcm
    
    # Create LCM configuration (format may vary by version)
    cat > myapp.conf << 'EOF'
    {
      "name": "myapp",
      "image": "busybox:latest",
      "command": ["/bin/sh", "-c", "echo 'Hello from LCM' && sleep infinity"],
      "autostart": false
    }
    EOF
    ```
    
    #### Step 2: Transfer Configuration to Device
    
    ```bash
    # Copy to your Banana Pi BPI-R4
    scp /tmp/myapp-lcm/myapp.conf root@<device-ip>:/etc/lcm/containers/
    ```
    
    #### Step 3: Start the Container
    
    ```bash
    # SSH into your Banana Pi BPI-R4
    ssh root@<device-ip>
    
    # Start the container using LCM
    lcm start myapp
    ```
    
    #### Step 4: Verify Container is Running
    
    ```bash
    # List running containers
    lcm list
    
    # Check container status
    lcm status myapp
    ```

## Managing Running Containers

=== "DAC (Dobby)"

    ### Listing Containers
    
    ```bash
    # List all containers (running and stopped)
    DobbyTool list
    ```
    
    ### Stopping a Container
    
    ```bash
    DobbyTool stop myapp
    ```
    
    ### Restarting a Container
    
    ```bash
    DobbyTool restart myapp
    ```
    
    ### Removing a Container
    
    ```bash
    DobbyTool stop myapp
    DobbyTool remove myapp
    ```
    
    ### Viewing Container Logs
    
    ```bash
    # Check DobbyDaemon logs
    journalctl -u dobby -f
    ```
    
    ### Inspecting Container Details
    
    ```bash
    DobbyTool info myapp
    ```

=== "LCM (Lightweight Container Manager)"

    ### Listing Containers
    
    ```bash
    # List all containers
    lcm list
    
    # Show detailed status
    lcm status
    ```
    
    ### Stopping a Container
    
    ```bash
    lcm stop myapp
    ```
    
    ### Restarting a Container
    
    ```bash
    lcm restart myapp
    ```
    
    ### Removing a Container
    
    ```bash
    lcm stop myapp
    lcm remove myapp
    ```
    
    ### Viewing Container Logs
    
    ```bash
    # Check LCM logs (command may vary)
    lcm logs myapp
    
    # Or check system logs
    journalctl -u lcm -f
    ```
    
    ### Inspecting Container Details
    
    ```bash
    lcm inspect myapp
    ```

## Advanced Container Configuration

=== "DAC (Dobby)"

    ### Resource Limits
    
    Add resource limits to your `config.json`:
    
    ```json
    {
      "linux": {
        "resources": {
          "memory": {
            "limit": 134217728
          },
          "cpu": {
            "shares": 1024
          }
        }
      }
    }
    ```
    
    ### Network Configuration
    
    Configure network settings in `config.json`:
    
    ```json
    {
      "linux": {
        "namespaces": [
          {
            "type": "network"
          }
        ]
      }
    }
    ```
    
    ### Volume Mounts
    
    Mount host directories into the container:
    
    ```json
    {
      "mounts": [
        {
          "destination": "/data",
          "type": "bind",
          "source": "/var/lib/myapp-data",
          "options": ["bind", "rw"]
        }
      ]
    }
    ```

=== "LCM (Lightweight Container Manager)"

    ### Resource Limits
    
    Configure resource limits in your LCM configuration:
    
    ```json
    {
      "resources": {
        "memory_limit": "128M",
        "cpu_shares": 1024
      }
    }
    ```
    
    ### Network Configuration
    
    Configure network settings:
    
    ```json
    {
      "network": {
        "mode": "bridge",
        "ports": [
          "8080:80"
        ]
      }
    }
    ```
    
    ### Volume Mounts
    
    Mount host directories into the container:
    
    ```json
    {
      "volumes": [
        {
          "host": "/var/lib/myapp-data",
          "container": "/data",
          "readonly": false
        }
      ]
    }
    ```

## Container Auto-start on Boot

=== "DAC (Dobby)"

    ### Configuring Auto-start
    
    To automatically start containers on boot, you need to configure the DobbyDaemon settings.
    
    *Detailed instructions coming soon*

=== "LCM (Lightweight Container Manager)"

    ### Configuring Auto-start
    
    Set the `autostart` flag in your container configuration:
    
    ```json
    {
      "name": "myapp",
      "autostart": true
    }
    ```
    
    Then enable the container:
    
    ```bash
    lcm enable myapp
    ```

## Monitoring and Debugging

=== "DAC (Dobby)"

    ### Real-time Monitoring
    
    ```bash
    # Watch container status
    watch -n 1 "DobbyTool list"
    
    # Monitor daemon logs
    journalctl -u dobby -f
    ```
    
    ### Debugging Container Issues
    
    1. Check if DobbyDaemon is running:
       ```bash
       systemctl status dobby
       ```
    
    2. Verify container configuration:
       ```bash
       DobbyTool info myapp
       ```
    
    3. Check system logs for errors:
       ```bash
       journalctl -u dobby --no-pager | tail -100
       ```

=== "LCM (Lightweight Container Manager)"

    ### Real-time Monitoring
    
    ```bash
    # Watch container status
    watch -n 1 "lcm list"
    
    # Monitor LCM logs
    journalctl -u lcm -f
    ```
    
    ### Debugging Container Issues
    
    1. Check if LCM service is running:
       ```bash
       systemctl status lcm
       ```
    
    2. Verify container configuration:
       ```bash
       lcm inspect myapp
       ```
    
    3. Check system logs for errors:
       ```bash
       journalctl -u lcm --no-pager | tail -100
       ```

## Common Tasks

### Updating a Running Container

=== "DAC (Dobby)"

    ```bash
    # Stop the existing container
    DobbyTool stop myapp
    
    # Update the bundle (replace files in bundle directory)
    # Then restart
    DobbyTool start myapp /path/to/updated/bundle/config.json
    ```

=== "LCM (Lightweight Container Manager)"

    ```bash
    # Stop the existing container
    lcm stop myapp
    
    # Update the configuration
    # Edit /etc/lcm/containers/myapp.conf
    
    # Restart with new configuration
    lcm start myapp
    ```

### Backing Up Container Data

=== "DAC (Dobby)"

    ```bash
    # Stop the container
    DobbyTool stop myapp
    
    # Backup the bundle and any mounted volumes
    tar -czf myapp-backup.tar.gz /path/to/bundle /var/lib/myapp-data
    ```

=== "LCM (Lightweight Container Manager)"

    ```bash
    # Stop the container
    lcm stop myapp
    
    # Backup configuration and volumes
    tar -czf myapp-backup.tar.gz /etc/lcm/containers/myapp.conf /var/lib/myapp-data
    ```

## Best Practices

1. **Use Tagged Images**: Always use specific version tags for container images, not `latest`
2. **Resource Limits**: Set appropriate memory and CPU limits for all containers
3. **Health Checks**: Implement health checks for critical containers
4. **Logging**: Configure proper log rotation to prevent disk space issues
5. **Security**: Run containers with minimal privileges when possible
6. **Testing**: Test container configurations on Banana Pi BPI-R4 development hardware before deploying to production

## Troubleshooting

### Container Won't Start

=== "DAC (Dobby)"

    - Verify the bundle path and config.json syntax
    - Check DobbyDaemon logs: `journalctl -u dobby -n 100`
    - Ensure the rootfs directory exists and is accessible
    - Verify OCI compliance of config.json

=== "LCM (Lightweight Container Manager)"

    - Verify configuration file syntax
    - Check LCM service logs: `journalctl -u lcm -n 100`
    - Ensure all required dependencies are installed
    - Verify network connectivity if pulling images

### Performance Issues

- Check system resource usage: `top`, `free -h`, `df -h`
- Review container resource limits
- Monitor for memory leaks in containerized applications
- Check for disk I/O bottlenecks on Banana Pi BPI-R4

### Network Connectivity Problems

- Verify network namespace configuration
- Check firewall rules: `iptables -L`
- Ensure port mappings are correct
- Test connectivity from host: `ping`, `netstat -tulpn`

## Related Resources

- [Getting Started Guide](getting-started.md) - Initial setup instructions
- [TR-369/USP Data Models](tr369-usp-data-models.md) - Remote management via USP
- [TR-69/CWMP Data Models](tr69-cwmp-data-models.md) - Legacy management protocol

## Contributing

If you have additional examples, tutorials, or corrections, please contribute by opening a pull request or issue on the [GitHub repository](https://github.com/rdkcentral/meta-rdk-broadband-apps).
