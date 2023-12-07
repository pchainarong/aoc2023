import re

def read_input(file_name):
    with open(file_name) as f:
        [_, time_inputs] = f.readline().strip().split(":")
        [_, distance_inputs] =  f.readline().strip().split(":")

        time = re.split('\\s+', time_inputs.strip())
        distance = re.split('\\s+', distance_inputs.strip())

        #convert list of string to number
        time_list = list(map(int, time))
        distance_list = list(map(int, distance))
        return [time_list, distance_list]

def read_input2(file_name):
    with open(file_name) as f:
        [_, time_inputs] = f.readline().strip().split(":")
        [_, distance_inputs] =  f.readline().strip().split(":")

        #replace space with zero length string
        time_inputs = time_inputs.replace(' ', '')
        distance_inputs = distance_inputs.replace(' ', '')

        print(time_inputs)
        print(distance_inputs)

        time = int(time_inputs)
        distance = int(distance_inputs)
        print (time)
        print (distance)
        time_list = [time]
        distance_list = [distance]

        return [time_list, distance_list]

def find_winning_time(time: int, distance: int):
    #for loop start from index 1
    count  = 0
    for i in range(1, time + 1):
        if (time - i)*i  > distance:
            count += 1
    return count


def part1():
    [time_list, distance_list] = read_input('input1.txt')
    print(time_list)
    print(distance_list)
    sum = 1
    for i in range(len(time_list)):
        time = time_list[i]
        distance = distance_list[i]
        print(time, distance)
        result = (find_winning_time(time, distance))
        print(result)
        if result > 0:
            sum *= result
    print(sum)

def part2():
    [time_list, distance_list] = read_input2('input2.txt')
    print(time_list)
    print(distance_list)
    sum = 1
    for i in range(len(time_list)):
        time = time_list[i]
        distance = distance_list[i]
        print(time, distance)
        result = (find_winning_time(time, distance))
        print(result)
        if result > 0:
            sum *= result
    print(sum)

part2()