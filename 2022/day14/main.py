#!/usr/bin/python3

from enum import Enum
from typing import List

class Cell(Enum):
    EMPTY = '.'
    SAND = 'o'
    WALL = '#'
    DEAD = '*'

def read_file(filename) -> List[str]:
    with open(filename) as f:
        return [row.strip('\n') for row in f.readlines()]

def get_map(filename, bottom_cell: Cell, extend_cell: Cell) -> List[List[Cell]]: 
    worldmap: List[List[Cell]] = []
    input_rows = read_file(filename)

    min_x = 500
    max_x = 500
    max_y = 0
    for input_row in input_rows:
        coords = [[int(c) for c in coords.split(',')] for coords in input_row.split(' -> ')]
        for coord in coords:
            x, y = coord
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            max_y = max(y, max_y)

    for y in range(0, max_y + 2):
        worldmap_row: List[Cell] = []
        for x in range(0, 2 * max_x + 2):
            c = Cell.EMPTY if min_x <= x and x <= max_x and y <= max_y else extend_cell
            worldmap_row.append(c)
        worldmap.append(worldmap_row)
    
    worldmap_row = []
    for x in range(0, 2 * max_x + 2):
        worldmap_row.append(bottom_cell)
    worldmap.append(worldmap_row)

    for input_row in input_rows:
        coords = [[int(c) for c in coords.split(',')] for coords in input_row.split(' -> ')]
        cur_x, cur_y = coords[0]

        for coord in coords[1:]:
            to_x, to_y = coord
            if to_x == cur_x:
                dx = 0
                if to_y < cur_y:
                    dy = -1
                else:
                    dy = 1
            else:
                dy = 0
                if to_x < cur_x:
                    dx = -1
                else:
                    dx = 1

            while (cur_x, cur_y) != (to_x, to_y):
                worldmap[cur_y][cur_x] = Cell.WALL
                cur_x += dx
                cur_y += dy

            worldmap[cur_y][cur_x] = Cell.WALL

    return worldmap

def simulate_sand_drops(worldmap: List[List[Cell]]) -> int:
    sand_count = 0
    drop_sand = True
    sand_x, sand_y = 500, 0
    while drop_sand:
        for dx in [0, -1, 1]:
            match worldmap[sand_y + 1][sand_x + dx]:
                case Cell.DEAD | Cell.EMPTY:
                    break

        match worldmap[sand_y + 1][sand_x + dx]:
            case Cell.DEAD:
                drop_sand = False
            case Cell.EMPTY:
                sand_x += dx
                sand_y += 1
            case Cell.WALL | Cell.SAND:
                sand_count += 1
                worldmap[sand_y][sand_x] = Cell.SAND

                if sand_x == 500 and sand_y == 0:
                    # There is sand up to where the source comes from
                    drop_sand = False

                sand_x, sand_y = 500, 0

    #print('\n'.join([''.join([c.value for c in row]) for row in worldmap]))
    return sand_count

def part1() -> None:
    worldmap = get_map('input.txt', Cell.DEAD, Cell.DEAD)
    print(simulate_sand_drops(worldmap))

def part2() -> None:
    worldmap = get_map('input.txt', Cell.WALL, Cell.EMPTY)
    print(simulate_sand_drops(worldmap))

part1()
part2()
