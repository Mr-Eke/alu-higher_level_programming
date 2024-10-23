#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    # added_values = 0
    # for i in argv[1:]:
    #     added_values += int(i)
    # print(added_values)

    added_values = sum(int(i) for i in argv[1:])
    print(added_values)
