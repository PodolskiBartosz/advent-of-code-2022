# Day 9: Rope Bridge (https://adventofcode.com/2022/day/9)
# Conditions:
# - The input represents series of motions (R, L, U, D) of the rope's head
# - The rope has a head and a tail, which must always stay in touch, even by overlapping
# - If the head is ever two steps directly up, down, left or right from the tail, the tail must also move one step in
#   that direction
# - Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step
#   diagonally to keep up
# - After each step the position of the tail must be updated


def main():
    print("Advent of Code - Day 9")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


def get_visited_by_tail(rope, moves):
    # Iterate firstly over all move instructions, over each move, move the head and then iterate over all tails as long
    # as the tail is not touching the temporary head; Afterwards it will be checked if the head is in the same line,
    # if not then the tail should move diagonally; Until the tail touches the head it will move straight. If it's the
    # last tail, then it should add to the dictionary which saves all moves made by it.
    tail_visited_pos = {0: {0}}
    for move in moves:
        move_direction, move_num = move.split()
        head = rope[0]
        for _ in range(int(move_num)):
            move_head_straight(head, move_direction)
            for knot_idx in range(len(rope)-1):
                temp_head, tail = rope[knot_idx], rope[knot_idx+1]
                if not is_head_touching(temp_head, tail):
                    is_last_tail = knot_idx+2 == len(rope)
                    if not (temp_head[0] == tail[0] or temp_head[1] == tail[1]):
                        move_tail_diagonally(temp_head, tail)
                        add_tail_to_dict(is_last_tail, tail, tail_visited_pos)
                    while not is_head_touching(temp_head, tail):
                        move_tail_straight(temp_head, tail)
                        add_tail_to_dict(is_last_tail, tail, tail_visited_pos)
                else:
                    break
    return tail_visited_pos


def move_head_straight(part, direction):
    match direction:
        case "R":
            part[0] += 1
        case "L":
            part[0] -= 1
        case "U":
            part[1] += 1
        case "D":
            part[1] -= 1


def move_tail_diagonally(head, tail):
    if head[0] > tail[0]:
        tail[0] += 1
    else:
        tail[0] -= 1
    if head[1] > tail[1]:
        tail[1] += 1
    else:
        tail[1] -= 1


def move_tail_straight(head, tail):
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    elif head[1] == tail[1]:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1


def is_head_touching(head, tail):
    row_dist_from_head = abs(head[0] - tail[0])
    column_dist_from_head = abs(head[1] - tail[1])
    return max(row_dist_from_head, column_dist_from_head) <= 1


def add_tail_to_dict(should, tail, dictionary):
    if should:
        dictionary.setdefault(tail[0], set()).add(tail[1])


def visualize_test(rope):
    # For test1 file
    rows_len = 6
    columns_len = 5
    # For test2 file
    rows_len = 26
    columns_len = 21
    grid = [["."] * rows_len for _ in range(columns_len)]
    head_x, head_y = rope[0]
    grid[head_y][head_x] = "H"
    for i, tail in enumerate(rope[1:]):
        tail_x, tail_y = tail
        if grid[tail_y][tail_x] == ".":
            grid[tail_y][tail_x] = str(i+1)
    for row in grid[::-1]:
        for char in row:
            print(char, end=" ")
        print()
    print("-" * rows_len*2)


# Task 1: Get the number of positions, that the tail visited at least once (including start position) with 2 knots
def task_1(file):
    rope = [[0, 0] for _ in range(2)]
    tail_visited_pos = get_visited_by_tail(rope, file.readlines())
    visited_pos_num = 0
    for row in tail_visited_pos.values():
        visited_pos_num += len(set(row))
    print("Task 1 result: " + str(visited_pos_num))


# Task 2: Get the number of positions, that the tail visited at least once (including start position) with 10 knots
def task_2(file):
    rope = [[0, 0] for _ in range(10)]
    tail_visited_pos = get_visited_by_tail(rope, file.readlines())
    visited_pos_num = 0
    for row in tail_visited_pos.values():
        visited_pos_num += len(row)
    print("Task 2 result: " + str(visited_pos_num))


if __name__ == "__main__":
    main()