#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n_l = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return n_l
    else:
        n_l[idx] = element
        return n_l
