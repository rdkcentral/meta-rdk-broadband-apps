# LCM (prpl) enablement via sub-manifest

This repository provides a sub-manifest to bring in prpl LCM dependencies and a layer config that declares recommended dependencies.

## What this delivers
- `manifests/rdkbb-apps-lcm.xml`: repo manifest snippet that fetches:
  - `meta-amx` (dependency)
  - `meta-lcm`
- `meta-rdk-broadband-apps/conf/layer.conf`: declares `LAYERRECOMMENDS` (or `LAYERDEPENDS`) for `meta-amx`, `meta-lcm`, and RDK base layers.

## How to use

### 1) Include the sub-manifest in your **product manifest** repo

> Note: `repo <include>` only works within the same manifest repo.

Copy `manifests/rdkbb-apps-lcm.xml` into your product’s manifest repo (e.g. under `manifests/`), then in your product manifest:

```xml
<manifest>
  <!-- your existing remotes/projects -->
  <include name="manifests/rdkbb-apps-lcm.xml"/>
</manifest>

