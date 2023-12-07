global joker_flag
joker_flag = False

class Card:
    def __init__(self, card_input: str, bid: int):
        self.bid = bid
        self.cards = []
        self.card_input = card_input
        for c in card_input:
            self.cards.append(c)

        self.type = 'High Card'
        #calculate type of hand
        if joker_flag:
            self.type = calculate_type_with_joker(card_input)
        else:
            self.type = calculate_type(card_input)

    def __str__(self):
        return f'{self.card_input} {self.bid} {self.type}'

    def __lt__(self, other):
        return self.compare_cards(other)

    def compare_cards(self, other):
        if self.type == other.type:
            for i in range(len(self.cards)):
                #order of value A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
                #mapping value to number
                value1 = get_card_value(self.cards[i])
                value2 = get_card_value(other.cards[i])
                if value1 > value2:
                    return True
                elif value1 < value2:
                    return False

        else:
            if self.type > other.type:
                return True
            else:
                return False

def calculate_type(cards: str):
    #create map from list of cards
    card_map = {}
    type = '1 High Card'
    for c in cards:
        if c in card_map:
            card_map[c] += 1
        else:
            card_map[c] = 1
    #classify type
    if len(card_map) == 1:
        type = '7 Five of a Kind'
    elif len(card_map) == 2:
        if 4 in card_map.values():
            type = '6 Four of a Kind'
        else:
            type = '5 Full House'
    elif len(card_map) == 3:
        if 3 in card_map.values():
            type = '4 Three of a Kind'
        else:
            type = '3 Two Pairs'
    elif len(card_map) == 4:
        type = '2 One Pair'
    else:
        type = '1 High Card'
    return type

def calculate_type_with_joker(cards: str):
    #create map from list of cards
    card_map = {}
    for c in cards:
        if c in card_map:
            card_map[c] += 1
        else:
            card_map[c] = 1
    #get any key with max value

    joker_card_number = card_map.pop('J', None)
    if joker_card_number == 5:
        return '7 Five of a Kind'

    max_value = max(card_map.values())
    #get one key of the max value
    max_key = ''
    for key, value in card_map.items():
        if value == max_value:
            max_key = key
            break
    #replace Joker card with max key
    new_cards = cards.replace('J', max_key)
    print(new_cards)
    return calculate_type(new_cards)

def get_card_value(card: str):
    value = 1
    if card == 'A':
        value = 14
    elif card == 'K':
        value = 13
    elif card == 'Q':
        value = 12
    elif card == 'J':
        if joker_flag:
            value = 1
        else:
            value = 11
    elif card == 'T':
        value = 10
    else:
        value = int(card)
    return value


def read_input(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return lines

def part1():
    lines = read_input('input1.txt')
    cards = []
    for line in lines:
        card_input, bid = line.split(' ')
        card = Card(card_input, int(bid))

        cards.append(card)

    #compare and sort cards with compare_cards function
    for card in cards:
        print(card)

    cards.sort(reverse=True)
    print('Sorted')
    sum = 0
    for i in range(len(cards)):
        sum += cards[i].bid * (i+1)
        print(cards[i])

    print(sum)

def part2():
    lines = read_input('input2.txt')
    cards = []
    for line in lines:
        card_input, bid = line.split(' ')
        print(card_input)
        card = Card(card_input, int(bid))
        cards.append(card)

    #compare and sort cards with compare_cards function
    for card in cards:
        print(card)

    cards.sort(reverse=True)
    print('Sorted')
    sum = 0
    for i in range(len(cards)):
        sum += cards[i].bid * (i+1)
        print(cards[i])

    print(sum)

joker_flag = True
part2()