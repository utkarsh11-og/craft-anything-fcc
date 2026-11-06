# craft_anythingXFCC app icon

The artwork in this directory is the XFCC replacement icon created for this project. It
replaces the original Craft Anything raven icon. The original raven artwork and ArtCraft
brand assets are not part of this replacement; see the retained upstream notice at
`docs/brand/LICENSE-brand.txt`.

## Files

- `craft-anything.svg`: master SVG and scalable Linux icon.
- `craft-anything-1024.png`: 1024 px PNG render.
- `craft-anything.icns`: macOS bundle icon.
- `craft-anything.ico`: Windows icon.
- `hicolor/`: Linux icon-theme renders.
- `trace.py`: icon-processing utility, covered by the repository's MIT OR Apache-2.0 licence.

The filenames remain compatible with the existing build and packaging configuration. They
do not indicate that the original raven artwork is still used.

## Regenerate

Use the project's icon-generation workflow and its documented dependencies. Verify all
platform-specific outputs after regeneration.
