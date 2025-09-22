# meta-rdk-broadband-apps
Meta layer to add the Broadband Apps Framework to your existing RDK image.

## Documentation:
See `docs/` folder or the live [GitHub Pages site](TODO).


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