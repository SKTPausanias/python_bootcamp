#!/usr/bin/python

import time


start_time = time.time()


def ft_progress(listy):
    for i in listy:
        elapsed_time = time.time() - start_time
        eta = (len(listy) - i) * 0.01126
        pct = i/len(listy) * 100
        str1 = ("[" + "=" * int((pct) / 5) + ">").ljust(21, ' ')
        str1 += "]"
        print("ETA:", '{:.2f}'.format(eta), "[", str('{:.0f}'.format(pct)) + "%", "]", str1, i, "/", len(listy), "|", "elapsed time", elapsed_time)
        yield i


listy = range(1000)
ret = 0
# your code

for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)

print()
print(ret)
