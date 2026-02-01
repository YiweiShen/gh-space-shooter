# GitHub Space Shooter

![GitHub Release](https://img.shields.io/github/v/release/YiweiShen/gh-space-shooter) ![GitHub Release Date](https://img.shields.io/github/release-date/YiweiShen/gh-space-shooter) ![GitHub License](https://img.shields.io/github/license/YiweiShen/gh-space-shooter)

Transform your GitHub contribution graph into an animated space shooter game GIF for your profile README.

## Quick Start

Add this workflow to your repository at `.github/workflows/space-shooter.yml`:

```yaml
name: Update Space Shooter Game

on:
  schedule:
    - cron: '0 0 * * *' # Daily at midnight UTC
  workflow_dispatch: # Manual trigger

permissions:
  contents: write

jobs:
  update-game:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: YiweiShen/gh-space-shooter@v1.0.5
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```
