from math import *

for i in range(0, 360, 15):
    print(i, '---', round(sin(i), 4), round(cos(i), 4))