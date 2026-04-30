# Advanced Workflows

## Multi-Architecture Images

### Why?

RDK devices vary:

- ARMv7 (most common)
- ARM64 / AARCH64 (newer 64-bit SoCs)
- x86 (dev environments)

## Manifest Creation

```bash
docker manifest create ghcr.io/org/app:1.2.3 \
  ghcr.io/org/app:arm64-1.2.3 ghcr.io/org/app:armv7-1.2.3 ghcr.io/org/app:amd64-1.2.3

docker manifest push ghcr.io/org/app:1.2.3
```

## QEMU Emulation

Used when building non-native architectures:

```yaml
- uses: docker/setup-qemu-action@v4
```

## Image Size Optimization

### 1. Use `scratch`

Smallest possible image

### 2. Multi-stage builds

```dockerfile
FROM rust:latest AS builder
RUN cargo build --release

FROM scratch
COPY --from=builder /app/bin /app/bin
```

### 3. Strip binaries

```bash
strip target/release/my-app
```

### 4. Avoid unnecessary files

- No package managers
- No debug symbols
- No logs
- No unnecessary tools/libraries (e.g. curl, busybox, etc...)

## Alpine Linux vs Scratch Images

| Feature | Alpine | Scratch |
|---|---|---|
| Size | ~5MB | **~0MB** |
| Debugging | **Easier (Terminal)** | Hard |
| Security | Good | **Best** |
| 3rd Party Dependencies | **Installable via Package Manager** | Must be compiled from scratch |

## GitHub Actions Optimizations

### Caching

```bash
--cache-from type=gha
--cache-to type=gha,mode=max
```

### Parallel Target Arch Builds

```bash
strategy:
  matrix:
    arch: [arm64, armv7, amd64]
```

## OCI Image Metadata (Best Practices)

Include rich metadata:

```dockerfile
LABEL org.opencontainers.image.title="RDK App"
LABEL org.opencontainers.image.description="Dashboard UI for RDK"
LABEL org.opencontainers.image.vendor="Your Company"
LABEL org.opencontainers.image.licenses="Apache-2.0"
```

## GHCR (OCI Registry) Best Practices

- Use **public images** where possible
- Add descriptions in repo settings
- Use consistent naming, e.g. `ghcr.io/org/app`

## Optional Enhancements

- SBOM generation (Software Bill of Materials)
- Image signing (cosign)
- Vulnerability scanning

## Key Takeaways
- Multi-arch support improves portability
- Smaller images = faster deployment + better security
- CI/CD pipelines should be optimized and cached
- Metadata improves maintainability and traceability