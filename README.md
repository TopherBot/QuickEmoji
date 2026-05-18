# QuickEmoji 🚀

**QuickEmoji** is a lightweight, zero‑dependency Python CLI tool that parses a string and replaces recognised keywords with emojis.

## Features
- Simple command‑line interface.
- Extensible keyword‑to‑emoji mapping.
- Works on Windows, macOS, and Linux.
- No external libraries required.

## Installation
```bash
# Clone the repo
git clone https://github.com/yourusername/quickemoji.git
cd quickemoji

# Make the script executable (optional)
chmod +x quickemoji.py
```

## Usage
```bash
# Basic usage
python quickemoji.py "I love python and coffee"

# Or, if you made it executable
./quickemoji.py "Happy birthday to you"
```

**Output**:
```
I ❤️ 🐍 and ☕
Happy 🎂 to you
```

## Extending the Mapping
Edit the `EMOJI_MAP` dictionary in `quickemoji.py` to add or modify keyword‑emoji pairs.

## Contributing
Feel free to open issues or submit pull requests. All contributions are welcome!

## License
This project is licensed under the MIT License – see the `LICENSE` file for details.
