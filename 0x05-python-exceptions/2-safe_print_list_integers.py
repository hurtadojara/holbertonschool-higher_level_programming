#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    p_n = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            p_n += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            raise
    print()
    return p_n
