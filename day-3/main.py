# Day 3: Rucksack Reorganization (https://adventofcode.com/2022/day/3)
# Rules:
# - a single line represents a rucksack containing two compartments
# - each compartment have the same amount of items and are seperated in the middle
# - every item type is identified by a single lower or uppercase letter
# - priority of item is given by an order of the letter in the alphabet, starting at "a", ending at "Z"

def main():
    print("Advent of Code - Day 3")
    file = open('input.txt', 'r')
    task_1(file)
    task_2(file)


# Task 1: Sum the priority of item types repeating in both compartments (one per rucksack) among all rucksacks
def task_1(file):
    priority = 0
    for line in file.read().splitlines():
        middle_index = int(len(line) / 2)
        item_common_set = set(line[:middle_index]).intersection(line[middle_index:])
        common_item = item_common_set.pop()
        ascii_start = 96 if common_item.islower() else 38
        priority += ord(common_item) - ascii_start
    print("Task 1 result: " + str(priority))


# Task 2: Sum the priority of badges among all groups; A group consists of three rucksacks; A badge is an item type
# that occurs in all three rucksacks
def task_2(file):
    lines = file.read().splitlines()
    # Create using a "list comprehension" a list of groups (nested lists) with each group having three rucksacks
    groups = [[lines[i], lines[i + 1], lines[i + 2]] for i, _ in enumerate(lines[:-2]) if i % 3 == 0]
    priority = 0
    for group in groups:
        item_common_set = set(group[0]).intersection(group[1], group[2])
        common_item = item_common_set.pop()
        ascii_start = 96 if common_item.islower() else 38
        priority += ord(common_item) - ascii_start
    print("Task 2 result: " + str(priority))


if __name__ == "__main__":
    main()
