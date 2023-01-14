# Day 3: Rucksack Reorganization (https://adventofcode.com/2022/day/3)
# Conditions:
# - The input represents in each line a rucksack containing items
# - A rucksack is seperated in the middle in two compartments
# - Every item type is identified by a single lower or uppercase letter
# - Priority of item is given by an order of the letter in the alphabet, starting at "a", ending at "Z"

def main():
    print("Advent of Code - Day 3")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


# Task 1: Sum the priority of item types repeating in both compartments of a rucksack (among all rucksacks)
def task_1(file):
    # Iterate over rucksacks, separate each in half and find out the priority of the common item between both halves
    # using ASCII
    priority = 0
    for line in file.read().splitlines():
        middle_index = int(len(line) / 2)
        common_items_set = set(line[:middle_index]).intersection(line[middle_index:])
        common_item = common_items_set.pop()
        ascii_start = 96 if common_item.islower() else 38
        priority += ord(common_item) - ascii_start
    print("Task 1 result: " + str(priority))


# Task 2: Sum the priority of badges among all groups; A group consists of three rucksacks; A badge is an item type
# that occurs in all three rucksacks
def task_2(file):
    # Iterate over rucksacks, create groups with 3 rucksacks in them and find out the priority of an item that occurs
    # in all 3 of them
    lines = file.read().splitlines()
    # Create a list of groups (nested lists) with each group having three rucksacks
    groups = [[lines[i], lines[i + 1], lines[i + 2]] for i, _ in enumerate(lines[:-2]) if i % 3 == 0]
    priority = 0
    for group in groups:
        common_items_set = set(group[0]).intersection(group[1], group[2])
        common_item = common_items_set.pop()
        ascii_start = 96 if common_item.islower() else 38
        priority += ord(common_item) - ascii_start
    print("Task 2 result: " + str(priority))


if __name__ == "__main__":
    main()
