#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = [
# ]
# ///

from pathlib import Path
# from functools import reduce, lru_cache, cmp_to_key
# from queue import PriorityQueue
# from typing import Optional
from collections import deque #, Counter
# from itertools import chain

def region_fits_shapes(region: tuple[int, int, tuple], shapes: dict[int, list[str]]) -> bool:
    area = region[0] * region[1]
    num_shapes = sum(region[2])
    if num_shapes * 9 <= area:
        return True
    return False

def part_one(lines: list[str]) -> int:
    shapes, regions = parse(lines)
    result = sum([region_fits_shapes(region, shapes) for region in regions])
    return result

def part_two(lines: list[str]) -> int:
    return None

def parse(lines: list[str]) -> tuple[list[list], list[tuple[int, int, tuple]]]:
    lines = deque(lines)
    shapes = {}
    while ('x' not in (line := lines.popleft())):
        if (l := line.strip()):
            # Start reading a new shape
            shape = []
            for i in range(3):
                shape.append(lines.popleft().strip())
            shapes[int(l.strip(':'))] = shape
    # Now read the regions
    regions: list[tuple[int, int, tuple]] = []
    try:
        while (line := lines.popleft().strip()):
            parts = line.split(':')
            height, width = (int(x) for x in parts[0].split('x'))
            counts = (int(x) for x in parts[1].split())
            regions.append((height, width, counts))
    except IndexError:
        pass
    return (shapes, regions)

if __name__ == '__main__':      
    for input_file in ('test.txt', 'input.txt'):
        print(f'{input_file}:')
        with open(Path(__file__).resolve().parent / input_file, 'r') as file:
            lines = [s for l in file.readlines() if (s := l.strip())]
        result = part_one(lines)
        print(f'  Part one: {result}')
        # result = part_two(lines)
        # print(f'  Part two: {result}')
        # print()
        