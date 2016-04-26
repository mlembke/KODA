# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

output_decode = "decoded/"

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


class PredictiveCodec(object):

    def __init__(self, image_name, image):
        self.image_name = image_name
        image = image.convert('L')
        self.image = image
        self.width = image.size[0]
        self.height = image.size[1]
        self.encoded_data = [] # 4-elementowa tablica przechowująca zakodowane dane
        self.decoded_data = []

    def encode_predictive(self):
        for opt in range(0,4):

            if opt == 0:
                self.encoded_data.append((np.array(self.image, dtype='int64')).flatten())
                continue

            pix = np.array(self.image, dtype='int64')
            pix_diff = np.copy(pix)
            for j in range(0, self.width):
                for i in range(0, self.height):
                    # lewy sasiad
                    # if (opt == 1) and (j > 0):
                    if opt == 1:
                        if j > 0:
                            pix_diff[i, j] = pix[i, j] - pix[i, j - 1]
                        else:
                            pix_diff[i, j] = pix[i, j] - 128
                    # gorny sasiad
                    if opt == 2:
                        if i > 0:
                            pix_diff[i, j] = pix[i, j] - pix[i - 1, j]
                        else:
                            pix_diff[i, j] = pix[i, j] - 128
                    # medianowe
                    # michał: ta operacja (np.median) jest bardzo kosztowna obliczeniowo
                    # MJK: mowisz-masz :p
                    if opt == 3:
                        if (i > 0) and (j > 0):
                            pix_diff[i, j] = pix[i, j] - mid(pix[i - 1, j], pix[i, j - 1], pix[i - 1, j - 1])
                        else:
                            pix_diff[i, j] = pix[i, j] - 128 # mediana z 128, 128, x to zawsze 128.

            self.encoded_data.append(pix_diff.flatten())

    # input: 4-elementowa tablica 1D wejsciowa
    def decode_predictive(self,data):
        for opt in range(0,3):
            if opt == 0:
                self.decoded_data.append(data[0])
                continue

            pred_data = np.copy(data[opt])
            for i in range(0, self.width * self.height):
                if opt == 1:
                    if (i + self.width) % self.width > 0:
                        pred_data[i] = data[opt][i] + pred_data[i - 1]
                    else:
                        pred_data[i] = data[opt][i] + 128
                if opt == 2:
                    if i > self.width - 1:
                        pred_data[i] = data[opt][i] + pred_data[i - self.width]
                    else:
                        pred_data[i] = data[opt][i] + 128

            self.decoded_data.append(pred_data)

    def save_decoded(self):
        imgs = []
        for opt in range(0,3):
            im = Image.new("L", (self.width, self.height))
            im.putdata(self.decoded_data[opt])
            im.convert("RGB")
            imgs.append(im)
            im.save(output_decode + self.image_name + "_" + str(opt) + "_decoded.png","PNG")
