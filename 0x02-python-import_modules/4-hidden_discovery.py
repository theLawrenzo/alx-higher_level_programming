#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    new_list = [x for x in dir(hidden_4) if not x.startswith('__')]
    for i in new_list:
        print(i)
