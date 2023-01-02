# Day 1: Calorie Counting (https://adventofcode.com/2022/day/1)
# Conditions:
# - The input file represents inventories
# - Inventory consists of calories seperated by new line
# - Each inventory is seperated by empty line

def main():
    print("Advent of Code - Day 1")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


# Task 1: Get the calorie number of an inventory with the most of them
def task_1(file):
    inventory = 0
    biggest_inventory = 0
    for line in file.readlines():
        if line == "\n":  # The line is empty representing end of one inventory
            if inventory > biggest_inventory:
                biggest_inventory = inventory
            inventory = 0
        else:  # The line represent calories
            inventory += int(line)
    print("Task 1 result: " + str(biggest_inventory))


# Task 2: Sum top three inventories by calorie count
def task_2(file):
    inventory = 0
    inventory_list = []
    for line in file.readlines():
        if line == "\n":  # The line is empty representing end of one inventory
            inventory_list.append(inventory)
            inventory = 0
        else:  # Otherwise the line represents calories
            inventory += int(line)
    sum_top_inventories = sum(sorted(inventory_list)[-3:])  # Sort inventories and sum last 3 of them (the highest ones)
    print("Task 2 result: " + str(sum_top_inventories))


if __name__ == "__main__":
    main()
