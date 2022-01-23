import os
import random
import shutil
from pathlib import Path

import yaml
from PIL import Image

screen_yaml = Path(__file__).parent / ".." / "data" / "Screenshot.yaml"
screenshots_dir = Path(__file__).parent / ".." / "themes" / "qtile-theme" / "static"
thumbnails = screenshots_dir / "img" / "screenshots" / "thumbnails"

with open(screen_yaml, "r") as data:
    try:
        shots = yaml.safe_load(data)
    except yaml.YAMLError as e:
        raise ValueError(f"Unable to load screenshots: {e}")

if thumbnails.is_dir():
    shutil.rmtree(thumbnails)

os.mkdir(thumbnails)

for shot in shots:
    img = Path(shot["image"])
    try:
        image = Image.open(screenshots_dir / img)
    except IOError:
        continue
    image.thumbnail((200, 200))
    thumb_name = img.parent / "thumbnails" / img.name
    image.save(screenshots_dir / thumb_name)
    shot["thumbnail"] = thumb_name.as_posix()
    shot["name"] = img.name
    if shot["config"] is None:
        shot["config"] = ""

INLINE_SCREENSHOTS = random.sample(shots, 3)
SCREENSHOTS = shots
