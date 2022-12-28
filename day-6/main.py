# Day 6: Tuning Trouble (https://adventofcode.com/2022/day/6)
# Conditions:
# - In a given file there is a non-seperated string of characters
# - The answer is the position of the character in the string; This character is the last character of a
#   substring consisting of X unique characters starting; Substrings are created in a schema 0:X->1:X+1

def main():
    print("Advent of Code - Day 4")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


# Task 1: Get the position of the character, with X being 4
def task_1(file):
    file_content = file.read()
    index = 0
    while len(set(file_content[index:index+4])) != 4:
        index += 1
    print("Task 1 result: " + str(index+4))


# Task 2: Get the position of the character, with X being 14
def task_2(file):
    file_content = file.read()
    index = 0
    while len(set(file_content[index:index+14])) != 14:
        index += 1
    print("Task 2 result: " + str(index+14))


if __name__ == "__main__":
    main()
