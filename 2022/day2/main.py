#!/usr/bin/python3

from enum import Enum

class Move(Enum):
    PIERRE = 1
    FEUILLE = 2
    CISEAUX = 3

class Result(Enum):
    LOST = 0
    DRAW = 3
    WIN = 6

def read_file(filename):
    with open(filename) as f:
        return [row.strip() for row in f.readlines()]

def compute_score(move: Move, result: Result):
    return move.value + result.value

def part1():
    rows = read_file('input.txt')

    def decrypt_move(encrypted_move):
        match encrypted_move:
            case 'X' | 'A':
                return Move.PIERRE
            case 'Y' | 'B':
                return Move.FEUILLE
            case 'Z' | 'C':
                return Move.CISEAUX

    score = 0
    for row in rows:
        moves = [decrypt_move(encrypted_move) for encrypted_move in row.split(' ')]

        match moves:
            case [Move.PIERRE, Move.CISEAUX] | [Move.FEUILLE, Move.PIERRE] | [Move.CISEAUX, Move.FEUILLE]:
                result = Result.LOST
            case [m1, m2] if m1 == m2:
                result = Result.DRAW
            case [Move.PIERRE, Move.FEUILLE] | [Move.FEUILLE, Move.CISEAUX] | [Move.CISEAUX, Move.PIERRE]:
                result = Result.WIN

        score += compute_score(moves[1], result)

    print(score)

def part2():
    rows = read_file('input.txt')

    def decrypt_move(encrypted_move):
        match encrypted_move:
            case 'A':
                return Move.PIERRE
            case 'B':
                return Move.FEUILLE
            case 'C':
                return Move.CISEAUX

    def decrypt_result(encrypted_result):
        match encrypted_result:
            case 'X':
                return Result.LOST
            case 'Y':
                return Result.DRAW
            case 'Z':
                return Result.WIN

    score = 0
    for row in rows:
        encrypted_move, encrypted_result = row.split(' ')
        opponent_move = decrypt_move(encrypted_move)
        result = decrypt_result(encrypted_result)

        match [opponent_move, result]:
            case [Move.PIERRE, Result.DRAW] | [Move.FEUILLE, Result.LOST] | [Move.CISEAUX, Result.WIN]:
                my_move = Move.PIERRE
            case [Move.PIERRE, Result.WIN] | [Move.FEUILLE, Result.DRAW] | [Move.CISEAUX, Result.LOST]:
                my_move = Move.FEUILLE
            case [Move.PIERRE, Result.LOST] | [Move.FEUILLE, Result.WIN] | [Move.CISEAUX, Result.DRAW]:
                my_move = Move.CISEAUX

        score += compute_score(my_move, result)

    print(score)
    
part1()
part2()
