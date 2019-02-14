#[12,34,[56,67]]

a_list = [12, 34, [56, 67], 78]

def flatten(a_list_of_lists):
    new_list = []
    for n in a_list_of_lists:
        if isinstance(n,list):
            for i in n:
                new_list.append(i)
        else:
            new_list.append(n)
    return new_list


def print_right(a_list_of_lists):
    for n in a_list_of_lists:
        if isinstance(n,list):
            for i in n:
                print(i, end=', ')
            print('')
        else:
            print(n)
    
print_right(a_list)

for n in range(50):
    print("lol", end=" ")


def single_row_stars(number):
    for n in range(number):
        print("*", end="")

print("hi")