#!/usr/bin/python3

import typing

def read_file(filename):
    with open(filename) as f:
        return [row.strip() for row in f.readlines()]

def gpt(start1: int, end1: int, start2: int, end2: int):
    if (start1 <= start2 <= end1) and (end1 <= end2):
        return True
    elif (start2 <= start1 <= end2) and (end2 <= end1):
        return True
    else:
        return False

def is_fully_contained(min1: int, max1: int, min2: int, max2: int):
    one_include_two = min1 <= min2 and max1 >= max2
    two_include_one = min2 <= min1 and max2 >= max1
    return one_include_two or two_include_one

def is_partially_contained(min1: int, max1: int, min2: int, max2: int):
    return (min1 <= min2 <= max1) or (min1 <= max2 <= max1) or (min2 <= min1 <= max2) or (min2 <= max1 <= max2)

def is_row_redundant(row: str, f: typing.Callable[[int, int, int, int], bool]):
    p1, p2 = row.split(',')
    min1, max1 = map(int, p1.split('-'))
    min2, max2 = map(int, p2.split('-'))

    return f(min1, max1, min2, max2)

def part1gpt():
    print(sum([1 for x in read_file('input.txt') if is_row_redundant(x, gpt)]))

def part1():
    print(sum([1 for x in read_file('input.txt') if is_row_redundant(x, is_fully_contained)]))

def part2():
    print(sum([1 for x in read_file('input.txt') if is_row_redundant(x, is_partially_contained)]))

part1gpt()
part1()
part2()
