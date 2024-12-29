# AmbientCG Library Downloader

A Python-based tool to download and create your own local AmbientCG library. This tool allows you to specify asset parameters : type of asset, resolution... and save them.

The ambientcg.com site contains more than +15000 assets.

All ambientCG assets are provided under the Creative Commons CC0 1.0 Universal License.
This applies to the downloadable asset files and the material preview renders shown for each asset on the site.

---

## Features

- **Asset Filtering**: Filter assets based on resolution, type, and more.
- **Validation**: Validate user-defined parameters against predefined allowed values.
- **Batch Downloading**: Download multiple assets simultaneously.
- **File Management**: Organize downloaded assets in folders and manage file extensions.

---

## Requirements

- Python 3.7+
- Modules:
  - `requests`
  - `urllib`
  - `mimetypes`
  - `zipfile`
  - `logging`

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Agorgext/ambientcg-downloader.git
cd ambientcg-downloader
```

2. Update parameters directly in the script (parameters.py) for your needs.

3. Run the script:
```bash
python main.py
```

## License
Created using assets from ambientCG.com, licensed under the Creative Commons CC0 1.0 Universal License.

The current code and content follow the same licence.
