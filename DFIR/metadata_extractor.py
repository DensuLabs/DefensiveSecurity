import sys
import subprocess
from pathlib import Path

# Dependency setup
try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except ImportError:
    print("[!] Pillow not found. Installing automatically...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image
    from PIL.ExifTags import TAGS


def get_metadata(image_path: str | Path) -> dict[str, str | int | bytes] | None:
    """Extracts human-readable EXIF metadata from an image file."""
    path = Path(image_path)
    
    if not path.is_file():
        print(f"[-] Error: File not found at '{path}'.")
        return None

    try:
        # Use context manager to properly manage file resources
        with Image.open(path) as image:
            exif_data = image._getexif()

        print(f"\n[+] Metadata for: {path}")
        print("-" * 45)

        if not exif_data:
            print("[-] No EXIF metadata found in this image.")
            return None

        metadata = {}
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            metadata[tag_name] = value
            print(f"{str(tag_name):25}: {value}")

        return metadata

    except Exception as e:
        print(f"[-] An error occurred: {e}")
        return None