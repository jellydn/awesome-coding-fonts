# Awesome Coding Fonts

Compare **10 free monospaced Nerd Fonts** side by side using realistic coding snippets.

**Live preview (after GitHub Pages is enabled):** https://jellydn.github.io/awesome-coding-fonts/

## Fonts

| # | Font | Focus |
|---|---|---|
| 1 | JetBrains Mono | Everyday coding |
| 2 | Iosevka Term | Dense terminal layouts |
| 3 | Maple Mono | Modern rounded style |
| 4 | Fira Code | Ligatures |
| 5 | Geist Mono | Minimalist |
| 6 | Cascadia Code | Editor readability |
| 7 | Monaspace Neon | Modern typography |
| 8 | Hack | Classic terminal |
| 9 | Commit Mono | Clear characters |
| 10 | 0xProto | Character differentiation |

## Features

- Two-column comparison (switchable to one column)
- TypeScript, React/TSX, Node.js, Go, Python, Rust, SQL, Bash, JSON, YAML
- Adjustable font size
- Syntax highlighting toggle (highlight.js, client-side, GitHub Dark)\n- Editable snippets
- Dark theme and responsive layout
- No build process or tracking

## Syntax highlighting\n\nUses a lightweight, browser-side [highlight.js](https://highlightjs.org/) CDN script. No API keys, server, or model downloads. The referenced [research paper](https://arxiv.org/abs/2510.04166) describes ML highlighting, but this implementation deliberately uses deterministic highlighting instead of claiming to run its model.\n\n## Run locally

Open `index.html` in a browser. After vendoring, all font files load from `assets/fonts/` on the same origin. Syntax highlighting currently loads highlight.js from a CDN.

## Self-host the 10 fonts\n\nRun **Actions → Vendor Nerd Fonts → Run workflow** once. The workflow downloads the official Nerd Fonts release archives, selects each Mono Regular font, converts it to WOFF2, and commits `assets/fonts/0.woff2` through `9.woff2` to `main`. Until the workflow completes, the browser will fall back to monospace.\n\nThe workflow needs GitHub Actions permission to write repository contents (Settings → Actions → General → Workflow permissions → Read and write permissions), unless an organization policy already grants it.\n\n## Publish on GitHub Pages

In **Settings → Pages**, select **Deploy from a branch**, branch **main**, folder **/(root)**, then save.

The font files are generated from official Nerd Fonts release assets; no font binaries are committed until the vendor workflow runs successfully.

## Licenses

Fonts are separately licensed by their respective authors; see [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts). The preview website is MIT licensed.
