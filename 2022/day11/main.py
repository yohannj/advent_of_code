#!/usr/bin/python3

from functools import reduce
import re

class Monkey:
    def __init__(self, id: int, starting_items: list[int], worryness_lambda: str, throwing_to_monkey_id_lambda: str, modulo: int):
        self.id = id
        self.starting_items = starting_items
        self.worryness_lambda = worryness_lambda
        self.throwing_to_monkey_id_lambda = throwing_to_monkey_id_lambda
        self.modulo = modulo

    def __str__(self):
        return f'Monkey {self.id} => Items: {self.starting_items}, Worryness: {self.worryness_lambda}, Throws: {self.throwing_to_monkey_id_lambda}'
    
    def __repr__(self):
        return self.__str__()

def print_monkeys(monkeys: list[Monkey]):
    print('\n'.join([str(monkey) for monkey in monkeys]))

def read_file(filename):
    with open(filename) as f:
        return f.read()

def input_parse(input) -> list[Monkey]:
    input_parser_regex = re.compile(
        r"""Monkey (?P<MonkeyId>\d+):\n.*?: (?P<StartingItems>.+)+\n.*?= (?P<Operation>.+)\n.*?: divisible by (?P<IfCondition>\d+)\n.*?monkey (?P<MonkeyIfTrue>\d+)\n.*?monkey (?P<MonkeyIfFalse>\d+)\n"""
    )

    monkeys = []
    a = input_parser_regex.finditer(input)
    for monkey in a:
        monkeys.append(
            Monkey(
                id = int(monkey.group('MonkeyId')),
                starting_items = [int(item) for item in monkey.group('StartingItems').split(', ')],
                worryness_lambda = monkey.group('Operation'),
                throwing_to_monkey_id_lambda = monkey.group('MonkeyIfTrue') + ' if worryness % ' + monkey.group('IfCondition') + ' == 0 else ' + monkey.group('MonkeyIfFalse'),
                modulo = int(monkey.group('IfCondition'))
            )
        )

    return monkeys

def get_inspection_count(monkeys, worryness_control_lambda, round_cnt):
    inspection_count_by_monkey = [0 for _ in monkeys]
    for _ in range(0, round_cnt):
        for monkey in monkeys:
            while monkey.starting_items:
                inspection_count_by_monkey[monkey.id] = inspection_count_by_monkey[monkey.id] + 1
                old = monkey.starting_items.pop(0)
                worryness = eval('(' + monkey.worryness_lambda + ') ' + worryness_control_lambda)
                item_throwed_towards_monkey_id = eval(monkey.throwing_to_monkey_id_lambda)
                monkeys[item_throwed_towards_monkey_id].starting_items.append(worryness)

    return inspection_count_by_monkey

def get_top2(l: list[int]):
    top1 = max(l)
    top2 = sorted(l)[-2]

    return [top1, top2]

def part1():
    monkeys = input_parse(read_file('input.txt'))
    inspection_count_by_monkey = get_inspection_count(monkeys, '// 3', 20)
    top1, top2 = get_top2(inspection_count_by_monkey)
    print(top1 * top2)

def part2():
    monkeys = input_parse(read_file('input.txt'))
    modulo = reduce(lambda x1, x2: x1 * x2, [monkey.modulo for monkey in monkeys])

    inspection_count_by_monkey = get_inspection_count(monkeys, '% ' + str(modulo), 10000)
    top1, top2 = get_top2(inspection_count_by_monkey)
    print(top1 * top2)

part1()
part2()
