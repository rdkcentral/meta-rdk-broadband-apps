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