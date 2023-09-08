#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    h = len(argv) - 1
    sum = 0
    if h == 0:
        print(sum)
    else:
        for i in range(1, h + 1):
            sum = sum + int(argv[i])
        print(sum)
