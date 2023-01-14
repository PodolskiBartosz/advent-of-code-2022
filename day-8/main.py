# Day 8: Treetop Tree House (https://adventofcode.com/2022/day/8)
# Conditions:
# - The input represents a forest full of trees in a grid format
# - The height of a tree ranges from 0 until 9
# - A tree is visible, if all the surrounding trees from one of the directions (left, right, top, bottom)
#   is lower than it


def main():
    print("Advent of Code - Day 8")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


# Task 1: Get number of the trees visible from outside the grid
def task_1(file):
    # Iterate over all trees and check if any of the sides are completely visible
    grid = file.read().splitlines()
    visible_trees = len(grid)*2 + (len(grid[0])-2)*2  # Get number of trees outside
    for row_index, row in enumerate(grid):
        if row_index == 0 or row_index == len(grid)-1:  # Skip first and last row
            continue
        for tree_index, tree_height in enumerate(row):
            if tree_index == 0 or tree_index == len(row)-1:  # Skip first and last column
                continue
            tree_height = int(tree_height)
            visible_from_left = all(int(height) < tree_height for height in row[:tree_index])
            visible_from_right = all(int(height) < tree_height for height in row[tree_index+1:])
            top_trees = [row[tree_index] for row in grid[:row_index]]
            visible_from_top = all(int(height) < tree_height for height in top_trees)
            bottom_trees = [row[tree_index] for row in grid[row_index+1:]]
            visible_from_bottom = all(int(height) < tree_height for height in bottom_trees)
            visible_trees += any([visible_from_left, visible_from_right, visible_from_top, visible_from_bottom])
    print("Task 1 result: " + str(visible_trees))


def get_vision(tree_height, tree_list):
    vision = 0
    index = 0
    while index != len(tree_list):
        vision += 1
        if int(tree_list[index]) >= tree_height:  # If tree is the same height or higher, then it's the last visible one
            return vision
        index += 1
    return vision


# Task 2: Get the highest scenic score for any tree; A scenic score is found by multiplying together it's viewing
#         distance in each of the four directions; Viewing distance is the amount of trees that are of the same or lower
#         height; Outermost trees have the distance of 0
def task_2(file):
    # Iterate over all the trees and check if the tree's combined visions is higher than the highest one until now
    grid = file.read().splitlines()
    highest_scenic_score = 0
    for row_index, row in enumerate(grid):
        if row_index == 0 or row_index == len(grid)-1:  # Skip first and last row
            continue
        for tree_index, tree_height in enumerate(row):
            if tree_index == 0 or tree_index == len(row)-1:  # Skip first and last column
                continue
            tree_height = int(tree_height)
            left_vision = get_vision(tree_height, row[:tree_index:][::-1])
            right_vision = get_vision(tree_height, row[tree_index+1:])
            top_trees = [row[tree_index] for row in grid[:row_index]]
            top_vision = get_vision(tree_height, top_trees[::-1])
            bottom_trees = [row[tree_index] for row in grid[row_index+1:]]
            bottom_vision = get_vision(tree_height, bottom_trees)
            vision_score = left_vision * right_vision * top_vision * bottom_vision
            if vision_score > highest_scenic_score:
                highest_scenic_score = vision_score
    print("Task 2 result: " + str(highest_scenic_score))


if __name__ == "__main__":
    main()
