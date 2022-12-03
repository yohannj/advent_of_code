#!/usr/bin/python3

def read_file(filename):
    with open(filename) as f:
        return [row.strip() for row in f.readlines()]

def get_compartments(row):
    middle_index = int(len(row)/2)
    return [
        {x for x in row[middle_index:]},
        {x for x in row[:middle_index]}
    ]

def lowercase_score(letter):
    return ord(letter) - ord('a') + 1

def uppercase_score(letter):
    return ord(letter) - ord('A') + 27

def letter_score(letter):
    if letter.islower():
        return lowercase_score(letter)
    else:
        return uppercase_score(letter)

def row_score(row):
    c1, c2 = get_compartments(row)
    return letter_score(c1.intersection(c2).pop())

def part1():
    print(sum([row_score(row) for row in read_file('input.txt')]))

def part2():
    rows = read_file('input.txt')
    total_score = 0
    for i in range(0, len(rows), 3):
        row1 = {x for x in rows[i]}
        row2 = {x for x in rows[i+1]}
        row3 = {x for x in rows[i+2]}

        letter_in_common = (row1 & row2 & row3).pop()
        total_score += letter_score(letter_in_common)
    
    print(total_score)


part1()
part2()
