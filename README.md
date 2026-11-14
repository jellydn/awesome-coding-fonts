# Awesome Coding Fonts

A lightweight, side-by-side playground for comparing **10 free coding fonts** with real code, consistent syntax highlighting, and adjustable typography.

[**Live demo**](https://jellydn.github.io/awesome-coding-fonts/) · [Source](https://github.com/jellydn/awesome-coding-fonts) · [Report an issue](https://github.com/jellydn/awesome-coding-fonts/issues)

> **Scope:** A practical font comparison tool, not a font distribution service, code editor, or AI syntax-highlighting benchmark.

## Contents

- [Features](#features)
- [Font collection](#font-collection)
- [Try it](#try-it)
- [Self-hosted fonts](#self-hosted-fonts)
- [How it works](#how-it-works)
- [Contributing](#contributing)
- [Licensing](#licensing)

## Features

- **Side-by-side previews:** Compare fonts in one or two columns with identical code.
- **Real-world snippets:** TypeScript, React/TSX, Node.js, Go, Python, Rust, SQL, Bash, JSON, and YAML.
- **Typography controls:** Change font size without changing the snippet.
- **Editable code:** Paste your own sample to compare glyphs, punctuation, and spacing.
- **Syntax highlighting:** Toggle GitHub Dark highlighting on or off.
- **Static deployment:** Plain HTML, CSS, and JavaScript; no framework, build step, backend, account, or tracking.

## Font collection

| Font | Why compare it? |
| --- | --- |
| [JetBrains Mono](https://www.jetbrains.com/lp/mono/) | Clear characters and developer-focused typography |
| [Iosevka Term](https://typeof.net/Iosevka/) | Narrow, terminal-friendly glyphs |
| [Maple Mono](https://github.com/subframe7536/maple-font) | Rounded shapes and modern styling |
| [Fira Code](https://github.com/tonsky/FiraCode) | Programming ligatures |
| [Geist Mono](https://vercel.com/font) | Minimal, contemporary design |
| [Cascadia Code](https://github.com/microsoft/cascadia-code) | Terminal and editor readability |
| [Monaspace Neon](https://monaspace.githubnext.com/) | Distinctive shapes from the Monaspace family |
| [Hack](https://sourcefoundry.org/hack/) | Familiar, practical terminal typeface |
| [Commit Mono](https://commitmono.com/) | Readability and configurable character forms |
| [0xProto](https://github.com/0xType/0xProto) | Distinguishable lookalike characters |

The website targets **Nerd Font Mono Regular** variants for consistent monospace comparison. These patched fonts are maintained by the [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) project; each upstream font has its own license.

## Try it

Open the [live demo](https://jellydn.github.io/awesome-coding-fonts/), select a language, adjust the font size, and compare the same code across fonts. Turn highlighting off when you want to focus on glyph shapes alone.

To run locally, clone the repository and serve its root directory:

```sh
git clone https://github.com/jellydn/awesome-coding-fonts.git
cd awesome-coding-fonts
python3 -m http.server 8000
```

Open http://localhost:8000.

> The font previews need the generated `assets/fonts/*.woff2` files. If those files have not been committed yet, the browser falls back to a generic monospace font.

## Self-hosted fonts

Font assets are intended to be served **from this repository**, not fetched from a third-party font CDN at runtime.

To generate the 10 WOFF2 files:

1. Open [Actions → Vendor Nerd Fonts](https://github.com/jellydn/awesome-coding-fonts/actions/workflows/vendor-fonts.yml).
2. Choose **Run workflow** on `main`.
3. Confirm the workflow succeeds and commits `assets/fonts/0.woff2` through `9.woff2`.

The workflow downloads official Nerd Fonts release archives, selects regular mono variants, converts them with FontTools, and commits the generated assets. It requires GitHub Actions **Contents: write** permission. If a commit is denied, check **Settings → Actions → General → Workflow permissions**.

To regenerate locally instead:

```sh
python3 -m pip install 'fonttools[woff]>=4.50,<5'
python3 scripts/vendor_fonts.py
```

This is a one-time asset-generation step, not a build requirement for site visitors. Verify the resulting files and the applicable font licenses before redistribution.

## How it works

| Component | Implementation |
| --- | --- |
| UI | Single `index.html` |
| Font assets | Same-origin WOFF2 in `assets/fonts/` |
| Highlighting | [highlight.js](https://highlightjs.org/) via CDN |
| Hosting | GitHub Pages |
| Data collection | None |

Syntax highlighting uses **highlight.js**, not an AI model. This keeps the site small and predictable; the [ML syntax-highlighting paper](https://arxiv.org/abs/2510.04166) is background research, not a dependency or implemented feature.

**Offline caveat:** Fonts are self-hosted once generated, but highlight.js and its theme still load from a CDN. Highlighting may be unavailable offline; the code preview remains readable.

To publish the site, configure **Settings → Pages → Deploy from a branch → `main` → `/(root)`**.

## Contributing

Issues and pull requests are welcome for broken font loading, incorrect font metadata, accessibility improvements, and better code samples.

Please keep changes focused: preserve the static architecture, avoid unnecessary dependencies, and verify the same snippet renders consistently across all 10 previews.

- [Open an issue](https://github.com/jellydn/awesome-coding-fonts/issues/new)
- [Submit a pull request](https://github.com/jellydn/awesome-coding-fonts/pulls)

## Licensing

**Fonts:** Each font and its Nerd Fonts patches retain their respective upstream licenses. See [Nerd Fonts licenses](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts) and the individual font projects above.

**Website source:** No root `LICENSE` file is currently present. A repository license should be added before describing the website code as MIT-licensed.
