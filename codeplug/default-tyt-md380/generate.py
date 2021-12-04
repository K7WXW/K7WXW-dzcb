#!/usr/bin/env python3

# This script generates the same codeplug as generate.sh
# by running dzcb via the python API

# K7WXW V0.1 - build bare codeplug with just the pnwdigital list
# and an updated include list. comment out seattledmr, default_k7abd,
# scan list.

from pathlib import Path
import os

from dzcb.recipe import CodeplugRecipe

cp_dir = Path(__file__).parent
output = Path(os.environ.get("OUTPUT") or (cp_dir / ".." / ".." / "OUTPUT"))

CodeplugRecipe(
    source_pnwdigital=True,
#    source_seattledmr=True,
#    source_default_k7abd=True,
#    scanlists_json=cp_dir / "scanlists.json",
    exclude=cp_dir / "exclude.csv",
    output_farnsworth=cp_dir.glob("md3?0-?hf.json"),
).generate(output / cp_dir.name)
