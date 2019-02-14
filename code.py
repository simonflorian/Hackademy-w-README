import random
def today():
    now = datetime.datetime.now()
    return now.day

def my_sum(a_list):
    total = 0
    for n in a_list:
        total = total + n
    return total

def my_prod(a_list):
    total = 1
    for n in a_list:
        total = total * n
    return total

def my_count(a_list):
    count = 0
    for n in a_list:
        count = count + 1
    return count

def my_count_less_5(a_list):
    count = 0
    for n in a_list:
        if n < 5:
            count = count + 1
    return count

def my_count_ones(a_list):
    count = 0
    for n in a_list:
        if n == 1:
            count = count + 1
    return count

def my_count_max(a_list):
    count = 0
    for n in a_list:
        if n > count:
            count = n
    return count

def my_max(a_list):
    if is_list_empty(a_list):
        return None
    b = a_list[0]
    for n in a_list:
        if n > b:
            b = n
    return b


def single_row_stars(number):
    for n in range(number):
        print("*", end="")


def single_row_of():
    string = str(input("What would you like to print?"))
    my_number = int(input("WHow many times?"))
    for n in range(my_number):
        for i in range(my_number):
             print(string, end="") 
        print()



def list_by_2(a_list):
    new_list = []
    for n in a_list:
        new_list.append(n * 2)
    return new_list

def create_grid(size):
    new_list = []
    for row in range(size):
        liste = []
        for column in range(size):
            liste.append("lol")
        new_list.append(liste)
    return new_list

def setup_game(size, max_alive):
    a_grid = get_empty_


def rand_alive():
    number = random.randint(1,3)
    if number == 1:
        return True
    else:
        return False

def fill_grid_random(a_grid, max_alive):
    size = len(a_grid)
    remaining = max_alive
    for r_i in range(size):
        print(r_i)
        for c_i in range(size):
            print(c_i)
            if remaining > 0:
                if rand_alive() == True:
                    a_grid[r_i][c_i] = 'X'
                    remaining = remaining - 1
                    print(a_grid)
                else:
                    continue
            else:
                a_grid[r_i][c_i] = '-'
    return a_grid

print(fill_grid_random(create_grid(5), 2))


def fill_grid_random(a_grid, max_alive):
    size = len(a_grid)
    remaining = max_alive
    for r_i in range(size):
        print(r_i)
        for c_i in range(size):
            print(c_i)
            if (remaining > 0) and (rand_alive() == True):
                a_grid[r_i][c_i] = 'X'
                remaining = remaining - 1
            else:
                a_grid[r_i][c_i] = '-'
    return a_grid

print(fill_grid_random(create_grid(5), 2))




def print_grid(a_grid):
    size = len(grid)
    for r_i in range(size):
        print(r_i)
        for c_i in range(size):
            print(a_grid[r_i][c_i], end="")
        print("")




def is_duplicate_there(list_a, list_b):
    counter = 0
    for n in list_a:
        for i in list_b:
            if i == n:
                counter = counter + 1
            else:
                None

    if counter > 0:
        return True
    else:
        return False

        



