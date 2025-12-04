# Noto Emoji Animated GIFs Collection 🎉

A complete collection of animated Noto Emoji GIFs from the official [Google Fonts Noto Emoji Animation project](https://googlefonts.github.io/noto-emoji-animation/).

This repository makes it easy for developers, designers, and creators to access and use animated Noto Emojis without needing to manually fetch them from the source site.

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Quick Start](#quick-start)
- [Download Script](#download-script)
- [Repository Structure](#repository-structure)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

## 🎯 About

Noto Emoji is Google's open-source emoji font and animation library. This repository provides:

- **Easy Access**: Download all animated GIFs with a single script
- **Organized Collection**: Properly named and structured emoji files
- **Metadata**: JSON file with emoji information and codepoints
- **Multiple Sizes**: Support for 512px, 256px, and 128px GIFs
- **Up-to-date**: Simple script to fetch the latest emojis from Google

## ✨ Features

- 🚀 **One-command download** of all animated Noto Emojis
- 📦 **Python script** with no complex dependencies
- 🏷️ **Metadata file** with emoji names and codepoints
- 🎨 **Multiple size options** (512px, 256px, 128px)
- 📝 **Clean naming convention** for easy file management
- ⚡ **Fast and efficient** downloading with progress tracking

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Internet connection

### Installation

1. Clone this repository:
```bash
git clone https://github.com/DeLTa-X-Tunisia/noto-emoji-animation-GIF.git
cd noto-emoji-animation-GIF
```

2. Run the download script:
```bash
python3 download_emojis.py
```

That's it! All animated emoji GIFs will be downloaded to the `emojis` directory.

## 📥 Download Script

### Basic Usage

```bash
python3 download_emojis.py
```

This downloads all emojis in 512px size to the `emojis` directory.

### Advanced Options

```bash
# Download to a custom directory
python3 download_emojis.py --output-dir my_emojis

# Download smaller size (256px or 128px)
python3 download_emojis.py --size 256

# Combine options
python3 download_emojis.py --output-dir assets/emojis --size 512
```

### Script Options

| Option | Default | Description |
|--------|---------|-------------|
| `--output-dir` | `emojis` | Directory to save downloaded GIFs |
| `--size` | `512` | GIF size: 512, 256, or 128 pixels |
| `--help` | - | Show help message |

## 📁 Repository Structure

```
noto-emoji-animation-GIF/
├── README.md                 # This file
├── download_emojis.py        # Download script
├── LICENSE                   # License information
└── emojis/                   # Downloaded emojis (after running script)
    ├── metadata.json         # Emoji metadata and information
    ├── grinning_face_1f600.gif
    ├── smiling_face_with_hearts_1f970.gif
    └── ...                   # All other emoji GIFs
```

## 💡 Usage Examples

### In Web Projects

```html
<!-- Use in HTML -->
<img src="emojis/grinning_face_1f600.gif" alt="Grinning Face" width="64" height="64">
```

```css
/* Use in CSS */
.emoji-background {
    background-image: url('emojis/smiling_face_with_hearts_1f970.gif');
}
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
    if 'heart' in emoji['name'].lower():
        print(f"Found: {emoji['name']} - {emoji['filename']}")
```

### In React/Next.js

```jsx
import Image from 'next/image';

function MyComponent() {
  return (
    <Image 
      src="/emojis/grinning_face_1f600.gif" 
      alt="Grinning Face"
      width={64}
      height={64}
    />
  );
}
```

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

- Report bugs or issues
- Suggest new features or improvements
- Submit pull requests
- Improve documentation

## 📄 License

This repository's code is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

**Note**: The Noto Emoji animations themselves are created by Google and are licensed under the [Apache License 2.0](https://github.com/googlefonts/noto-emoji/blob/main/LICENSE). Please review Google's license terms for the emoji content.

## 🙏 Credits

- **Google Fonts Team**: For creating and maintaining the [Noto Emoji Animation project](https://googlefonts.github.io/noto-emoji-animation/)
- **Noto Emoji**: Original font and emoji designs by Google
- **Community**: Thanks to all contributors and users of this repository

## 🔗 Related Resources

- [Official Noto Emoji Animation Hub](https://googlefonts.github.io/noto-emoji-animation/)
- [Noto Emoji GitHub Repository](https://github.com/googlefonts/noto-emoji)
- [Google Fonts](https://fonts.google.com/)

---

**Made with ❤️ by the open-source community**

If you find this repository useful, please ⭐ star it and share it with others!
