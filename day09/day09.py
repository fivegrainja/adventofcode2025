#! /usr/bin/env python3

def part_one(lines: list[str]) -> int:
    pass

def part_two(lines: list[str]) -> int:
    pass

if __name__ == '__main__':      
    for input_file in ('test.txt',): #'input.txt'):
        print(f'{input_file}:')
        with open(input_file, 'r') as file:
            lines = [s for l in file.readlines() if (s := l.strip())]
        result = part_one(lines)
        print(f'  Part one: {result}')
        result = part_two(lines)
        print(f'  Part two: {result}')
        print()
        