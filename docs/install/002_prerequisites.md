# Device / Hardware Requirements

This page outlines the hardware and storage requirements for devices to run containerized applications.

## Flash Layout Requirements

To support containerised applications, devices must support a dedicated **writeable** and **encrypted** flash partition as specified below:

| Partition | Mount Point | Type | Security | Minimum Size | Purpose |
|-----------|-------------|------|----------|--------------|---------|
| Apps | `/apps` | Read-Write | Encrypted (TEE preferred) | 512 MB | Stores app images, persistent app data, and app logs | 

!!! tip "Why a new **dedicated partition**?"
    - **Isolation**: Applications cannot corrupt the root filesystem
    - **Recovery**: "Restore to default" operations can safely erase the apps partition without affecting the base image
    - **Security**: Application storage can be secured independently from the system partition
    - **Write Permissions**: Only applies to the apps partition, not to the base image.

!!! note "During a **Factory Restore** operation:"
    - The **apps partition should be erased**, removing all installed applications and their data, and returning the device to a clean state for app reinstallation.
    - The **base squashfs image must remain intact**, preserving the root filesystem.

    This behavior ensures that factory reset operations are **safe** and **predictable**.

## Directory Structure

The recommended directory structure for the `/apps` mount is as follows:

```bash
/apps/                      # Mounted read-write partition for apps
├── <app-id>/               # Per-application data directory using obfuscated ID for security   
│   └── <image>             # App OCI Image
│   └── data/               # Persistent application data 
│   └── logs/               # Application logs
└── <app-id-2>/
    └── ...
```

!!! tip
    Each application must be provided with its own dedicated subdirectory:

    ```bash
    /apps/<app-id>/        # Per-application data directory using obfuscated IDs
    ```

    This isolation ensures:

    - Applications cannot **identify** other applications' partitions
    - Applications cannot **access** other applications' data / logs
    - Data **cleanup** when removing an application means deleting that app's subdirectory
    - **Quota** enforcement can be applied **per application**

## Minimum Flash Space

The device must allocate sufficient flash space for the `/apps` partition based on:

- Expected number of apps installed on the device
- Average app size
- Data storage requirements per app
- Log size per app & retention policies

!!! note "Individual App Quotas"
    To define individual runtime quotas for each app, such as Allocated Memory and Allocated Disk Space, see [Advanced Configurations](deploy/005_advanced).

## Application Storage Security

The `/apps` folder and its contents must be secured to prevent unauthorized access and malicious activity:

1. **Encryption / TEE**: The `/apps/` folder must be secured via encryption or other good security practices
2. **Data Integrity**: Prevent spoofing or tampering with application packages and data
3. **Access Controls**: Implement appropriate permissions to restrict application access
