#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

from pathlib import Path

def count_movable_rolls(lines: list[str]) -> int:
    num_movable = 0
    for row_i in range(len(lines)):
        for col_i in range(len(lines[row_i])):
            if lines[row_i][col_i] != '@':
                continue
            num_adjacent_rolls = 0
            num_lines = len(lines)
            line_length = len(lines[0])
            # row above
            if row_i > 0:
                if col_i > 0 and lines[row_i-1][col_i-1] == '@':
                    num_adjacent_rolls += 1
                if lines[row_i-1][col_i] == '@':
                    num_adjacent_rolls += 1
                if col_i < line_length - 1 and lines[row_i-1][col_i+1] == '@':
                    num_adjacent_rolls  += 1
            # row of
            if col_i > 0 and lines[row_i][col_i-1] == '@':
                num_adjacent_rolls += 1
            if col_i < line_length - 1 and lines[row_i][col_i+1] == '@':
                num_adjacent_rolls  += 1
            # row below
            if row_i < num_lines - 1:
                if col_i > 0 and lines[row_i+1][col_i-1] == '@':
                    num_adjacent_rolls += 1
                if lines[row_i+1][col_i] == '@':
                    num_adjacent_rolls += 1
                if col_i < line_length - 1 and lines[row_i+1][col_i+1] == '@':
                    num_adjacent_rolls  += 1
            if num_adjacent_rolls < 4:
                num_movable += 1
    return num_movable

def remove_rolls(lines: list[str]) -> int:
    lines = [list(row) for row in lines]
    num_removed = 0
    do_another_pass = True
    while do_another_pass:
        do_another_pass = False
        for row_i in range(len(lines)):
            for col_i in range(len(lines[row_i])):
                if lines[row_i][col_i] != '@':
                    continue
                num_adjacent_rolls = 0
                num_lines = len(lines)
                line_length = len(lines[0])
                # row above
                if row_i > 0:
                    if col_i > 0 and lines[row_i-1][col_i-1] == '@':
                        num_adjacent_rolls += 1
                    if lines[row_i-1][col_i] == '@':
                        num_adjacent_rolls += 1
                    if col_i < line_length - 1 and lines[row_i-1][col_i+1] == '@':
                        num_adjacent_rolls  += 1
                # row of
                if col_i > 0 and lines[row_i][col_i-1] == '@':
                    num_adjacent_rolls += 1
                if col_i < line_length - 1 and lines[row_i][col_i+1] == '@':
                    num_adjacent_rolls  += 1
                # row below
                if row_i < num_lines - 1:
                    if col_i > 0 and lines[row_i+1][col_i-1] == '@':
                        num_adjacent_rolls += 1
                    if lines[row_i+1][col_i] == '@':
                        num_adjacent_rolls += 1
                    if col_i < line_length - 1 and lines[row_i+1][col_i+1] == '@':
                        num_adjacent_rolls  += 1
                if num_adjacent_rolls < 4:
                    lines[row_i][col_i] = 'x'
                    num_removed += 1
                    do_another_pass = True
                    
    return num_removed

print(f'Part One:')
for input_file in ('test.txt', 'input.txt'):
    with open(Path(__file__).resolve().parent / input_file, 'r') as file:
        lines = [s for l in file.readlines() if (s := l.strip())]
        part_one = count_movable_rolls(lines)
        print(f'  {input_file}: {part_one}')

print(f'Part Two:')
for input_file in ('test.txt', 'input.txt'):
    with open(Path(__file__).resolve().parent / input_file, 'r') as file:
        lines = [s for l in file.readlines() if (s := l.strip())]
        part_two = remove_rolls(lines)
        print(f'  {input_file}: {part_two}')

