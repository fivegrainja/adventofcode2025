#! /usr/bin/env python3

import math

if __name__ == '__main__':      
    for input_file in ('test.txt', 'input.txt'):
        with open(input_file, 'r') as file:
            lines = file.readlines()
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
            # print(f'  line {i}: {result}')
            total += result
        print(f'  Part one: {total}')
        print()

