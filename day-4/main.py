# Day 4: Camp Cleanup (https://adventofcode.com/2022/day/4)
# Conditions:
# - A line represents two ranges of id-sections


def main():
    print("Advent of Code - Day 4")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


# Task 1: Get number of assignments, where one range completely overlaps with the other
def task_1(file):
    overlaps = 0
    for line in file.read().splitlines():
        # Create a list using split and map function in order to extract range values as int in a nested list
        pairs = [list(map(int, pair.split('-'))) for pair in line.split(",")]
        if pairs[0][0] == pairs[1][0]:
            # Determine the inside_range_index by the smaller ending value
            inside_range_index, outside_range_index = (0, 1) if pairs[0][1] < pairs[1][1] else (1, 0)
        else:
            inside_range_index, outside_range_index = (0, 1) if pairs[0][0] > pairs[1][0] else (1, 0)
        if pairs[inside_range_index][1] <= pairs[outside_range_index][1]:
            overlaps += 1
    print("Task 1 result: " + str(overlaps))


# Task 2: Get number of assignments, where one range has an overlapping section with the other range
def task_2(file):
    overlaps = 0
    for line in file.read().splitlines():
        pairs = [list(map(int, pair.split('-'))) for pair in line.split(",")]
        inside_range_index, outside_range_index = (0, 1) if pairs[0][0] > pairs[1][0] else (1, 0)
        if pairs[inside_range_index][0] <= pairs[outside_range_index][1]:
            overlaps += 1
    print("Task 2 result: " + str(overlaps))


if __name__ == "__main__":
    main()
