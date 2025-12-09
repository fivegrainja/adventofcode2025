#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

from pathlib import Path
import functools

def part_one(lines: list[str]) -> int:
    beams = set([lines[0].index('S')])
    num_splits = 0
    for line in lines[1:]:
        next_beams = set()
        for b in beams:
            if line[b] == '^':
                next_beams.update([b - 1, b + 1])
                num_splits += 1
            else:
                next_beams.add(b)
        beams = next_beams
    return num_splits

@functools.lru_cache
def count_splits(lines: tuple[str], beam_loc: int, line_num: int) -> int:
    if line_num == len(lines):
        return 0
    if lines[line_num][beam_loc] == '.':
        return count_splits(lines, beam_loc, line_num + 1)
    if lines[line_num][beam_loc] == '^':
        return (1 
            + count_splits(lines, beam_loc - 1, line_num + 1)
            + count_splits(lines, beam_loc + 1, line_num + 1))
    raise Exception('Should not get here')

def part_two(lines: tuple[str]) -> int:
    beam_loc = lines[0].index('S')
    result = 1 + count_splits(lines, beam_loc, 1)
    return result

if __name__ == '__main__':      
    for input_file in ('test.txt', 'input.txt'):
        with open(Path(__file__).resolve().parent / input_file, 'r') as file:
            # Use a tuple instead of list so that lru_cache can hash it
            lines = tuple([s for l in file.readlines() if (s := l.strip())])
        part_one_result = part_one(lines)
        print(f'  Part one: {part_one_result}')
        part_two_result = part_two(lines)
        print(f'  Part two: {part_two_result}')
        print()

