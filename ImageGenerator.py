# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

__min_value = 0
__max_value = 255


def __scale_samples(data):
    data_max = max(data)
    data_min = min(data)
    scaled = ((data - data_min) / (data_max - data_min)) * (__max_value - __min_value) + __min_value
    return scaled


def __save_image(file_name, data, image_width, image_height):
    image = Image.new('L', (image_width, image_height))
    image.putdata(data)
    if file_name:
        image.save(file_name)
    return image


def generate_gaussian(file_name='', mu=0, sigma=1, image_width=512, image_height=512):
    data = __scale_samples(np.random.normal(mu, sigma, image_width * image_height))
    return __save_image(file_name, data, image_width, image_height)


def generate_laplace(file_name='', mu=0, decay=1, image_width=512, image_height=512):
    data = __scale_samples(np.random.laplace(mu, decay, image_width * image_height))
    return __save_image(file_name, data, image_width, image_height)


def generate_uniform(file_name='', image_width=512, image_height=512):
    data = np.random.randint(__min_value, __max_value + 1, size=image_width * image_height)
    return __save_image(file_name, data, image_width, image_height)


def __self_test():
    uniform = generate_uniform()
    gaussian = generate_gaussian()
    laplace = generate_laplace()
    plt.subplot(1, 3, 1)
    plt.plot(uniform.histogram(), color='blue', linewidth=2.0)
    plt.title('Uniform')
    plt.subplot(1, 3, 2)
    plt.plot(gaussian.histogram(), color='red', linewidth=2.0)
    plt.title('Standard')
    plt.subplot(1, 3, 3)
    plt.plot(laplace.histogram(), color='green', linewidth=2.0)
    plt.title('Laplace')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    __self_test()
