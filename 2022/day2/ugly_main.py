#!/usr/bin/python3

from enum import Enum

class MyMove(Enum):
    X = [1, 0]
    Y = [2, 3]
    Z = [3, 6]

class Result(Enum):
    AX = [3, 3]
    AY = [6, 1]
    AZ = [0, 2]
    BX = [0, 1]
    BY = [3, 2]
    BZ = [6, 3]
    CX = [6, 2]
    CY = [0, 3]
    CZ = [3, 1]

def read_file(filename):
    with open(filename) as f:
        return [row.strip() for row in f.readlines()]

def row_score(row, idx):
    opponent_move, my_move = row.split(' ')
    move_score = MyMove[my_move].value[idx]
    battle_score = Result[opponent_move + my_move].value[idx]

    return move_score + battle_score

def compute_score(idx):
    rows = read_file('input.txt')
    return [row_score(row, idx) for row in rows]

def part1():
    print(sum(compute_score(0)))

def part2():
    print(sum(compute_score(1)))
    
part1()
part2()
