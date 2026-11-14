#!/usr/bin/env python3
"""Download official Nerd Fonts releases and self-host WOFF2 Mono regular faces."""
import io
import json
from pathlib import Path
import urllib.request
import zipfile
from fontTools.ttLib import TTFont

NAMES = [
    "JetBrainsMono", "IosevkaTerm", "MapleMono", "FiraCode",
    "GeistMono", "CascadiaCode", "Monaspace", "Hack",
    "CommitMono", "0xProto",
]
OUT = Path("assets/fonts")
OUT.mkdir(parents=True, exist_ok=True)
headers = {"User-Agent": "awesome-coding-fonts", "Accept": "application/vnd.github+json"}
req = urllib.request.Request("https://api.github.com/repos/ryanoasis/nerd-fonts/releases/latest", headers=headers)
with urllib.request.urlopen(req, timeout=40) as response:
    release = json.load(response)
assets = {a["name"].lower(): a["browser_download_url"] for a in release["assets"]}
# Maple Mono is distributed by its own upstream project, not Nerd Fonts.
MAPLE_URL = "https://github.com/subframe7536/maple-font/releases/download/v7.9/MapleMono-NF.zip"
missing = [name for name in NAMES if name != "MapleMono" and name.lower() + ".zip" not in assets]
if missing:
    raise RuntimeError(f"Missing Nerd Fonts release archives ({release['tag_name']}): {', '.join(missing)}")
print("Nerd Fonts release:", release["tag_name"])

for i, name in enumerate(NAMES):
    asset = name.lower() + ".zip"
    url = MAPLE_URL if name == "MapleMono" else assets[asset]
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-coding-fonts"})
    with urllib.request.urlopen(req, timeout=180) as response:
        archive = zipfile.ZipFile(io.BytesIO(response.read()))
    candidates = [p for p in archive.namelist() if p.lower().endswith((".ttf", ".otf"))
                  and not p.startswith("__MACOSX/")]
    def rank(path):
        base = Path(path).name.lower()
        regular = "regular" in base and not any(x in base for x in ("italic", "bold", "light", "medium"))
        mono = "nerdfontmono" in base or (name == "MapleMono" and "maplemono" in base and "-nf" in base)
        return (not mono, not regular, "italic" in base, len(path))
    candidates.sort(key=rank)
    if not candidates or rank(candidates[0])[0] or rank(candidates[0])[1]:
        raise RuntimeError(f"No regular mono font in {asset}: {candidates[:8]}")
    chosen = candidates[0]
    font = TTFont(io.BytesIO(archive.read(chosen)))
    font.flavor = "woff2"
    dest = OUT / f"{i}.woff2"
    font.save(dest)
    print(f"{name}: {chosen} -> {dest} ({dest.stat().st_size:,} bytes)")
