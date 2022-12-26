# Day 1: Calorie Counting (https://adventofcode.com/2022/day/1)
# Conditions:
# - Inventory consists of calories seperated by new line
# - Each inventory is seperated by empty space

def main():
    print("Advent of Code - Day 1")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


# Task 1: Get the calorie number of an inventory with the most of them
def task_1(file):
    calories = 0
    max_calories = 0
    for line in file.readlines():
        if line == "\n":
            if calories > max_calories:
                max_calories = calories
            calories = 0
        else:
            calories += int(line)
    print("Task 1 result: " + str(max_calories))


# Task 2: Sum top three inventories by calorie count
def task_2(file):
    calories = 0
    calories_list = []
    for line in file.readlines():
        if line == "\n":
            calories_list.append(calories)
            calories = 0
        else:
            calories += int(line)
    sum_top_calories = sum(sorted(calories_list)[-3:])
    print("Task 2 result: " + str(sum_top_calories))


if __name__ == "__main__":
    main()
