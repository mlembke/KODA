# -*- coding: utf-8 -*-
import numpy as np
import itertools

from PIL import Image

def encode_predictive(image, opt):
    width = image.size[0]
    height = image.size[1]
    pix = np.array(image, dtype='int64')
    pix_diff = np.copy(pix)
    for j in range(0, height):
        for i in range(0, width):
            # lewy sasiad
            if (opt == 1) and (j > 0):
                pix_diff[i, j] = pix[i, j] - pix[i, j - 1]
            # gorny sasiad
            if (opt == 2) and (i > 0):
                pix_diff[i, j] = pix[i, j] - pix[i - 1, j]
            # medianowe
            if (opt == 3) and (i > 0) and (j > 0):
                pix_diff[i, j] = np.median([(pix[i, j] - pix[i - 1, j]), (pix[i, j] - pix[i, j - 1]),
                                            (pix[i, j] - pix[i - 1, j - 1])])
    return pix_diff.flatten()
