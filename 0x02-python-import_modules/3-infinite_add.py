#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    total = 0
    argc = len(argv) - 1
    if argc == 0:
        print(total)
    else:
        for i in range(1, argc + 1):
            total += int(argv[i])
        print(total)
