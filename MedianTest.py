import matplotlib.pyplot as plt
import numpy as np
from random import random
from time import time


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


def count_time(a, b, c, opt):
    start_time = time()
    if opt == 0:
        np.median([a, b, c])
    else:
        mid(a, b, c)
    action_time = time() - start_time
    if opt == 0:
        print('np.median time: ' + str(action_time))
    else:
        print('mid time: ' + str(action_time))
    return action_time


def __test():
    mid_times = []
    median_times = []
    amount = 150
    for i in range(0, amount):
        a, b, c = random()*1000, random()*1000, random()*1000
        mid_times.append(1000*count_time(a, b, c, 1))
        median_times.append(1000*count_time(a, b, c, 0))

    plt.plot(range(0, amount), mid_times,'b+', linewidth=2.0, label='mid')
    plt.plot(range(0, amount), median_times, 'rx', linewidth=2.0, label='np.median')
    plt.title('mid vs np.median')
    plt.xlabel('attempt nr')
    plt.ylabel('time (ms)')
    plt.axis([0, amount, -0.5*max(median_times), 1.5*max(median_times)])
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    __test()
