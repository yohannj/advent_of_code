#!/usr/bin/python3

from typing import List

def read_file(filename) -> List[str]:
    with open(filename) as f:
        return [row.strip('\n') for row in f.readlines()]

def part1() -> None:
    pass

def part2() -> None:
    pass

part1()
part2()
