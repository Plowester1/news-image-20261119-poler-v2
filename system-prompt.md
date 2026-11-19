# Build instructions

This entry was built in small steps: first a plain `main.py` that copies
`entry.png` to `/output/entry.png`, then a verification step that compares the
SHA-256 of the source and the written file and raises an error on mismatch,
then documentation files (README, LICENSE, owner metadata, this note).
