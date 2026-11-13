"""news-image-01 v3: deliver the entry image to the output directory.

The entry is a newspaper front page summing up the world news of Friday
13 November 2026. Its lead is the FAA communications outage that grounded
US flights, and sixteen numbered stories below it cover the day across
regions and fields (Ukraine, Russia, Gaza, technology, Europe, Germany,
Kenya, India, Saudi Arabia, Guinea, Turkiye, climate, Africa, Asia-Pacific
and the Middle East). The finished image lives in this repository as
entry.png; this program writes those exact bytes to the output directory,
so running it twice produces the identical file both times.
"""

import os
import shutil

ENTRY_IMAGE = "entry.png"


def main():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(repo_dir, ENTRY_IMAGE)
    if not os.path.isfile(source):
        raise FileNotFoundError("entry image not found in repository: " + source)
    # The entry image is a JPEG: its first two bytes must be the SOI marker.
    # A truncated or misnamed source fails loudly here instead of reaching
    # the judge as a broken file.
    with open(source, "rb") as handle:
        if handle.read(2) != b"\xff\xd8":
            raise ValueError("entry image is not a JPEG file: " + source)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, ENTRY_IMAGE)
    shutil.copyfile(source, target)
    if os.path.getsize(target) != os.path.getsize(source):
        raise IOError("incomplete copy of entry image to " + target)


if __name__ == "__main__":
    main()
