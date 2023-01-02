# Day 2: Rock Paper Scissors (https://adventofcode.com/2022/day/2)
# Conditions:
# - In the first task the input represents the opponent's shape (A B C) and user's shape (Y X Z)
# - In the second task the input represents the opponent's shape (A B C) and expected outcome (Y X Z)
# - The game has the regular rules of rock-paper-scissors
# - A new line represents a new round
# - The final score is a combination of round's outcome and points for a shape

def main():
    print("Advent of Code - Day 2")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


class Shape:
    def __init__(self, name, points, win_against, lose_against):
        self.name = name
        self.points = points
        self.win_against = win_against
        self.lose_against = lose_against

    def determine_user_score(self, char):
        match char:
            case "X":  # Lose
                return shapes_mapping[self.win_against].points
            case "Y":  # Tie
                return 3 + self.points
            case "Z":  # Win
                return 6 + shapes_mapping[self.lose_against].points


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
        opponent_shape, user_shape = line.split()
        if user_shape.name == opponent_shape.name:  # Tie
            score += 3
        elif user_shape.win_against == opponent_shape.name:  # Win
            score += 6
        score += user_shape.points
    print("Task 1 result: " + str(score))


# Task 2: Sum user's score from all games using opponent's shape and expected outcome
def task_2(file):
    score = 0
    for line in file.readlines():
        opponent_shape, expected_outcome = line.split()
        score += opponent_shape.determine_user_score(expected_outcome)
    print("Task 2 result: " + str(score))


if __name__ == "__main__":
    main()
