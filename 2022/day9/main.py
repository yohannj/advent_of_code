#!/usr/bin/python3

from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

def read_file(filename):
    with open(filename) as f:
        return [row.strip('\n') for row in f.readlines()]

def parse_direction_from_char(c: str):
    match c:
        case 'U':
            return Direction.UP.value
        case 'D':
            return Direction.DOWN.value
        case 'L':
            return Direction.LEFT.value
        case 'R':
            return Direction.RIGHT.value
        case _:
            raise Exception('Unable to handle direction: ' + c)

def compute_new_tail_position(head, tail):
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        new_tail_y = tail[0]
        new_tail_x = tail[1]
        match head[0] - tail[0]:
            case y if y > 0:
                new_tail_y = tail[0] + 1
            case y if y < 0:
                new_tail_y = tail[0] - 1
            case _:
                pass

        match head[1] - tail[1]:
            case x if x > 0:
                new_tail_x = tail[1] + 1
            case x if x < 0:
                new_tail_x = tail[1] - 1
            case _:
                pass

        return (new_tail_y, new_tail_x)
    else:
        return tail

def get_tail_coords(knot_count, moves):
    knots = []
    for _ in range(0, knot_count):
        knots.append((0, 0))

    tail_coords = {knots[-1]}
    for row in moves:
        unparsed_direction, cnt = row.split(' ')

        direction = parse_direction_from_char(unparsed_direction)

        for _ in range(0, int(cnt)):
            knots[0] = (knots[0][0] + direction[0], knots[0][1] + direction[1])

            for i in range(1, knot_count):
                knots[i] = compute_new_tail_position(knots[i-1], knots[i])
            
            tail_coords.add(knots[-1])
    return tail_coords

def part1():
    rows = read_file('input.txt')
    tail_coords = get_tail_coords(2, rows)
    print(len(tail_coords))

def part2():
    rows = read_file('input.txt')
    tail_coords = get_tail_coords(10, rows)
    print(len(tail_coords))


part1()
part2()
