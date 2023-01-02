# Day 4: Camp Cleanup (https://adventofcode.com/2022/day/4)
# Conditions:
# - A line represents two ranges of id-sections seperated by coma


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
        # Create two lists using split and map function in order to extract range values as integers
        first_pair, second_pair = [list(map(int, pair.split('-'))) for pair in line.split(",")]
        if first_pair[0] != second_pair[0]:
            # Determine the inside range by the higher starting value
            if first_pair[0] > second_pair[0]:
                inside_range, outside_range = first_pair, second_pair
            else:
                inside_range, outside_range = second_pair, first_pair
        else:
            # If the starting value is the same, then determine the inside range by the smaller ending value
            if first_pair[1] < second_pair[1]:
                inside_range, outside_range = first_pair, second_pair
            else:
                inside_range, outside_range = second_pair, first_pair
        # Check if the inside range ends before or at the same place as the end of outside range
        if inside_range[1] <= outside_range[1]:
            overlaps += 1
    print("Task 1 result: " + str(overlaps))


# Task 2: Get number of assignments, where one range has an overlapping section with the other range
def task_2(file):
    overlaps = 0
    for line in file.read().splitlines():
        # Create two lists using split and map function in order to extract range values as integers
        first_pair, second_pair = [list(map(int, pair.split('-'))) for pair in line.split(",")]
        # Determine the inside range by the higher starting value
        if first_pair[0] > second_pair[0]:
            inside_range_index, outside_range_index = first_pair, second_pair
        else:
            inside_range_index, outside_range_index = second_pair, first_pair
        # Check if the inside range ends before or at the same place as the start of outside range
        if inside_range_index[0] <= outside_range_index[1]:
            overlaps += 1
    print("Task 2 result: " + str(overlaps))


if __name__ == "__main__":
    main()
