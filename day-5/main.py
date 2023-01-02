# Day 5: Supply Stacks (https://adventofcode.com/2022/day/5)
# Conditions:
# - The input represents two sections seperated by an empty line, crates section and rearrangement section
# - Crates Section is a 9 by 9 table, with vertical stacks and horizontal levels; The bottom level describes a stack
#   with numbers from  1 to 9; Other levels (8 of them) are filled with crates represented by capital letters surrounded
#   by squared brackets; Lack of crate is represented by three empty spaces
# - Rearrangement section consists of a list of instructions; An instruction has a syntax "move [number of crates] from
#   [stack x] to [stack y]"

def main():
    print("Advent of Code - Day 5")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


def get_sections(file):
    # Separate into two sections and get a list of lines
    levels, instructions = [section.split("\n") for section in file.read().split("\n\n")]
    levels = [crate.replace("    ", " [X] ") for crate in levels[:-1]]  # Replace empty space with [X]
    levels = [[crate[1] for crate in level.split()] for level in levels]  # Get rid of brackets
    stacks = [[] for _ in range(len(levels[0]))]  # Create nested lists of number of vertical stacks
    for level in reversed(levels):
        for index, crate in enumerate(level):
            if crate != "X":
                stacks[index].append(crate)
    return instructions, levels, stacks


# Task 1: Get the crate names from the top of each stack after the rearrangement procedure, hereby the crates are moved
#         one after another, so the top crate of one stock ends up on the bottom of another
def task_1(file):
    instructions, levels, stacks = get_sections(file)
    for instruction in instructions:
        quantity, from_stack_order, to_stack_order = [int(i) for i in instruction.split(" ") if i.isnumeric()]
        while quantity != 0:
            stacks[to_stack_order-1].append(stacks[from_stack_order - 1].pop())  # Move crates each after another
            quantity -= 1
    print("Task 1 result: ", end="")
    [print(stack[-1], end="") for stack in stacks]
    print()


# Task 2: Get the crate names from the top of each stack after the rearrangement procedure, hereby the crates are moved
#         all at once, so the top crate of one stock ends up on the top of another
def task_2(file):
    instructions, levels, stacks = get_sections(file)
    for instruction in instructions:
        quantity, from_stack_order, to_stack_order = [int(i) for i in instruction.split(" ") if i.isnumeric()]
        from_stack = stacks[from_stack_order-1]
        stacks[to_stack_order-1].extend(from_stack[len(from_stack)-quantity:])  # Move crates all at once
        stacks[from_stack_order-1] = from_stack[:len(from_stack)-quantity]
    print("Task 2 result: ", end="")
    [print(stack[-1], end="") for stack in stacks]


if __name__ == "__main__":
    main()
