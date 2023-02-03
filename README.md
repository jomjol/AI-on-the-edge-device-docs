# User Documentation for the AI on the Edge Device Project
 
This repo contains the documentation for the [AI-on-the-Edge-Device Project](https://github.com/jomjol/AI-on-the-edge-device).

# How does it work
1. You can edit any `*.md` document in the [docs](docs) folder.
1. Then create a Pull Request for it to merge it into the `main` branch (or edit it directly in the `main` branch if you have the required rights).
1. When it got merged, the [Github Actions](https://github.com/jomjol/AI-on-the-edge-device-docs/actions) will re-generate the documentation and place it in the `gh-pages` branch. This branch automatically gets populated to the public [Documentation Site](https://jomjol.github.io/AI-on-the-edge-device-docs)

## Migrating existing Wiki Pages
The files from the [AI-on-the-Edge-Device Wiki](https://github.com/jomjol/AI-on-the-edge-device/wiki) got exported and added to this repo. Unless the files are listed in the [docs/nav.yml](docs/nav.yml) file, they will be listed in the **assorted pages** section of the left sidebar.

In the end, we should review all pages from there step by step and add them to the upper part of the navigation.

### Tasks to do
 - Make sure there is a top level title (#) and all other chapter headers are on lower levels (##, ###)
 - Check the links in the documents
 - Fetch included images and place them directly in the [docs/img](docs/img) folder
 - Rewrite to have a clear structure

## Editing a page
Each page has a link on its top-right corner `Edit on GitHub` which brings you directly to the Github editor.

## Adding new pages
1. Add a new `*.md` document in the [docs](docs) folder.
1. Add the **filename** to the [docs/nav.yml](docs/nav.yml) at the wished position in the **Links** section.

## Local Test
To test it locally:
1. Clone this repo
1. Install the required tools (See also [.github/workflows/build-docs.yaml](.github/workflows/build-docs.yaml)):
    ```
    pip install --upgrade pip
    pip install mkdocs mkdocs-gen-files mkdocs-awesome-pages-plugin mkdocs-material pymdown-extensions
    ```
1. In the main folder of the repo, call `mkdocs serve` (and keep it running).
  This will locally generate the documentation.
  You can access it under http://127.0.0.1:8000/AI-on-the-edge-device-docs/

    Any change to the files will automatically be applied.
