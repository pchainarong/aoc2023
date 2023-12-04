import re

reg_number = re.compile(r'\d')

def read_input(file_name: str):
    with open(file_name, "r") as file:
        lines = file.readlines()
        line_array = []
        for i in range(len(lines)):
            line_str = lines[i].strip()
            chars = []
            for c in line_str:
                chars.append(c)
            line_array.append(chars)
        print(line_array)
        return line_array

class Position:
    def __init__(self, value:int, row_start:int, col_start:int, row_end:int, col_end:int):
        self.value = value
        self.row_start = row_start
        self.row_end = row_end
        self.col_start = col_start
        self.col_end = col_end

    def __str__(self):
        return f"{self.value} {self.row_start} {self.col_start} {self.row_end} {self.col_end}"

def find_position_number(water_source_array: list):
    positions = []
    gear_positions = []
    for i in range(len(water_source_array)):
        row_start = -1
        row_end = -1
        col_start = -1
        col_end = -1
        value_str = ""
        found = False

        for j in range(len(water_source_array[i])):
            #part2 to find gear positions
            if water_source_array[i][j] == "*":
                gear_positions.append(Gear(i, j))

            if reg_number.match(water_source_array[i][j]) and not found:
                found = True
                row_start = i
                col_start = j
                row_end = i
                col_end = j
                value_str += water_source_array[i][j]
            elif found and reg_number.match(water_source_array[i][j]):
                row_end = i
                col_end = j
                value_str += water_source_array[i][j]
            elif found and not reg_number.match(water_source_array[i][j]):
                found = False
                value = int(value_str)
                position = Position(value, row_start, col_start, row_end, col_end)
                positions.append(position)
                value_str = ""
            else:
                found = False
        if found:
            #add the last one in the row
            value = int(value_str)
            position = Position(value, row_start, col_start, row_end, col_end)
            positions.append(position)
            value_str = ""
    return [positions, gear_positions]

def is_part_number(position: Position, water_source_array: list):
    is_part = False

    for i in range(position.row_start -1 , position.row_end + 2): #python range is exclusive of the end
        for j in range(position.col_start -1, position.col_end + 2):
            if i < 0 or j < 0 or i >= len(water_source_array) or j >= len(water_source_array[i]):
                continue
            #print(i, j, water_source_array[i][j])
            if water_source_array[i][j] != "." and not reg_number.match(water_source_array[i][j]):
                is_part = True
                break
            #print(is_part)
    return is_part

class Gear:
    def __init__(self, row_start:int, col_start:int):
        self.row_start = row_start
        self.col_start = col_start
    
    def __str__(self):
        return f"{self.row_start} {self.col_start}"


def find_number_next_to_gear(gear: Gear, positions: list[Position]):
    numbers_found = []
    gear_row = gear.row_start
    gear_col = gear.col_start

    for position in positions:
        #find if poistion boder overlaps with gear
        if (position.row_start -1 <= gear_row and position.row_end + 1 >= gear_row and \
        position.col_start -1 <= gear_col and position.col_end + 1 >= gear_col):
            numbers_found.append(position)
    return numbers_found

water_source_array = read_input("sample.txt")
# print(water_source_array[0][0])
sum = 0
gear_sum = 0
[positions, gears] = find_position_number(water_source_array)

#part 1
for position in positions:
    # print(position)    
    is_part = is_part_number(position, water_source_array)
    print(position, is_part)
    if is_part:
        sum += position.value

print('sum:', sum)

#part 2
for gear in gears:
    print(gear)
    numbers_found = find_number_next_to_gear(gear, positions)
    for number_found in numbers_found:
        print(number_found)
    if len(numbers_found) == 2:
        print("found 2 numbers")
        innger_gear_sum = 1
        for number_found in numbers_found:
            innger_gear_sum *= number_found.value
        gear_sum += innger_gear_sum

print('gear_sum:', gear_sum)

# print(sum + gear_sum)
# 522144 is too low

        
# x = [['1', '2', '3',], ['4', '5', '6']]
# print(x[0][0])
# print(x[-1][-1])

# for i in range(-1, 1):
#     print(i)

#check if string is digit with regex
# x = "-7"
# reg_number = re.compile(r'\d+')
# print(reg_number.match(x))

# position_set = set()
# position_set.add(Position(1, 1, 1, 1, 1))
# position_set.add(Position(1, 1, 1, 1, 2))
# position_set.add(Position(1, 1, 1, 1, 1))
# print(position_set)
# gear_map = {}
# gear_map[Gear(0, 0)] = position_set
# # gear_map[Gear(0, 0)] = position_set
# print(gear_map[Gear(0, 0)])

#sample_reddit result for part1 is 925
#sample_reddit result for part2 is 6756