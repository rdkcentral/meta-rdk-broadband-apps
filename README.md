# meta-rdk-broadband-apps
Meta layer to add the Broadband Apps Framework to your existing RDK image.

### Quick Links
[![Read The Wiki](https://img.shields.io/badge/Read_The_Wiki-6F3DFA.svg?logo=firefox)](https://rdkcentral.github.io/meta-rdk-broadband-apps/)

### Live Status Updates
[![Deploy Zensical to GitHub Pages](https://github.com/rdkcentral/meta-rdk-broadband-apps/actions/workflows/deploy_docs.yml/badge.svg)](https://github.com/rdkcentral/meta-rdk-broadband-apps/actions/workflows/deploy_docs.yml)

[![GitHub milestone details](https://img.shields.io/github/milestones/progress-percent/rdkcentral/meta-rdk-broadband-apps/2)](https://github.com/rdkcentral/meta-rdk-broadband-apps/milestone/2)

[![GitHub milestone details](https://img.shields.io/github/milestones/progress-percent/rdkcentral/meta-rdk-broadband-apps/1)](https://github.com/rdkcentral/meta-rdk-broadband-apps/milestone/1)


## Getting Started & Technical Docs:
See the `docs/` folder, or visit the live website: [![Read The Wiki](https://img.shields.io/badge/Read_The_Wiki-6F3DFA.svg?logo=firefox)](https://rdkcentral.github.io/meta-rdk-broadband-apps/).

### Building the GitHub Pages Site
We use `zensical` to publish `.md` files in the `docs/` folder to GitHub Pages.

See [Docs Generation Workflow](.github/workflows/deploy_docs.yml).

Required setting for this to work:
> * __Settings > Pages__
> * Under __"Build and deployment"__:
> * __Select Source:__ `GitHub Actions`

### Preview The Site On Your Local Machine
You can also preview the Pages site on your local machine, e.g. for development and debugging.

First, pull the `Zensical` docker image.
NOTE: This requires you to have `Docker Desktop` or the `docker` CLI tool installed and running on your machine.
```bash
docker pull zensical/zensical
```

Then run the `Zensical` docker image on this repo.
This will host a local web server at http://localhost:8000/ where you can preview the site.

```bash
cd path/to/meta-rdk-broadband-apps
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs zensical/zensical
```
NOTE: The server will automatically rebuild the site when you make changes to source files. No need to restart the docker container.

