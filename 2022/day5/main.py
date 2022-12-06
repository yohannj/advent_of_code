#!/usr/bin/python3

import re
from typing import Dict

def read_file(filename):
    with open(filename) as f:
        return [row.strip('\n') for row in f.readlines()]

def part1():
    stacks: Dict[int, list] = {}
    input = read_file('input.txt')
    for row in input:
        if row[1] == '1':
            for v in stacks.values():
                v.reverse()
            break

        for idx in range(1, len(row), 4):
            c = row[idx]
            if c.isupper():
                stack_idx = (idx-1)//4 + 1
                currentStack = stacks.get(stack_idx, [])
                currentStack.append(c)
                stacks[stack_idx] = currentStack

    for row in input:
        match_res = re.search(r"^move (?P<nb_element>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)$", row)
        if match_res:
            from_stack = int(match_res.group('from_stack'))
            to_stack = int(match_res.group('to_stack'))
            for i in range(0, int(match_res.group('nb_element'))):
                stacks[to_stack].append(stacks[from_stack].pop(-1))

    print(''.join([stacks[i+1][-1] for i in range(len(stacks))]))

def part2():
    stacks: Dict[int, list] = {}
    input = read_file('input.txt')
    for row in input:
        if row[1] == '1':
            for v in stacks.values():
                v.reverse()
            break

        for idx in range(1, len(row), 4):
            c = row[idx]
            if c.isupper():
                stack_idx = (idx-1)//4 + 1
                currentStack = stacks.get(stack_idx, [])
                currentStack.append(c)
                stacks[stack_idx] = currentStack

    for row in input:
        match_res = re.search(r"^move (?P<nb_element>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)$", row)
        if match_res:
            from_stack = int(match_res.group('from_stack'))
            to_stack = int(match_res.group('to_stack'))

            for i in range(int(match_res.group('nb_element')), 0, -1):
                stacks[to_stack].append(stacks[from_stack].pop(-i))

    print(*[stacks[i+1][-1] for i in range(len(stacks))], sep = '')

part1()
part2()
