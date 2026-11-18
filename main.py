"""News-image entry: copy the rendered front page to the output directory.

The image is entry.png beside this file. The program writes it to
<output>/entry.png, where <output> is MAKEFUN_OUTPUT_DIR when set and
/output otherwise. Deterministic: a plain byte copy, no network, no clock,
no randomness, so two runs always produce identical bytes.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> int:
    # Fail loudly (non-zero exit) if the image is missing, rather than
    # writing a partial or empty output the gate would reject.
    if not SRC.is_file():
        print(f"missing image: {SRC}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # shutil.copyfile copies bytes only (no metadata), so the output is
    # identical to the source on every run.
    shutil.copyfile(SRC, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
