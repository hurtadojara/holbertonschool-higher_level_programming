#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_l = my_list.copy()
    new_l = set(new_l)
    return sum(new_l)
