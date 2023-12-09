def read_input(file):
    with open(file) as f:
        lines = f.readlines()
        inputs = []
        for line in lines:
            line_number = []
            for n in line.split(' '):
                line_number.append(int(n.strip()))
            inputs.append(line_number)
        return inputs

def get_diff(inputs: list):
    diff = []
    for i in range(len(inputs) - 1):
        diff.append(inputs[i+1] - inputs[i])
    return diff


def calculate_pyramid_diff(inputs: list, output: list):
    line_diff = get_diff(inputs)
    #if all element in line_diff is 0, then it is the end of pyramid
    output.append(inputs)
    if all([x == 0 for x in line_diff]):
        return output
    else:
        return calculate_pyramid_diff(line_diff, output)

def part1():
    inputs = read_input('input1.txt')
    print(inputs)
    all_sum = 0
    for input in inputs:
        sum = 0
        pyramid = calculate_pyramid_diff(input, [])
        print(pyramid)
        # for each list in pyramid sum the last element
        for p in pyramid:
            sum += p[-1]
        print(sum)
        all_sum += sum
    print(all_sum)

def part2():
    inputs = read_input('input2.txt')
    print(inputs)
    all_sum = 0
    for input in inputs:
        pyramid = calculate_pyramid_diff(input, [])
        print(pyramid)
        # for each list in pyramid, get the first element if the index is even then add, else minus
        sum = 0
        i = 0
        for p in pyramid:
            #if i is even then add, else minus
            if i % 2 == 0:
                sum += p[0]
            else:
                sum -= p[0]
            i += 1
        print(sum)
        all_sum += sum
    print(all_sum)

part2()