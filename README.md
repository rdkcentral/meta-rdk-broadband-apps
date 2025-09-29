# meta-rdk-broadband-apps
Meta layer to add the Broadband Apps Framework to your existing RDK image.

[![Deploy MkDocs to GitHub Pages](https://github.com/rdkcentral/meta-rdk-broadband-apps/actions/workflows/deploy_docs.yml/badge.svg)](https://github.com/rdkcentral/meta-rdk-broadband-apps/actions/workflows/deploy_docs.yml)

[![GitHub milestone details](https://img.shields.io/github/milestones/progress-percent/rdkcentral/meta-rdk-broadband-apps/2)](https://github.com/rdkcentral/meta-rdk-broadband-apps/milestone/2)

[![GitHub milestone details](https://img.shields.io/github/milestones/progress-percent/rdkcentral/meta-rdk-broadband-apps/1)](https://github.com/rdkcentral/meta-rdk-broadband-apps/milestone/1)


## Documentation:
See `docs/` folder or the live [GitHub Pages site](https://rdkcentral.github.io/meta-rdk-broadband-apps/).


## Using This Repo
TODO

## GitHub Pages
We use `mkdocs` to publish `.md` files in the `docs/` folder to GitHub Pages.

See [Docs Generation Workflow](.github/workflows/deploy_docs.yml).

Required setting for this to work:
> * __Settings > Pages__
> * Under __"Build and deployment"__:
> * __Select Source:__ `GitHub Actions`

### Preview Site Locally
To preview the Pages site on your local machine:
```
pip install -r docs/requirements.txt
mkdocs serve
```
This will run a local server at http://127.0.0.1:8000/.



## LCM (prpl) enablement via sub-manifest

This layer provides:
- `conf/layer.conf` – marks this repo as a BitBake layer and recommends `meta-amx` and `meta-lcm`.
- `manifests/rdkbb-apps-lcm.xml` – manifest snippet to fetch prpl LCM dependencies.

### How to consume in a product build

**A) With a product manifest (recommended)**  
In your **product manifest repo** (the one you pass to `repo init -u …`):

1. Copy `manifests/rdkbb-apps-lcm.xml` into `manifests/` of your product manifest repo.
2. In your top manifest (e.g. `default.xml`) add:
   ```xml
   <remote name="github" fetch="https://github.com"/>
   <project remote="github"
            name="YOURORG/meta-rdk-broadband-apps"
            path="meta-rdk-broadband-apps"
            revision="main"/>
   <include name="manifests/rdkbb-apps-lcm.xml"/>


3. Add Layers & Enable LCM
 - In your Yocto build dir(build/ after source oe-init-build-env):
 - conf/bblayers.conf

BBLAYERS += " \
  ${TOPDIR}/../meta-rdk-broadband-apps \
  ${TOPDIR}/../meta-amx \
  ${TOPDIR}/../meta-lcm \
"



