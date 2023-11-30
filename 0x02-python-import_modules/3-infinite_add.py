#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    result = 0
    for i in range(1, n):
        result += int(sys.argv[i])
    print(result)
