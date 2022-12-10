#!/usr/bin/python3

from enum import Enum
from typing import Callable

def read_file(filename):
    with open(filename) as f:
        return [row.strip('\n') for row in f.readlines()]

def get_score_part1(cycle, v):
    return str(cycle * v) if (cycle + 20) % 40 == 0 else str(0)

def run_cycles(instructions, score_per_cycle: Callable[[int, int], str]):
    cycle = 1
    register = 1

    scores = []
    for instruction in instructions:
        instruction = instruction.split(' ')
        match instruction[0]:
            case 'addx':
                scores.append(score_per_cycle(cycle, register))
                scores.append(score_per_cycle(cycle + 1, register))
                register += int(instruction[1])
                cycle += 2
            case 'noop':
                scores.append(score_per_cycle(cycle, register))
                cycle += 1

    return scores

def part1():
    rows = read_file('input.txt')
    scores = run_cycles(rows, get_score_part1)
    print(sum([int(x) for x in scores]))

def get_pixel_part2(cycle, register):
    position = (cycle - 1) % 40
    return '#' if abs(position - register) <= 1 else '.'

def part2():
    rows = read_file('input.txt')
    crt = ''.join(run_cycles(rows, get_pixel_part2))

    print(crt[0:40])
    print(crt[40:80])
    print(crt[80:120])
    print(crt[120:160])
    print(crt[160:200])
    print(crt[200:240])

part1()
part2()
