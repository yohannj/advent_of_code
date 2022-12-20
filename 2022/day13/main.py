#!/usr/bin/python3

from functools import cmp_to_key
from typing import Any

class Packet():
    packet: Any
    def __init__(self, packet: Any) -> None:
        self.packet = packet

    def __str__(self) -> str:
        return str(self.packet)

    def __repr__(self) -> str:
        return str(self.packet)

    def __lt__(self, other) -> int:
        items1 = self.packet
        items2 = other.packet

        min_list_size = min(len(items1), len(items2))
        for idx in range(min_list_size):
            item1 = items1[idx]
            item2 = items2[idx]

            if isinstance(item1, int) and isinstance(item2, int):
                diff = item1 - item2
            elif isinstance(item1, int):
                diff = Packet([item1]).__lt__(Packet(item2))
            elif isinstance(item2, int):
                diff = Packet(item1).__lt__(Packet([item2]))
            else:
                diff = Packet(item1).__lt__(Packet(item2))

            if diff < 0:
                return -1
            elif diff == 0:
                # We must continue to check the next element
                pass
            else:
                return 1

        return len(items1) - len(items2)

def read_file(filename) -> str:
    with open(filename) as f:
        return f.read()

def part1() -> None:
    inputs = [[Packet(eval(s)) for s in i.split('\n')] for i in read_file('test.txt').split('\n\n')]

    res = 0
    for idx in range(len(inputs)):
        diff = inputs[idx][0] < inputs[idx][1]
        if diff < 0:
            res += idx + 1
    print(res)

def part2() -> None:
    all_rows = [Packet(eval(s)) for s in filter(lambda x: len(x) > 0, read_file('input.txt').split('\n'))]
    p1 = Packet([[2]])
    p2 = Packet([[6]])
    all_rows.append(p1)
    all_rows.append(p2)
    
    sorted_rows = sorted(all_rows, key=cmp_to_key(Packet.__lt__))
    print((sorted_rows.index(p1)+1) * (sorted_rows.index(p2)+1))
    
part1()
part2()
