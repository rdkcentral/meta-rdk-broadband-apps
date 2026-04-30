# App Architecture & Build Flow

## Overview

RDK Broadband (RDK-B) applications designed for **prplLCM** and **Dobby** are packaged as **OCI (Open Container Initiative) images**.

An OCI image is a standardized container format that includes:

- Application binaries
- Runtime dependencies
- Metadata (labels, versioning)
- Execution instructions (entrypoint / CMD)

These images are:

- Built once (cross-platform if needed)
- Stored in a container registry (e.g., GHCR)
- Pulled and executed by container runtimes like Dobby

## High-Level Architecture

```mermaid
flowchart TD;
    A["Source Code Repo"];
    B["CI/CD Pipeline<br/>(GitHub Actions / Jenkins)"];
    C["OCI Image Build<br/>(Docker / Buildx)"];
    D["OCI Registry<br/>(e.g. ghcr.io)"];
    E["RDK Device<br/>(App Runtime)"];

    A --> B;
    B --> C;
    C --> D;
    D --> E;
```

## Expected Vendor Workflow

### 1. Build Trigger

- Triggered on **Git tag (e.g., v1.2.3)**
- Ensures semantic versioning

```yaml
on:
  push:
    tags:
      - 'v[0-9]+.[0-9]+.[0-9]+'
```

### 2. Version Extraction

```bash
APP_VERSION=$(git describe --tags --exact-match HEAD | sed 's/^v//')
```

Used for:
- Image tagging
- OCI metadata labels

### 3. Multi-Architecture Build

Typical targets:

- `arm64` (aarch64)
- `armv7`
- `amd64`

### 4. Image Tagging Strategy

Each build produces:
```
ghcr.io/org/app:arm64
ghcr.io/org/app:arm64-1.2.3
ghcr.io/org/app:latest
ghcr.io/org/app:1.2.3
```

### 5. Multi-Platform Manifest
A final manifest combines all architectures:

```bash
docker manifest create app:1.2.3 arm64 armv7 amd64
docker manifest push app:1.2.3
```

This allows:

```bash
docker pull app:1.2.3
```

→ Automatically pulls correct architecture

## Key Takeaways

- **OCI images** are the standard deployment artifact
- CI/CD pipelines handle build, test, and distribution
- Multi-arch support is strongly recommended
- Images must be **lightweight** and **secure**