# -*- coding: utf-8 -*-
from collections import Counter
from heapq import heappush, heappop, heapify
from itertools import zip_longest

import numpy as np


def encode(data, code_book):
    """
    Encode the one-dimensional numpy.array of values using given code book

    This function computes the one-dimensional numpy.array of bytes based on input code book.

    :param data: array_like
        one-dimensional input array of values to encode
    :param code_book:  dictionary
        dictionary for mapping values to codes
    :return: numpy.array
        one-dimensional numpy.array of bytes represents encoded data
    """
    return np.array([int(chunk, 2).to_bytes(-(-len(chunk) // 8), byteorder='big') for chunk in
                     map(lambda tup: ''.join(tup), (lambda iterable: zip_longest(*[iter(iterable)] * 8, fillvalue=''))(
                         ''.join(map(lambda x: code_book[x], data))))])


def generate_huffman_code_book(data):
    """
    Generates code book using Huffman coding
    :param data: one-dimensional numpy.array of values
    :return: dictionary
    """
    frequencies = Counter(data)
    heap = [[weight, [symbol, '']] for symbol, weight in frequencies.items()]
    heapify(heap)
    while len(heap) > 1:
        low = heappop(heap)
        high = heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return dict(sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))


def decode(code, codebook):
    pass
