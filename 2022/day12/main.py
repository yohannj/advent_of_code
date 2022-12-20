#!/usr/bin/python3

from enum import Enum
from typing import Callable, Dict, List, Tuple

from PIL import Image

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

def read_file(filename) -> List[str]:
    with open(filename) as f:
        return [row.strip('\n') for row in f.readlines()]

def parse_input(filename: str) -> Tuple[Tuple[int, int], Tuple[int, int], List[List[int]]]:
    height_map: List[List[int]] = []
    rows = read_file(filename)
    for y in range(0, len(rows)):
        row = rows[y]
        parsed_row = []
        for x in range(0, len(row)):
            c = row[x]
            match c:
                case 'S':
                    height = 0
                    start = (x, y)
                case 'E':
                    height = 25
                    end = (x, y)
                case default:
                    height = ord(default) - ord('a')
            parsed_row.append(height)
        height_map.append(parsed_row)

    return (start, end, height_map)

def path_finder(start: Tuple[int, int], end_condition: Callable[[Tuple[int, int]], bool], height_map: List[List[int]]) -> List[Tuple[int, int]]:
    previous: Dict[Tuple[int, int], Tuple[int, int]] = {}
    to_check = [start]

    while to_check:
        cell = to_check.pop(0)
        if end_condition(cell):
            path = [cell]
            while path[-1] in previous:
                path.append(previous[path[-1]])
            return path
        
        current_height = height_map[cell[1]][cell[0]]
        for dir in Direction:
            new_x = cell[0] + dir.value[0]
            new_y = cell[1] + dir.value[1]
            new_cell = (new_x, new_y)

            coords_in_map = new_x >= 0 and new_y >= 0 and new_y < len(height_map) and new_x < len(height_map[0])
            if coords_in_map and height_map[new_y][new_x] + 1 >= current_height and new_cell not in previous and new_cell != start:
                to_check.append((new_x, new_y))
                previous[new_cell] = cell

    raise Exception('''Couldn't find a way from Start to End''')

def part1() -> None:
    start, end, height_map = parse_input('input.txt')
    path = path_finder(end, lambda t: t == start, height_map)
    print(len(path) - 1)

def part2() -> None:
    _, end, height_map = parse_input('input.txt')
    path = path_finder(end, lambda t: height_map[t[1]][t[0]] == 0, height_map)
    print(len(path) - 1)

part1()
part2()

def get_rgb(red_value: int, green_value: int, blue_value: int):
    return 256 * 256 * blue_value + 256 * green_value + red_value

def generate_forest_png() -> None:
    start, end, height_map = parse_input('input.txt')
    forest_aoa = [[int(tree) for tree in tree_row] for tree_row in height_map]
    forest = [int(tree) for tree_row in forest_aoa for tree in tree_row]
    width = len(forest_aoa[0])
    height = len(forest_aoa)
    
    image = Image.new('RGB', (width, height))
    pixels = [get_rgb(0, 10 * tree, 0) for tree in forest]

    path = path_finder(end, lambda t: t == start, height_map)
    for x, y in path:
        pixels[y * width + x] += get_rgb(255, 0, 0)

    image.putdata(pixels)
    image.save('mountain.png')

generate_forest_png()