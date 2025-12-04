#!/usr/bin/env python3
"""
Download Noto Emoji Animated GIFs from Google Fonts

This script downloads all animated Noto Emoji GIFs from the official
Google Fonts Noto Emoji Animation project.

Usage:
    python3 download_emojis.py [--output-dir OUTPUT_DIR] [--size SIZE]

Arguments:
    --output-dir: Directory to save downloaded GIFs (default: emojis)
    --size: Size of GIFs to download - 512, 256, or 128 (default: 512)
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import List, Tuple
import urllib.request
import urllib.error


API_URL = "https://googlefonts.github.io/noto-emoji-animation/data/api.json"
BASE_URL = "https://fonts.gstatic.com/s/e/notoemoji/latest/{codepoint}/{size}.gif"


def fetch_emoji_list() -> List[Tuple[str, str]]:
    """
    Fetch the list of available emojis from the API.
    
    Returns:
        List of tuples containing (codepoint, name) for each emoji
    """
    print(f"Fetching emoji list from {API_URL}...")
    try:
        with urllib.request.urlopen(API_URL) as response:
            data = json.loads(response.read().decode())
        
        emojis = []
        for icon in data.get('icons', []):
            codepoint = icon.get('codepoint', '')
            # Get the first tag as the name, removing brackets
            tags = icon.get('tags', [])
            if tags and len(tags) > 0:
                name = tags[0].strip('[]')
            else:
                name = codepoint
            
            if codepoint:
                emojis.append((codepoint, name))
        
        print(f"Found {len(emojis)} emojis")
        return emojis
    
    except urllib.error.URLError as e:
        print(f"Error fetching emoji list: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing API response: {e}")
        sys.exit(1)


def download_emoji(codepoint: str, name: str, output_dir: Path, size: int = 512) -> bool:
    """
    Download a single emoji GIF.
    
    Args:
        codepoint: The Unicode codepoint of the emoji
        name: The name/tag of the emoji
        output_dir: Directory to save the GIF
        size: Size of the GIF (512, 256, or 128)
    
    Returns:
        True if download was successful, False otherwise
    """
    url = BASE_URL.format(codepoint=codepoint, size=size)
    # Create a safe filename
    filename = f"{name}_{codepoint}.gif"
    # Replace any characters that might be problematic in filenames
    filename = "".join(c if c.isalnum() or c in "._- " else "_" for c in filename)
    filepath = output_dir / filename
    
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
        
        with open(filepath, 'wb') as f:
            f.write(content)
        
        return True
    
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"  ⚠️  Not found: {name} ({codepoint})")
        else:
            print(f"  ❌ HTTP Error {e.code}: {name} ({codepoint})")
        return False
    
    except urllib.error.URLError as e:
        print(f"  ❌ URL Error: {name} ({codepoint}) - {e}")
        return False
    
    except Exception as e:
        print(f"  ❌ Error downloading {name} ({codepoint}): {e}")
        return False


def create_metadata(emojis: List[Tuple[str, str]], output_dir: Path, size: int):
    """
    Create a metadata JSON file with information about downloaded emojis.
    
    Args:
        emojis: List of (codepoint, name) tuples
        output_dir: Directory where the metadata file will be saved
        size: Size of downloaded GIFs
    """
    metadata = {
        "source": "Google Fonts Noto Emoji Animation",
        "source_url": "https://googlefonts.github.io/noto-emoji-animation/",
        "total_emojis": len(emojis),
        "gif_size": size,
        "emojis": [
            {
                "codepoint": codepoint,
                "name": name,
                "filename": f"{name}_{codepoint}.gif".replace(" ", "_")
            }
            for codepoint, name in emojis
        ]
    }
    
    metadata_path = output_dir / "metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Metadata saved to {metadata_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Download Noto Emoji Animated GIFs from Google Fonts"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="emojis",
        help="Directory to save downloaded GIFs (default: emojis)"
    )
    parser.add_argument(
        "--size",
        type=int,
        choices=[512, 256, 128],
        default=512,
        help="Size of GIFs to download (default: 512)"
    )
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    
    print("=" * 70)
    print("Noto Emoji Animated GIFs Downloader")
    print("=" * 70)
    print(f"Output directory: {output_dir.absolute()}")
    print(f"GIF size: {args.size}x{args.size} pixels")
    print("=" * 70)
    print()
    
    # Fetch emoji list
    emojis = fetch_emoji_list()
    
    # Download emojis
    print(f"\nDownloading {len(emojis)} emojis...")
    print("-" * 70)
    
    successful = 0
    failed = 0
    
    for i, (codepoint, name) in enumerate(emojis, 1):
        print(f"[{i}/{len(emojis)}] {name} ({codepoint})...", end=" ")
        
        if download_emoji(codepoint, name, output_dir, args.size):
            print("✅")
            successful += 1
        else:
            failed += 1
        
        # Add a small delay to be respectful to the server
        time.sleep(0.1)
    
    # Create metadata file
    create_metadata(emojis, output_dir, args.size)
    
    # Summary
    print("\n" + "=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"✅ Successfully downloaded: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"📁 Saved to: {output_dir.absolute()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
