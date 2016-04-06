import numpy as np

import HuffmanCodec
import ImageGenerator


def main():
    image = ImageGenerator.generate_gaussian('out.bmp')
    data = np.array(image).flatten()
    code_book = HuffmanCodec.generate_huffman_code_book(data)
    code = HuffmanCodec.encode(data, code_book)
    with open('out.bin', 'wb') as f:
        f.write(code)


if __name__ == '__main__':
    main()
