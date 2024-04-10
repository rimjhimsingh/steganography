# BMP Steganography Decoder
This project provides a Python implementation for extracting hidden steganographic information from BMP image files. The program reads a BMP file, identifies the presence of hidden data, and extracts this data based on specific rules outlined in the assignment specifications.

## Features
- Reads BMP files and ignores the first 100 bytes.
- Searches for a marker indicating the presence of hidden data.
- Extracts the size of the hidden data and the data itself.
- Outputs the extracted data to a specified file.

## Usage
To use this program, run the following command in your terminal:

python steganography_decoder.py input_file.bmp output_file

**input_file.bmp:** The BMP file from which you want to extract hidden data.
**output_file:** The file where the extracted data will be saved.

## Requirements
Python 3

## Example
Given a BMP file named sample.bmp with hidden data, you can extract the data and save it to output.txt using the following command:

python steganography_decoder.py sample.bmp output.txt
Check output.txt to view the extracted hidden data.

## Implementation Details
The program uses the least significant bit (LSB) method to extract hidden data from the BMP file.
It checks for a marker of 64 bits where each interpreted byte is the hexadecimal value 0xa5 to confirm the presence of hidden data.
The size of the hidden data is represented by the next 27 bits, and the actual data follows this size indicator.
