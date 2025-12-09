# Device Prerequisites

This page outlines the hardware and storage requirements for devices to run containerized applications.

## Flash Layout Requirements

To support containerized applications, devices must have the following dedicated **writeable** flash partitions with minimum sizes and mount points as specified:

| Partition | Minimum Size | Mount Point | Purpose | Writable |
|-----------|--------------|-------------|---------|----------|
| App Storage | 256 MB | `/apps/packages` | Stores downloaded application packages (Deployment Units) | Yes |
| App Data | 128 MB | `/apps/data` | Stores persistent application data | Yes |
| App Logs | 20 MB | `/apps/logs` | Stores application log files | Yes |

### Partition Structure

The recommended flash structure uses a dedicated `/apps` partition separate from the root filesystem:

```bash
/apps/                      # Dedicated partition for applications
├── packages/               # Application packages (Deployment Units)
├── data/                   # Persistent application data
│   └── <app-id>/           # Per-application data directory using obfuscated ID for security
└── logs/                   # Application logs
    └── <app-id>/           # Per-application logs directory using obfuscated ID for security
```

## Root Filesystem Protection

It is generally safe to keep the root filesystem (rootfs) untouched. Using **SquashFS** for the root filesystem is recommended to maintain system integrity and reliability. 

Thus, a **dedicated partition** in the device flash for storing applications outside of rootfs is **mandatory**. This separation provides:

- **Isolation**: Applications cannot corrupt the root filesystem
- **Recovery**: "Restore to default" operations can safely erase the apps partition without affecting the base image
- **Security**: Application storage can be secured independently from the system partition
- **Write Permissions**: Only applies to the apps partition, not to the base image.

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

1. **Encryption or Alternative Security**: The `/apps/` folder must be secured via encryption or other good security practices
2. **Data Integrity**: Prevent spoofing or tampering with application packages and data
3. **Access Controls**: Implement appropriate permissions to restrict application access

### Application Data Isolation

Each application should store its data in a dedicated subdirectory:

```bash
/apps/data/<app-id>/        # Per-application data directory using obfuscated IDs
```

This isolation ensures:

- Applications cannot **identify** other applications' partitions
- Applications cannot **access** other applications' data
- Data **cleanup** is straightforward when removing an application
- **Quota** enforcement can be applied **per application**

## Restore to Factory Behavior

During a "Factory Restore" operation:

- The **apps partition should be erased**, removing all installed applications and their data, and returning the device to a clean state for app reinstallation.
- The **base squashfs image must remain intact**, preserving the root filesystem.

This behavior ensures that factory reset operations are safe and predictable.
