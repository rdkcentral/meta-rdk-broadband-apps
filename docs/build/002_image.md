# Developing An OCI Image

!!! danger
    (Dockerfile, from scratch Vs alpine Vs Debian size tradeoffs / examples, entry point, labels, etc)

This guide provides instructions for building containerized applications for RDK-B.

!!! warning "Documentation In Progress"
    This page is currently under development. Detailed tutorials and examples will be added in future updates.

## Overview

The RDK Broadband Apps Toolkit supports two types of deployable artifacts:

- **OCI Images** - A packaged, distributable form of a containerized application.
- **OCI Bundles** - An unpacked, executable form of a containerized application, ready to be run by a container runtime.

## Contributing

If you have example applications or tutorials to share, please contribute by opening a pull request or issue on the [GitHub repository](https://github.com/rdkcentral/meta-rdk-broadband-apps).


## Prerequisites

Before building apps, ensure you have a built RDK image with either DAC or LCM support. 

See the [Installing the Toolkit](installing-toolkit.md) guide for full details.

## Building OCI Images

!!! warning "Coming Soon..."

## Building OCI Bundles

!!! warning "Coming Soon..."

## Best Practices

1. **Version your Apps** - Use semantic versioning for releases
2. **Test locally first** - Validate on development hardware before deployment
3. **Document Dependencies** - Clearly specify required libraries and services

