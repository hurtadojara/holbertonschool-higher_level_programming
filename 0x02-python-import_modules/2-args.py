#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        if argc == 1:
            print("{} argument:".format(argc))
            print("{}: {}".format(argc, argv[argc]))
        else:
            print("{} arguments:". format(argc))
            for i in range(1, argc + 1):
                print("{}: {}". format(i, argv[i]))
