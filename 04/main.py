import re

def read_input(file_name):
    bingo_numbers = []
    your_tickets = []
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            [temp, data] = line.split(":")
            [bingo_line,ticket_line]= data = data.split("|")
            bingos = re.split('\s+', bingo_line.strip())
            tickets = re.split('\s+', ticket_line.strip())
            bingo_numbers.append(bingos)
            your_tickets.append(tickets)
    #print(bingo_numbers)
    #print(your_tickets)
    return [bingo_numbers, your_tickets]

def find_match_number(bingo_number: list, your_ticket: list):
    wining_number = []
    for i in range(len(bingo_number)):
        for j in range(len(your_ticket)):
            if bingo_number[i] == your_ticket[j]:
                wining_number.append(bingo_number[i])
    return wining_number

def add_up_copy_cards(index: int, copy_counters: list, wining_number: list):
    start = int(index)
    end = start + len(wining_number) + 1 #range is exclusive we need to add 1
    existing_copies = copy_counters[start]
    for j in range(start, end):
        if j == start:
            copy_counters[j] += 1
        if j > start:
            copy_counters[j] += (existing_copies + 1)
    return copy_counters

def part1():
    [bingo_numbers, ticket_numbers] = read_input("input1.txt")
    print(bingo_numbers)
    print(ticket_numbers)
    sum = 0
    for i in range(len(bingo_numbers)):
        bingo = bingo_numbers[i]
        ticket = ticket_numbers[i]
        wining_number = find_match_number(bingo, ticket)
        if len(wining_number) > 0:
            sum += pow(2, len(wining_number)-1)
    print(sum)


def part2():
    [bingo_numbers, ticket_numbers] = read_input("input2.txt")
    sum = 0
    copy_counters = []
    for i in range(len(bingo_numbers)):
        copy_counters.append(0)

    for i in range(len(bingo_numbers)):
        bingo = bingo_numbers[i]
        ticket = ticket_numbers[i]
        wining_number = find_match_number(bingo, ticket)
        if len(wining_number) > 0:
            copy_counters = add_up_copy_cards(i, copy_counters, wining_number)
        else:
            copy_counters[i] += 1
    for counter in copy_counters:
        sum += counter
    print(sum)
        
# part1()
part2()
        
