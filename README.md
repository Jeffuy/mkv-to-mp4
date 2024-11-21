# MKV Converter

## Overview

This project is a simple command-line tool for converting MKV files to MP4 using the FFmpeg library. It provides a user-friendly interface to specify the input directory and output file format.

## Usage

To use this tool, simply run the `run.bat` script in the command line and follow the prompts:

1. Enter the path to the directory containing the MKV files you want to convert.
2. The tool will automatically convert all `.mkv` files in that directory to MP4 format.
3. The converted files will be saved in the same directory with the MP4 extension.

## Contributing

Contributions are welcome! To contribute, please follow these guidelines:

* Create a new branch for your feature or bug fix: `git checkout -b new-feature`
* Make changes to the code and commit them: `git add .` and `git commit -m "Brief description of changes"`
* Push your changes to the remote repository: `git push origin new-feature`
* Open a pull request against the main branch (`master`)

## Configuration

The tool uses a few configuration files:

* `.env`: contains environment variables for the conversion process
* `secrets.json`: contains sensitive information, such as API keys or encryption keys
* `keys.json`: contains private keys for encryption or decryption

These files should be managed carefully to ensure security and data integrity.

## Technical Requirements

This project relies on:

* Python 3.x
* FFmpeg library (version 4.2 or higher)
* Windows command line interface (for the `run.bat` script)

Please note that this is a basic implementation, and you may need to modify it to suit your specific use case.

## Known Issues

None known at this time. However, please report any issues or bugs you encounter during usage.