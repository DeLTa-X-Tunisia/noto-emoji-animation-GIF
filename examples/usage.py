#!/usr/bin/env python3
"""
Example: Using Noto Emoji Animated GIFs in Python

This script demonstrates how to work with the downloaded emoji GIFs
and metadata in your Python projects.
"""

import json
from pathlib import Path
from typing import List, Dict, Optional


def load_emoji_metadata(metadata_path: str = "emojis/metadata.json") -> Dict:
    """
    Load emoji metadata from the JSON file.
    
    Args:
        metadata_path: Path to the metadata.json file
        
    Returns:
        Dictionary containing emoji metadata
    """
    with open(metadata_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_emoji_by_name(metadata: Dict, search_term: str) -> List[Dict]:
    """
    Find emojis by searching their names.
    
    Args:
        metadata: Emoji metadata dictionary
        search_term: Term to search for in emoji names
        
    Returns:
        List of emoji dictionaries matching the search term
    """
    return [
        emoji for emoji in metadata['emojis']
        if search_term.lower() in emoji['name'].lower()
    ]


def find_emoji_by_codepoint(metadata: Dict, codepoint: str) -> Optional[Dict]:
    """
    Find an emoji by its Unicode codepoint.
    
    Args:
        metadata: Emoji metadata dictionary
        codepoint: Unicode codepoint (e.g., "1f600")
        
    Returns:
        Emoji dictionary if found, None otherwise
    """
    for emoji in metadata['emojis']:
        if emoji['codepoint'] == codepoint:
            return emoji
    return None


def get_emoji_path(emoji: Dict, base_dir: str = "emojis") -> Path:
    """
    Get the full path to an emoji GIF file.
    
    Args:
        emoji: Emoji dictionary with filename
        base_dir: Base directory where emojis are stored
        
    Returns:
        Path object pointing to the emoji file
    """
    return Path(base_dir) / emoji['filename']


def list_all_emojis(metadata: Dict) -> None:
    """
    Print a list of all available emojis.
    
    Args:
        metadata: Emoji metadata dictionary
    """
    print(f"Total emojis: {metadata['total_emojis']}")
    print(f"GIF size: {metadata['gif_size']}px")
    print(f"Source: {metadata['source']}")
    print("\nEmojis:")
    print("-" * 60)
    
    for i, emoji in enumerate(metadata['emojis'], 1):
        print(f"{i}. {emoji['name']} (U+{emoji['codepoint']})")
        if i >= 10:  # Just show first 10 for brevity
            print(f"... and {metadata['total_emojis'] - 10} more")
            break


def main():
    """Example usage of emoji functions."""
    
    # Check if metadata exists
    metadata_path = "emojis/metadata.json"
    if not Path(metadata_path).exists():
        print("❌ Metadata file not found!")
        print("Please run: python3 download_emojis.py")
        return
    
    # Load metadata
    print("Loading emoji metadata...")
    metadata = load_emoji_metadata(metadata_path)
    print(f"✅ Loaded {len(metadata['emojis'])} emojis\n")
    
    # Example 1: Find emojis by name
    print("=" * 60)
    print("Example 1: Find emojis with 'heart' in the name")
    print("=" * 60)
    heart_emojis = find_emoji_by_name(metadata, "heart")
    for emoji in heart_emojis[:5]:  # Show first 5
        print(f"  - {emoji['name']} ({emoji['codepoint']})")
        print(f"    File: {emoji['filename']}")
    print()
    
    # Example 2: Find specific emoji by codepoint
    print("=" * 60)
    print("Example 2: Find emoji by codepoint")
    print("=" * 60)
    emoji = find_emoji_by_codepoint(metadata, "1f600")
    if emoji:
        print(f"  Found: {emoji['name']}")
        print(f"  Codepoint: U+{emoji['codepoint']}")
        print(f"  File: {emoji['filename']}")
        emoji_path = get_emoji_path(emoji)
        print(f"  Path: {emoji_path}")
        print(f"  Exists: {emoji_path.exists()}")
    print()
    
    # Example 3: List all emojis (first 10)
    print("=" * 60)
    print("Example 3: List available emojis")
    print("=" * 60)
    list_all_emojis(metadata)
    print()
    
    # Example 4: Search for specific categories
    print("=" * 60)
    print("Example 4: Find emojis by category")
    print("=" * 60)
    categories = ["smile", "animal", "food", "flag"]
    for category in categories:
        results = find_emoji_by_name(metadata, category)
        print(f"  {category.title()}: {len(results)} emojis found")
    print()
    
    print("=" * 60)
    print("✨ Examples completed!")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. Use get_emoji_path() to get file paths")
    print("  2. Load GIFs in your application")
    print("  3. Display them in your UI or export to other formats")


if __name__ == "__main__":
    main()
