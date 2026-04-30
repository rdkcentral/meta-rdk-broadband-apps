# Defining A Dockerfile For The OCI Image

## Overview

This guide defines best practices for creating Dockerfiles for RDK-B containerized applications.

## Base Image Selection

### Option 1: `FROM scratch` (Recommended for production)

```dockerfile
FROM scratch
```

| Pros | Cons|
|---|---|
| - Minimal size<br>- No attack surface | - Requires **fully static binaries** |

### Option 2: `FROM alpine` (Minimal Linux base, much smaller than Debian)

```dockerfile
FROM alpine:3.20
```

| Pros | Cons|
|---|---|
| - Small (~5MB)<br>- Includes package manager | - Uses **musl libc** (not glibc) |

## Static Linking with musl

To support `scratch`, compile binaries statically:

### Rust Example

```bash
target: x86_64-unknown-linux-musl
```

Install toolchain:

```bash
rustup target add x86_64-unknown-linux-musl
```

### Minimal Runtime Dockerfile Example

```dockerfile
FROM scratch

LABEL org.opencontainers.image.source="https://github.com/org/repo"
LABEL org.opencontainers.image.description="RDK-B OCI Application"

WORKDIR /app

COPY target/release/my-app /app/my-app
COPY templates /app/templates
COPY static /app/static

EXPOSE 8080

CMD ["/app/my-app"]
```

## ENTRYPOINT vs CMD

### CMD (Recommended)

```dockerfile
CMD ["/app/my-app"]
```

- Default command
- Easily overridden

### ENTRYPOINT (Optional)

```dockerfile
ENTRYPOINT ["/app/my-app"]
```

- Harder to override
- Good for fixed-function containers

## File Layout Best Practices

```text
/app
 ├── binary
 ├── templates/
 ├── static/
 └── config/
```

## OCI Metadata Labels

Include standard labels in your Dockerfile:

```dockerfile
LABEL org.opencontainers.image.version="1.2.3"
LABEL org.opencontainers.image.revision="abc1234"
LABEL org.opencontainers.image.source="https://github.com/org/repo"
LABEL org.opencontainers.image.description="RDK App"
```

## Key Recommendations

- Prefer `FROM scratch` + static binaries
- Use `alpine` only if dynamic dependencies are required
- Keep images **small (<50MB ideally)**
- Avoid unnecessary tools (curl, bash, etc.)
