# Day 10: Cathode-Ray Tube (https://adventofcode.com/2022/day/10)
# Conditions:
# - The input represents instructions of a program
# - There are two possible commands: "noop" which takes one cycle to complete and "addx {V}" takes 2 cycle to complete
#   and increases the X register by the value V AFTER finishing the 2nd cycle


def main():
    print("Advent of Code - Day 10")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


# Task 1: Get the sum of six signal strength from following cycles: 20th, 60th, 100th, 140th, 180th, and 220th; A signal
#         strength is the cycle number multiplied by the value of the X register
def task_1(file):
    # Iterate over commands, add 1 to cycle count no matter what is the input; If the command is "addx", then add
    # 1 more to the count and update signal strength if it's one of the above-mentioned cycles; At the end of this if,
    # add the number from the command to x register
    signal_strength = 0
    x_register = 1
    cycle_count = 0
    cycle_check = 20
    for command in file.readlines():
        cycle_count += 1
        if command.startswith("addx"):
            cycle_count += 1
            if cycle_count >= cycle_check:
                signal_strength += x_register * cycle_check
                cycle_check += 40
            x_register += int(command.split()[1])
    print("Task 1 result: " + str(signal_strength))


# Task 2: Get eight capital letters appearing on the CRT; The CRT produces a lit pixel represented by "#" if the cycle
#         is the same as one of the sprite pixels (a sprite starts at x_register and is 3 pixels wide) Otherwise a dark
#         pixel (".") will be produced. Find out the letters from cycle 1-240; The left-most pixel in each row is in
#         position 0, and the right-most pixel in each row is in position 39
def execute_cycle_actions(cycle_count, x_register, lit_pixels):
    cycle_count += 1
    if x_register <= cycle_count <= x_register+2:
        lit_pixels.append(cycle_count - 1)
    if cycle_count == 40:
        for idx in range(40):
            print("#", end="") if idx in lit_pixels else print(".", end="")
        print()
        lit_pixels.clear()
        cycle_count = 0
    return cycle_count


def task_2(file):
    # Iterate over commands and no matter what command execute once cycle actions; If it's the command "addx" then
    # execute it once more and add the number from the command to x register; Cycle actions are: add to cycle count,
    # save lit pixels if conditions are fulfilled and if it's a 40th cycle, then print the line and reset the cycle
    # count and lit pixels as the new line starts
    lit_pixels = []
    x_register = 1
    cycle_count = 0
    print("Task 2 result: ")
    for command in file.readlines():
        cycle_count = execute_cycle_actions(cycle_count, x_register, lit_pixels)
        if command.startswith("addx"):
            cycle_count = execute_cycle_actions(cycle_count, x_register, lit_pixels)
            x_register += int(command.split()[1])


if __name__ == "__main__":
    main()
