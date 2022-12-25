# Day 2: Rock Paper Scissors (https://adventofcode.com/2022/day/2)
# Rules:
# - regular rock-paper-scissors game
# - new line represents a new round
# - score is a combination of round's outcome and points for a shape

def main():
    print("Advent of Code - Day 2")
    file = open('input.txt', 'r')
    task_1(file)
    task_2(file)


class Shape:
    def __init__(self, name, score, win_against, lose_against):
        self.name = name
        self.score = score
        self.win_against = win_against
        self.lose_against = lose_against

    def determine_user_points(self, char):
        match char:
            case "X":  # Lose
                return shapes_mapping[self.win_against].score
            case "Y":  # Tie
                return 3 + self.score
            case "Z":  # Win
                return 6 + shapes_mapping[self.lose_against].score


rock = Shape("rock", 1, "scissors", "paper")
paper = Shape("paper", 2, "rock", "scissors")
scissors = Shape("scissors", 3, "paper", "rock")
opponent_mapping = {
    "A": rock,
    "B": paper,
    "C": scissors
}
user_mapping = {
    "X": rock,
    "Y": paper,
    "Z": scissors
}
shapes_mapping = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}


# Task 1: Sum user's score from all games using user's and opponent's shape
def task_1(file):
    score = 0
    for line in file.readlines():
        characters = line.split()  # 1st char represents enemy's shape, 2nd char represents user's shape
        opponent_shape = opponent_mapping[characters[0]]
        user_shape = user_mapping[characters[1]]
        if user_shape.name == opponent_shape.name:  # Tie
            score += 3
        elif user_shape.win_against == opponent_shape.name:  # Win
            score += 6
        score += user_shape.score
    print("Task 1 result: " + str(score))


# Task 2: Sum user's score from all games using opponent's shape and expected outcome
def task_2(file):
    score = 0
    for line in file.readlines():
        characters = line.split()  # 1st char represents enemy's shape, 2nd char represents round's outcome
        opponent_shape = opponent_mapping[characters[0]]
        score += opponent_shape.determine_user_points(characters[1])

    print("Task 2 result: " + str(score))


if __name__ == "__main__":
    main()
