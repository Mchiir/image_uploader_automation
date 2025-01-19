# MQTT Image Uploader

**Version**: 1.0.0  
**Author**: Mr. Mchrispin  
**Project**: Automated Image Uploading via MQTT  

The **MQTT Image Uploader** is a Python script designed to automatically upload images from a local directory to a specified remote server using HTTP POST requests. The script monitors the `src` directory for new images, uploads them, and moves them to a `dist` directory once uploaded. The script uses `curl` to handle the HTTP POST requests for image uploads.

## Features

- Automatically monitors a local `src` directory for `.jpg` files.
- Uploads images to a specified remote server via HTTP POST.
- Moves successfully uploaded images to a `dist` directory.
- Ensures the `src` and `dist` directories are created if they do not already exist.
- Logs success and error messages with timestamps for better traceability.

## Requirements

- Python 3.x
- `curl` command-line tool (used for uploading images via HTTP)
- Required Python libraries: `os`, `time`, `subprocess`, `logging`, `signal`, `sys`

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/yourusername/mqtt-image-uploader.git

2. Navigate to the base folder:
   ```bash
   cd MQTT-IMAGE-UPLOADER-AUTOMATION

3. Run the script:
   ```bash
   python app.py

## Enjoy the outcome!!