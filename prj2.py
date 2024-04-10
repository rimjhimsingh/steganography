import sys

def read(file_path):
    with open(file_path, 'rb') as f:
        byte_data = f.read()
        return byte_data

def uncover_steganography(input_file, output_file):
    if not input_file.lower().endswith('.bmp'):
        print("Error: Input file must be a BMP file.")
        sys.exit(1)
    byte_data = read(input_file)
    
    # Ignore the first 100 bytes of data
    byte_data = byte_data[100:]

    # Extract the least significant bit (LSB) from the next 64 bytes
    marker = ''.join(str(byte & 1) for byte in byte_data[:64])

    # Convert the hexadecimal value 0xa5 into an 8-bit binary string
    indicator_byte = format(0xa5, '08b')

    # Repeat the indicator byte 8 times to form a 64-bit string
    indicator_bits = indicator_byte * 8

    # Compare marker with the indicator bits and proceed or raise an error
    if marker == indicator_bits:
        print("marker matches the indicator bits. There is hidden data in your input file")
    else:
        print("marker does not match the indicator bits. No hidden data found")

    byte_data = byte_data[64:]

    size_hidden = ''.join(str(byte & 1) for byte in byte_data[:27])
    size_hidden_int = int(size_hidden[::-1], 2)
    print(size_hidden_int)
    byte_data = byte_data[27:]
    extracted_data = ''.join(str(byte & 1) for byte in byte_data[:size_hidden_int * 8])
    hidden_data = bytes(int(extracted_data[i:i + 8][::-1], 2) for i in range(0, len(extracted_data), 8))
    
    with open(output_file, "wb") as f:
        f.write(hidden_data)

    print("Check this output file to view the hidden data:", output_file)

def main():
    if len(sys.argv) != 3:
        print("Usage: python prj2.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    uncover_steganography(input_file, output_file)

if __name__ == "__main__":
    main()
