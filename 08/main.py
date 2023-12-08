from math import lcm


class Node:
    def __init__(self, value:str, left: str, right: str):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return f'({self.value} : {self.left}, {self.right})'

#read input files
def read_input(file_name):
    instruction = ''
    with open(file_name) as f:
        #read first line
        instruction = f.readline().strip()
        #skip the empty line
        f.readline()
        lines = f.readlines()
        nodes = {}
        for line in lines:
            print(line)
            [node_value, target] = line.split('=')
            #extract value in parenthesis
            [left, right] = target.strip()[1:-1].split(',')
            #add to instruction
            nodes[node_value.strip()] = (Node(node_value.strip(), left.strip(), right.strip()))
        return instruction, nodes

def part1():
    instruction, nodes = read_input('input1.txt')
    instructions = []
    for i in instruction:
        instructions.append(i)
    print(instructions)
    print(len(nodes))
    for node in nodes:
        print(node, nodes[node])

    start_node = 'AAA'
    end_node = 'ZZZ'
    #find path

    count = 0
    while start_node != end_node:
        for i in range(len(instructions)):
            if instructions[i] == 'L':
                start_node = nodes[start_node].left
            elif instructions[i] == 'R':
                start_node = nodes[start_node].right
            else:
                print('Error')
                break
            print(start_node, end_node)
            count += 1

    print(count)


def part2():
    instruction, nodes = read_input('input2.txt')
    instructions = []
    for i in instruction:
        instructions.append(i)
    print(instructions)
    print(len(nodes))
    for node in nodes:
        print(node, nodes[node])

    start_nodes = []
    #find all node endsWith 'A'
    for node in nodes:
        if node.endswith('A'):
            start_nodes.append(node)

    count_list = []
    for start_node in start_nodes:
        print(start_node)
        count = 0
        while not start_node.endswith('Z'):
            for i in range(len(instructions)):
                if instructions[i] == 'L':
                    start_node = nodes[start_node].left
                elif instructions[i] == 'R':
                    start_node = nodes[start_node].right
                else:
                    print('Error')
                    break
                count += 1
                print(count, instructions[i], start_node)

        count_list.append(count)

    #find the number for least common multiple value of number in count_list
    print(count_list)
    print(lcm(*count_list))

part2()

def test():
    a = [10,20,30]
    print(lcm(20, 30, 1, 50, 100, 30))
    print(lcm(*a))
    print(*a)
    print(a)