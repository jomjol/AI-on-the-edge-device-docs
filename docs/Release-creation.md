# Preparing for Release

1. [Changelog](https://github.com/jomjol/AI-on-the-edge-device/blob/rolling/Changelog.md) is merged back from `master` branch to `rolling` branch (should be the last step of the previous release creation)
1. All changes are documented in the [Changelog](https://github.com/jomjol/AI-on-the-edge-device/blob/rolling/Changelog.md) in `rolling` branch.
   To get a list of commits, call `git log --oneline`. Summarize the relevant chnages since the last release.


## Release creation steps
1. Merge`rolling` into `master` branch
2. Best to wait for the GitHub action to run successfully 
3. On `master` branch tag the version like `v11.3.1` and don't forget to push it:

     ```
     git checkout master
     git pull
     git tag v14.0.0
     git push --tags
     ```
     
5. Wait for the GitHub-Action of release creation. After all is done:
    * the release should be created
    * the artifacts are downloadable from release 
    * The documented changes were applied to the release
6. Merge master back in `rolling`
7. Check that the [Web Installer](https://jomjol.github.io/AI-on-the-edge-device) shows the right version. If needed, run he action manually: [github.com/jomjol/AI-on-the-edge-device/actions/workflows/manual-update-webinstaller.yml](https://github.com/jomjol/AI-on-the-edge-device/actions/workflows/manual-update-webinstaller.yml).
