#!/usr/bin/python3

from enum import Enum

def read_file(filename):
    with open(filename) as f:
        return [row.strip('\n') for row in f.readlines()]

def print_forest(forest):
    print('\n'.join([''.join(str(x)) for x in forest]))
    print()


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

def get_visible(starting_point, direction, forest):
    x = starting_point[0]
    y = starting_point[1]

    visible = set()
    min_size = -1
    while True:
        if x < 0 or y < 0 or x >= len(forest) or y >= len(forest):
            return visible
        else:
            tree_size = forest[x][y]
            if tree_size > min_size:
                visible.add((x, y))
                min_size = tree_size
            else:
                # We cannot see that tree
                pass

        x += direction.value[0]
        y += direction.value[1]

def part1():
    forest = [[int(tree) for tree in tree_row] for tree_row in read_file('input.txt')]
    all_visible = set()

    forest_edge_length = len(forest)
    for x in range(0, forest_edge_length):
        for y in range(0, forest_edge_length):
            if x == 0:
                all_visible |= get_visible((x, y), Direction.DOWN, forest)
            if y == 0:
                all_visible |= get_visible((x, y), Direction.RIGHT, forest)
            if x == forest_edge_length - 1:
                all_visible |= get_visible((x, y), Direction.UP, forest)
            if y == forest_edge_length - 1:
                all_visible |= get_visible((x, y), Direction.LEFT, forest)
    
    print(len(all_visible))

def part2():
    trees = [[int(tree) for tree in tree_row] for tree_row in read_file('input.txt')]
    scenic_scores = [[0 for tree in tree_row] for tree_row in trees]

    forest_edge_length = len(trees)

    for tree_x in range(0, forest_edge_length):
        for tree_y in range(0, forest_edge_length):
            tree_size = trees[tree_x][tree_y]
            scenic_score = 1

            for direction in Direction:
                x = tree_x
                y = tree_y
                direction_scenic_score = 0
                
                while True:
                    x += direction.value[0]
                    y += direction.value[1]
                    if x < 0 or y < 0 or x >= forest_edge_length or y >= forest_edge_length:
                        # We are out of the forest
                        break
                    else:
                        scenic_tree_size = trees[x][y]
                        direction_scenic_score += 1
                        if scenic_tree_size >= tree_size:
                            # Tree is to high, we cannot see any more tree
                            break
                        else:
                            # Tree is below ours, we can see more trees
                            pass

                scenic_score *= max(1, direction_scenic_score)

            scenic_scores[tree_x][tree_y] = scenic_score

    #print_forest(trees)
    #print_forest(scenic_scores)
    print(max([max(row_scenic_score) for row_scenic_score in scenic_scores]))


part1()
#part2()
