def run_length_encode(data):
    if not data:
        return ""

    compressed = []
    count = 1
    last_char = data[0]

    for char in data[1:]:
        if char == last_char:
            count += 1
        else:
            compressed.append(last_char + str(count))
            count = 1
            last_char = char

    compressed.append(last_char + str(count))  # Append the last set of data
    return ''.join(compressed)

def compress_encoded_image(image_string):
    width = image_string[0]
    height = image_string[1]
    data = image_string[2:]
    
    # Apply RLE to only the data part
    compressed_data = run_length_encode(data)
    
    # Combine width, height, and compressed data
    return width + height + compressed_data

# Example Usage:
encodedImage = "43111111111111"
compressedImage = compress_encoded_image(encodedImage)
print("Original:", encodedImage)
print("Compressed:", compressedImage)
