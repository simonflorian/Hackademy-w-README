import code

list_a = [31, 51, 61, 71, 81]
list_b = [4, 6, 7, 8, 0]


print(code.is_duplicate_there(list_a, list_b))


def is_duplicate_there(list_a, list_b):
    for i in list_a:
        if (i in list_b):
            return True
        else: False

