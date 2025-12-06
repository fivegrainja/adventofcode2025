#! /usr/bin/env python3

import math

def part_one(lines: list[str]) -> int:
    numbers = [[int(x) for x in line.strip().split()] for line in lines[:-1]]
    operations = lines[-1].strip().split()
    total = 0
    print(f'{input_file}:')
    for i in range(len(numbers[0])):
        if operations[i] == '+':
            op = sum
        elif operations[i] == '*':
            op = math.prod
        else:
            raise Exception('Problem understanding operation')
        result = op([row[i] for row in numbers])
        total += result
    return total

def part_two(lines: list[str]) -> int:
    operations = lines[-1].strip().split()
    lines = [l.strip('\n') + ' ' for l in lines[:-1]]
    line_length = len(lines[0])
    total = 0
    operands = []
    problem_num = 0
    for big_col_i in range(line_length):
        operand = ''.join([line[big_col_i] for line in lines]).strip()
        if operand == '':
            # We hit the end of this problem
            if operands:
                # This should always be the case, except for the first column
                print(f'operands is {operands}')
                op = sum if operations[problem_num] == '+' else math.prod
                result = op(operands)
                total += result
            else:
                raise Exception('Expected operands')
            problem_num += 1
            operands = []
        else:
            operands.append(int(operand))
    return total


if __name__ == '__main__':      
    for input_file in ('test.txt', 'input.txt'):
        with open(input_file, 'r') as file:
            lines = file.readlines()
        part_one_result = part_one(lines)
        print(f'  Part one: {part_one_result}')
        part_two_result = part_two(lines)
        print(f'  Part two: {part_two_result}')
        print()

