import numpy as np

import HuffmanCodec.HuffmanCoder as coder
import ImageGenerator as igen

__BYTE = 8


def decode(code):
    buffer = []
    total_length = 0
    node = code.huffman_tree.root
    for chunk in code.encoded_data:
        buffer_size = 0
        while buffer_size < __BYTE and total_length < code.code_length:
            buffer_size += 1
            total_length += 1
            if chunk >> (__BYTE - buffer_size) & 1:
                node = node.right
            else:
                node = node.left
            if node.symbol is not None:
                buffer.append(node.symbol)
                node = code.huffman_tree.root
    return buffer


def main():
    image = igen.generate_gaussian()
    data = np.array(image).flatten()
    code = coder.encode(data)
    decoded_data = decode(code)
    print(data == decoded_data)


if __name__ == '__main__':
    main()
