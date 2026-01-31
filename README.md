# GitHub Space Shooter

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

      - uses: czl9707/gh-space-shooter@v1
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

Then display it in your README:

```markdown
![My GitHub Game](gh-space-shooter.gif)
```

## Inputs

| Input            | Description                                          | Required | Default                         |
| ---------------- | ---------------------------------------------------- | -------- | ------------------------------- |
| `github-token`   | GitHub token for fetching contributions              | Yes      | -                               |
| `username`       | GitHub username to generate game for                 | No       | Repository owner                |
| `output-path`    | Where to save the GIF                                | No       | `gh-space-shooter.gif`          |
| `strategy`       | Enemy clearing pattern: `column`, `row`, or `random` | No       | `random`                        |
| `fps`            | Generation FPS (higher = smoother)                   | No       | `40`                            |
| `output-fps`     | Output FPS after optimization (lower = smaller file) | No       | `10`                            |
| `max-colors`     | Max colors in palette (lower = smaller file)         | No       | `64`                            |
| `commit`         | Auto-commit the generated GIF                        | No       | `true`                          |
| `commit-message` | Commit message                                       | No       | `Update space shooter game GIF` |

## Outputs

| Output     | Description                        |
| ---------- | ---------------------------------- |
| `gif-path` | Path to the generated GIF          |
| `gif-size` | Size of the generated GIF in bytes |

## Examples

### Basic Usage

```yaml
- uses: czl9707/gh-space-shooter@v1
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

### Custom Strategy and Output

```yaml
- uses: czl9707/gh-space-shooter@v1
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    output-path: 'assets/game.gif'
    strategy: 'column'
```

### Smaller File Size

```yaml
- uses: czl9707/gh-space-shooter@v1
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    output-fps: '8'
    max-colors: '32'
```

### Without Auto-Commit

```yaml
- uses: czl9707/gh-space-shooter@v1
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    commit: 'false'

- name: Custom commit logic
  run: |
    git add gh-space-shooter.gif
    git commit -m "Custom message"
    git push
```

### Generate for Another User

```yaml
- uses: czl9707/gh-space-shooter@v1
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    username: 'torvalds'
```

## CLI Usage

You can also use this as a CLI tool:

```bash
pip install gh-space-shooter

# Set your GitHub token
export GH_TOKEN=your_token_here

# Generate GIF
gh-space-shooter <username> --output game.gif
```

## License

MIT
