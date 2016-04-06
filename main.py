import numpy as np

import HuffmanCodec.HuffmanCoder as Coder
import ImageGenerator


def main():
    image = ImageGenerator.generate_gaussian()
    data = np.array(image).flatten()
    code = Coder.encode_alt(data)
    print(code.code_book)
    print(code.encoded_data)


if __name__ == '__main__':
    main()
