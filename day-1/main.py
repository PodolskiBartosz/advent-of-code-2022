#https://adventofcode.com/2022/day/1

def main():
    print("Advent of Code - Day 1:")
    file = open('input.txt', 'r')
    lines = file.readlines()
    task_1(lines)
    task_2(lines)


def task_1(lines):
    calories = 0
    max_calories = 0
    for line in lines:
        if line == "\n":
            if calories > max_calories:
                max_calories = calories
            calories = 0
        else:
            calories += int(line)
    print("Task 1 result: " + str(max_calories))


def task_2(lines):
    calories = 0
    calories_list = []
    for line in lines:
        if line == "\n":
            calories_list.append(calories)
            calories = 0
        else:
            calories += int(line)
    sum_top_calories = sum(sorted(calories_list)[-3:])
    print("Task 2 result: " + str(sum_top_calories))

if __name__ == "__main__":
    main()