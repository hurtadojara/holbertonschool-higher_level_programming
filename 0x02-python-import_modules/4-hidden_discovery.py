#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for iterator in dir(hidden_4):
        if iterator[1] != '_':
            print(iterator)
