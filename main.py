import numpy as np

import HuffmanCodec
import ImageGenerator
import PredictiveCodec

def main():
    image = ImageGenerator.generate_uniform('out.bmp')
    data = PredictiveCodec.encode_predictive(image,1)
    #data = np.array(image).flatten()
    #print(data)
    code_book = HuffmanCodec.generate_huffman_code_book(data)
    code = HuffmanCodec.encode(data, code_book)
    with open('out.bin', 'wb') as f:
        f.write(code)


if __name__ == '__main__':
    main()
