class Game:
    id: int
    red_cube: int
    blue_cube: int
    green_cube: int

    def __init__(self, id: int):
        self.id = id
        self.red_cube = 0
        self.blue_cube = 0
        self.green_cube = 0

    def update_red_cube(self, red_cube: int):
        if red_cube > self.red_cube:
            self.red_cube = red_cube
    
    def update_blue_cube(self, blue_cube: int):
        if blue_cube > self.blue_cube:
            self.blue_cube = blue_cube
    
    def update_green_cube(self, green_cube: int):
        if green_cube > self.green_cube:
            self.green_cube = green_cube

    def is_valid(self):
        return self.red_cube <= 12 and self.blue_cube <= 14 and self.green_cube <= 13
    
    def get_power(self):
        return self.red_cube * self.blue_cube * self.green_cube
    
    def __str__(self):
        return f"{self.id} {self.red_cube} {self.blue_cube} {self.green_cube}"

def read_input(file_name: str):
    with open(file_name, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines

def parse_input(lines: list):
    games = []
    for line in lines:
        #read this input format and extract to create Game class
        #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        [game_str, play_subsets_str] = line.split(":")
        [tmp, game_num] = game_str.split()
        game = Game(int(game_num))

        play_subsets = play_subsets_str.split(";")
        
        for play_subset in play_subsets:
            play_subset = play_subset.strip()
            records = play_subset.split(",")
            #records will have format like: 3 blue, 4 red
            for record in records:
                record = record.strip()
                [num, color] = record.split()
                num = int(num)
                if color == "red":
                    game.update_red_cube(num)
                elif color == "blue":
                    game.update_blue_cube(num)
                elif color == "green":
                    game.update_green_cube(num)

        games.append(game)
    return games

def main1():
    lines = read_input("input1.txt")
    games = parse_input(lines)
    sum = 0
    for game in games:
        if game.is_valid():
            sum += game.id
    print(sum)

def main2():
    lines = read_input("input2.txt")
    games = parse_input(lines)
    sum = 0
    for game in games:
        sum += game.get_power()
    print(sum)

main2()