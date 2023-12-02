
def find_fist_last_number(str_input):
    first = 0
    last = 0

    array = [c for c in str_input]
    len_array = len(array)

    for i in range(len_array):
        # if array[i] is a number
        if array[i].isdigit():
            first = int(array[i])
            break

    for i in range(len_array):
        # if array[i] is a number
        if array[len_array - i -1].isdigit():
            last = int(array[len_array - i -1])
            break

    return [first, last]

def find_fist_last_number_or_letters(str_input):
    first = 0
    last = 0
    number_letters_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five' : 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9        
    }

    len_input = len(str_input)
    match_first = False
    for i in range(len_input):
        if str_input[i].isdigit():
            first = int(str_input[i])
            break
        for key in number_letters_map:
            if str_input.startswith(key, i, len_input):
                first = number_letters_map[key]
                match_first = True
                break
        if match_first:
            break

    match_last = False
    for i in range(len_input):
        if str_input[len_input - i - 1].isdigit():
            last = int(str_input[len_input - i - 1])
            break
        for key in number_letters_map:
            if str_input.endswith(key, 0, len_input - i):
                last = number_letters_map[key]
                match_last = True
                break
        if match_last:
            break

    return [first, last]

def part1(array):
    # loop through array and find two numbers that add up to 2020
    sum = 0
    for i in range(len(array)):
        # split line into array
        [first, last] = find_fist_last_number(array[i])
        sum += 10*first + last

    print(sum)

def part2(array):
    sum = 0
    for i in range(len(array)):
        # split line into array
        [first, last] = find_fist_last_number_or_letters(array[i])
        sum += 10*first + last

    print(sum)

def read_input(file_name):
    file = open(file_name, "r")
    array = []
    for line in file:
        array.append(line)
    return array

array_input1 = read_input("input1.txt")
part1(array_input1)

array_input2 = read_input("input2.txt")
part2(array_input2)