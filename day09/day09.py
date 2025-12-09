#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

from pathlib import Path

def part_one(lines: list[str]) -> int:
    red_tiles = [tuple(map(int, s.strip().split(','))) for l in lines if (s := l.strip())]
    # print(red_tiles)
    # import sys; sys.exit(0)
    max_size = 0
    corners = []
    for a_i, a in enumerate(red_tiles):
        for b_i, b in enumerate(red_tiles[a_i + 1:]):
            width = abs(a[0] - b[0] + 1)
            height = abs(a[1] - b[1] + 1)
            size = width * height
            # print(f'Considering {a} to {b}: size {size} ({width} x {height})')
            if size > max_size:
                max_size = size
                corners = [a, b]
    return max_size

def part_two(lines: list[str]) -> int:
    pass

if __name__ == '__main__':      
    for input_file in ('test.txt', 'input.txt'):
        print(f'{input_file}:')
        with open(Path(__file__).resolve().parent / input_file, 'r') as file:
            lines = [s for l in file.readlines() if (s := l.strip())]
        result = part_one(lines)
        print(f'  Part one: {result}')
        result = part_two(lines)
        print(f'  Part two: {result}')
        print()
        