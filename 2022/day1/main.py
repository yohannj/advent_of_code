#!/usr/bin/python3

def read_file(filename):
    with open(filename) as f:
        return f.read()

def compute_total_elf_calories(elf_calories):
    return sum([int(calorie) for calorie in elf_calories])

def topK_elf_calories(k):
    full_text = read_file('input.txt')
    calories_str = [elf_calories_str.strip().split('\n') for elf_calories_str in full_text.split('\n\n')]
    elf_total_calories = [compute_total_elf_calories(calories) for calories in calories_str]
    elf_total_calories.sort()
    return elf_total_calories[-k:]

def part1():
    print(sum(topK_elf_calories(1)))

def part2():
    print(sum(topK_elf_calories(3)))
    
part1()
part2()
