def safe_print_list(my_list=[], x=0):
    p_n = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            p_n += 1
        except:
            break
    print()
    return p_n
