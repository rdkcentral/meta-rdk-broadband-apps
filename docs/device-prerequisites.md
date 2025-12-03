# Device Prerequisites

This page outlines the hardware and storage requirements for devices running containerized applications with the RDK Broadband Apps Framework.

## Flash Layout Requirements

To support containerized applications, devices must have dedicated flash partitions with the following minimum sizes:

| Partition | Minimum Size | Mount Point | Purpose | Writable |
|-----------|--------------|-------------|---------|----------|
| App Storage | 256 MB | `/apps/packages` | Stores downloaded application packages (Deployment Units) | Yes |
| App Data | 128 MB | `/apps/data` | Stores persistent application data | Yes |
| App Logs | 20 MB | `/apps/logs` | Stores application log files | Yes |

### Partition Structure

The recommended flash structure uses a dedicated `/apps` partition separate from the root filesystem:

```
/apps/                      # Dedicated partition for applications
├── packages/               # Application packages (Deployment Units)
├── data/                   # Persistent application data
│   └── <app-id>/          # Per-application data directory
└── logs/                   # Application logs
```

## Root Filesystem Protection

### SquashFS Recommendation

It is generally safe to keep the root filesystem (rootfs) untouched. Using **SquashFS** for the root filesystem is recommended to:

- Prevent rootfs corruption that cannot be recovered by a "restore to default" action
- Avoid requiring aftersales intervention for filesystem corruption issues
- Maintain system integrity and reliability

### Dedicated Application Partition

To ensure root filesystem integrity, a **dedicated partition** in the device flash for storing applications outside of rootfs is **mandatory**. This separation provides:

- **Isolation**: Applications cannot corrupt the root filesystem
- **Recovery**: "Restore to default" operations can safely erase the apps partition without affecting the base system
- **Security**: Application storage can be secured independently from the system partition

## Storage Requirements

### Minimum Flash Space

The device must allocate sufficient flash space for the `/apps` partition based on:

- Expected number of applications
- Average application size
- Data storage requirements per application
- Log retention policies

### Per-Application Quotas

Flash space quotas per application should be implemented to:

- Prevent a single application from consuming excessive space (e.g., 90% of the partition)
- Ensure fair resource allocation across applications
- Maintain system stability and performance

!!! note "Quota Policy"
    The definition and enforcement of per-application storage quotas in the data model is under discussion. Check the [Data Models](data-models.md) page for updates on quota configuration.

## Security Requirements

### Application Storage Security

The `/apps` folder and its contents must be secured to prevent unauthorized access and malicious activity:

1. **Encryption or Alternative Security**: The `/apps/` folder must be secured via encryption or other mechanisms
2. **Data Integrity**: Prevent spoofing or tampering with application packages and data
3. **Access Controls**: Implement appropriate permissions to restrict application access

### Application Data Isolation

Each application should store its data in a dedicated subdirectory:

```
/apps/data/<app-id>/        # Per-application data directory
```

This isolation ensures:

- Applications cannot access other applications' data
- Data cleanup is straightforward when removing an application
- Quota enforcement can be applied per application

## Restore to Default Behavior

During a "restore to default" operation:

- The **apps partition is erased**, removing all installed applications and their data
- The **root filesystem remains intact**, preserving the base system
- The device returns to a clean state ready for application deployment

This behavior ensures that factory reset operations are safe and predictable.

## Platform Support

Refer to the [Installing the Toolkit](installing-toolkit.md) page for supported platforms and their specific configurations.

## Next Steps

Once your device meets these prerequisites:

1. [Install the Toolkit](installing-toolkit.md) - Set up the build environment
2. [Build Apps](building-apps.md) - Create containerized applications
3. [Deploy Apps](deploying-apps.md) - Deploy and manage applications on your device

## Related Resources

- [System Architecture](architecture.md) - Understanding the reference system architecture
- [Data Models](data-models.md) - TR-369/USP data models for lifecycle management
- [Acceptance Testing](acceptance-testing.md) - Testing and validation procedures
