# Release Procedure
Follow these steps to create a release:

1. Document all relevant changes in the [Changelog](https://github.com/jomjol/AI-on-the-edge-device/blob/rolling/Changelog.md) in the `main` branch.
   To get a list of commits, you can call `git log --oneline` or check [commits/main/](https://github.com/jomjol/AI-on-the-edge-device-docs/commits/main/). Summarize the relevant changes since the last release.
1. Wait for the GitHub action to run successfully.
1. Test it to see if everything worsk as expected.
1. Update the contributors list in the [README.md](https://github.com/jomjol/AI-on-the-edge-device7README.md) by triggering the [Manually update contributors list](https://github.com/jomjol/AI-on-the-edge-device/actions/workflows/manual-update-contributors-list.yaml) action.
1. Go to [releases/new](https://github.com/jomjol/AI-on-the-edge-device/releases/new) to create a new release.
   Fill in a new tag and select "Create new tag: xxx on publish".
   
   A tag should have the format x.y.z.
   
   It is suggested to first select "Set as a pre-release" at the bottom.   
1. Wait for the GitHub-Action of release creation. After all is done:
    * the release should be created
    * the artifacts are downloadable from release 
    * The documented changes were applied to the release
7. In case of a full release (not a pre-release), check that the [Web Installer](https://jomjol.github.io/AI-on-the-edge-device) shows the right version. If needed, run he action manually: [github.com/jomjol/AI-on-the-edge-device/actions/workflows/manual-update-webinstaller.yml](https://github.com/jomjol/AI-on-the-edge-device/actions/workflows/manual-update-webinstaller.yml).
