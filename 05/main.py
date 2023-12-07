import re
import sys

class Rule:
    def __init__(self, dest: int, source: int, range: int):
        self.dest = dest
        self.source = source
        self.range = range

    def __str__(self):
        return f'{self.dest} <- {self.source} if {self.range}'

    def is_match(self, value: int):
        if value >= self.source and value < self.source + self.range:
            return True
        return False

    def calculate_rule(self, value: int):
        if self.is_match(value):
            return self.dest + (value - self.source)
        else:
            return None


class Category:
    def __init__(self, start, end, rules):
        self.start = start
        self.end = end
        self.rules = rules

    def __str__(self):
        return f'{self.start} - {self.end}'

    def calculate_category(self, value: int):
        for rule in self.rules:
            result = rule.calculate_rule(value)
            if result is not None:
                return result
        return value


def parse_rule(line):
    [dest, source, range] = line.split(' ')
    return Rule(int(dest.strip()), int(source.strip()), int(range.strip()))

def read_file(file_name):
    i = 0
    print('read file')
    seeds = []
    category_list = []

    with open(file_name) as f:
        # for loop
        first_line = f.readline()
        seeds_list = re.split('\\s+', first_line.split(':')[1].strip())
        seeds = list(map(int, seeds_list))
        print('seeds:', seeds)

        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.endswith('map:'):
                [start, end] = line.split(' ')[0].split('-to-')
                i += 1
                line = lines[i].strip()
                rules = []
                while len(line) != 0:
                    rules.append(parse_rule(line))
                    i += 1
                    if i >= len(lines):
                        break
                    line = lines[i].strip()
                category_list.append(Category(start, end, rules))
            else:
                continue
    return [seeds, category_list]

def part1():
    [seeds, category_list] = read_file('input1.txt')
    # for cat in category_list:
    #     print(cat)
    #     for rule in cat.rules:
    #         print(rule)

    start_cat = 'seed'
    end_cat = 'location'
    traverse_cat = start_cat
    print(seeds)
    min_seed = sys.maxsize
    for seed in seeds:
        print('start of', seed)
        while traverse_cat != end_cat:
            print(traverse_cat)
            for cat in category_list:
                if cat.start == traverse_cat:
                    traverse_cat = cat.end
                    seed = cat.calculate_category(seed)
                    break

        print(traverse_cat)
        print(f'end of {seed}')
        traverse_cat = start_cat
        # find min seed value
        if seed < min_seed:
            min_seed = seed
    print('min', min_seed)

part1()
