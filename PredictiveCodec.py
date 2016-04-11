# -*- coding: utf-8 -*-
import numpy as np
import itertools

from PIL import Image


def mid(a, b, c):
    if a < b:
        if b < c:
            return b
        else:
            if a < c:
                return c
            else:
                return a
    else:
        if b < c:
            if a < c:
                return a
            else:
                return c
        else:
            return b


def encode_predictive(image, opt):
    width = image.size[0]
    height = image.size[1]
    image = image.convert('L')
    pix = np.array(image, dtype='int64')
    pix_diff = np.copy(pix)
    for j in range(0, width):
        for i in range(0, height):
            # lewy sasiad
            if (opt == 1) and (j > 0):
                pix_diff[i, j] = pix[i, j] - pix[i, j - 1]
            # gorny sasiad
            if (opt == 2) and (i > 0):
                pix_diff[i, j] = pix[i, j] - pix[i - 1, j]
            # medianowe
            # michał: ta operacja (np.median) jest bardzo kosztowna obliczeniowo
            # MJK: mowisz-masz :p
            if (opt == 3) and (i > 0) and (j > 0):
                pix_diff[i, j] = mid((pix[i, j] - pix[i - 1, j]), (pix[i, j] - pix[i, j - 1]), (pix[i, j] - pix[i - 1, j - 1]))
                # pix_diff[i, j] = np.median([(pix[i, j] - pix[i - 1, j]), (pix[i, j] - pix[i, j - 1]),
                #                             (pix[i, j] - pix[i - 1, j - 1])])
    return pix_diff.flatten()
