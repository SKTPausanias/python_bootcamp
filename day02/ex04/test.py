from ai42 import progressbar

listy = range(1000)
ret = 0
# your code
import time

for elem in progressbar(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)

print()
print(ret)