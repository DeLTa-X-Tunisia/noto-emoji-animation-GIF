# Usage Guide

## Downloading Emojis

### Quick Start

The simplest way to get started:

```bash
python3 download_emojis.py
```

This will download all animated Noto Emojis (512px size) to the `emojis` directory.

### Command-Line Options

#### Output Directory

Specify where to save the emoji GIFs:

```bash
python3 download_emojis.py --output-dir my_emojis
```

#### GIF Size

Choose the size of emoji GIFs to download:

```bash
# Download 512px GIFs (default, highest quality)
python3 download_emojis.py --size 512

# Download 256px GIFs (medium quality, smaller files)
python3 download_emojis.py --size 256

# Download 128px GIFs (low quality, smallest files)
python3 download_emojis.py --size 128
```

#### Combining Options

```bash
python3 download_emojis.py --output-dir assets/emojis --size 256
```

## Understanding the Output

After running the script, you'll have:

### Directory Structure

```
emojis/
├── metadata.json                          # Complete emoji catalog
├── grinning_face_1f600.gif               # Individual emoji GIFs
├── smiling_face_with_hearts_1f970.gif
├── party_popper_1f389.gif
└── ... (1500+ more emojis)
```

### Metadata File

The `metadata.json` file contains:

```json
{
  "source": "Google Fonts Noto Emoji Animation",
  "source_url": "https://googlefonts.github.io/noto-emoji-animation/",
  "total_emojis": 1500,
  "gif_size": 512,
  "emojis": [
    {
      "codepoint": "1f600",
      "name": "grinning face",
      "filename": "grinning_face_1f600.gif"
    }
  ]
}
```

## Using the Emojis

### In HTML

```html
<img src="emojis/grinning_face_1f600.gif" alt="Grinning Face" width="64" height="64">
```

### In CSS

```css
.emoji-icon {
    background-image: url('emojis/party_popper_1f389.gif');
    background-size: contain;
    width: 64px;
    height: 64px;
}
```

### In JavaScript

```javascript
// Load emoji dynamically
const emojiImg = new Image();
emojiImg.src = 'emojis/smiling_face_with_hearts_1f970.gif';
emojiImg.alt = 'Smiling Face with Hearts';
document.getElementById('emoji-container').appendChild(emojiImg);
```

### In Python

```python
import json
from pathlib import Path

# Load metadata
with open('emojis/metadata.json', 'r') as f:
    metadata = json.load(f)

# Find specific emoji
for emoji in metadata['emojis']:
    if 'heart' in emoji['name']:
        print(f"{emoji['name']}: {emoji['filename']}")
```

### In React

```jsx
function EmojiComponent() {
  return (
    <img 
      src="/emojis/grinning_face_1f600.gif" 
      alt="Grinning Face"
      width={64}
      height={64}
    />
  );
}
```

## Finding Specific Emojis

### By Name

Search the metadata for emojis by name:

```python
import json

with open('emojis/metadata.json', 'r') as f:
    data = json.load(f)

# Find all heart emojis
hearts = [e for e in data['emojis'] if 'heart' in e['name'].lower()]
for emoji in hearts:
    print(f"{emoji['name']}: {emoji['filename']}")
```

### By Unicode Codepoint

If you know the Unicode codepoint:

```python
import json

with open('emojis/metadata.json', 'r') as f:
    data = json.load(f)

# Find emoji by codepoint
codepoint = "1f600"
emoji = next((e for e in data['emojis'] if e['codepoint'] == codepoint), None)
if emoji:
    print(f"Found: {emoji['filename']}")
```

## Updating the Collection

To get the latest emojis from Google:

```bash
# Remove old emojis
rm -rf emojis/

# Download fresh copy
python3 download_emojis.py
```

## File Naming Convention

Emoji files follow this naming pattern:

```
{emoji_name}_{unicode_codepoint}.gif
```

Examples:
- `grinning_face_1f600.gif`
- `red_heart_2764.gif`
- `thumbs_up_1f44d.gif`

## Troubleshooting

### Network Issues

If downloads fail:
- Check your internet connection
- Verify the Google Fonts API is accessible
- Try again after a few minutes (rate limiting)

### Missing Emojis

Some emojis might not be available in animated form. The script will report which ones couldn't be downloaded.

### Large Downloads

The complete collection is substantial:
- 512px: ~150-200 MB
- 256px: ~50-75 MB
- 128px: ~20-30 MB

Consider your storage and bandwidth limitations.

## Advanced Usage

### Batch Processing

Process multiple emoji files:

```python
from pathlib import Path

emoji_dir = Path('emojis')
for gif in emoji_dir.glob('*.gif'):
    # Process each GIF
    print(f"Processing {gif.name}")
```

### Integration with Web Frameworks

#### Flask

```python
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/emojis/<path:filename>')
def serve_emoji(filename):
    return send_from_directory('emojis', filename)
```

#### Express.js

```javascript
const express = require('express');
const app = express();

app.use('/emojis', express.static('emojis'));
```

## Examples

Check the `examples/` directory for:
- `usage.py` - Python usage examples
- `usage.html` - HTML/CSS/JavaScript examples
- `metadata_sample.json` - Sample metadata structure

## Need Help?

- Check [README.md](README.md) for more information
- Open an issue on GitHub
- Review the [CONTRIBUTING.md](CONTRIBUTING.md) guide
