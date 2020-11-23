#!/usr/bin/python3

import time


start_time = time.time()


def progressbar(listy):
    for i in listy:
        elapsed_time = time.time() - start_time
        eta = (len(listy) - i) * 0.01126
        pct = i/len(listy) * 100
        str1 = ("[" + "=" * int((pct) / 5) + ">").ljust(21, ' ')
        str1 += "]"
        print("ETA:", '{:.2f}'.format(eta), "[", str('{:.0f}'.format(pct)) + "%", "]", str1, i, "/", len(listy), "|", "elapsed time", elapsed_time)
        yield i
