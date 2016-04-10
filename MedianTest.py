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
        result = np.median([a, b, c])
    else:
        result = mid(a, b, c)
    action_time = time() - start_time
    # if opt == 0:
    #     print('np.median time: ' + str(action_time))
    # else:
    #     print('mid time: ' + str(action_time))
    return action_time, result


def __test():
    mid_times = []
    median_times = []
    total_attempts = 512
    mid_errs = 0
    for i in range(0, total_attempts):
        a, b, c = random()*1000, random()*1000, random()*1000
        mid = 1000*count_time(a, b, c, 1)
        median = 1000*count_time(a, b, c, 0)
        mid_times.append(mid[0])
        median_times.append(median[0])
        print(str(mid[1]) + ' ' + str(median[1]))
        if mid[1] != median[1]:
            mid_errs+=1

    total_mid_time = sum(mid_times)
    total_median_time = sum(median_times)
    print('Total number of attempts: ' + str(total_attempts))
    print('mid total time (ms): ' + str(total_mid_time))
    print('np.median total time (ms): ' + str(total_median_time))
    print('Mid error count: ' + str(mid_errs))
    if mid_errs==0:
        print('Mid correct!')
    else:
        print('Mid incorect!')

    if total_mid_time < total_median_time:
        print('Better performance: mid')
    elif total_mid_time > total_median_time:
        print('Better performance: np.median')
    else:
        print('Equal performance: mid, np.median')


    plt.plot(range(0, total_attempts), mid_times,'b+', linewidth=2.0, label='mid')
    plt.plot(range(0, total_attempts), median_times, 'rx', linewidth=2.0, label='np.median')
    plt.title('mid vs np.median')
    plt.xlabel('attempt nr')
    plt.ylabel('time (ms)')
    plt.axis([0, total_attempts, -0.5*max(median_times), 1.5*max(median_times)])
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    __test()
