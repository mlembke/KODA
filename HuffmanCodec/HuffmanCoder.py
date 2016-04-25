import array

import numpy as np

import HuffmanCodec.HuffmanTree as HT

__BYTE = 8


class HuffmanCode(object):
    def __init__(self, encoded_data, code_book):
        self.encoded_data = encoded_data
        self.code_book = code_book

    def write_to_file(self, file_name):
        pass

    def load_from_file(self, file_name):
        pass


def encode(data):
    huffman_tree = HT.build_tree(data)
    code_book = huffman_tree.generate_code_book()
    encoded_data = array.array('B')
    buffer = 0
    length = 0
    for symbol in data:
        code_word = code_book[symbol]
        for bit in code_word:
            if bit == '1':
                buffer = (buffer << 1) | 0x01
            else:
                buffer = (buffer << 1)
            length += 1
            if length == __BYTE:
                encoded_data.extend([buffer])
                buffer = 0
                length = 0
    if length != 0:
        encoded_data.extend([buffer << (__BYTE - length)])
        # [0] - encoded_data
        # [1] - code_book
    return encoded_data, code_book # zwracane jako tuple, poniewaz python narzeka na obiekt


def encode_alt(data):
    huffman_tree = HT.build_tree(data)
    code_book = huffman_tree.generate_code_book()
    encoded_data = []
    buffer = 0
    length = 0
    for symbol in data:
        code_word = code_book[symbol]
        for bit in code_word:
            if bit == '1':
                buffer = (buffer << 1) | 0x01
            else:
                buffer = (buffer << 1)
            length += 1
            if length == __BYTE:
                encoded_data.extend([buffer])
                buffer = 0
                length = 0
    if length != 0:
        encoded_data.extend([buffer << (__BYTE - length)])
    return HuffmanCode(np.asanyarray(encoded_data, dtype=bytes), code_book)
