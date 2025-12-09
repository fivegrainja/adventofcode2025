#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = [
#    "shapely",
# ]
# ///

from pathlib import Path
from shapely.geometry import Polygon, box

def part_one(lines: list[str]) -> int:
    red_tiles = [tuple(map(int, s.strip().split(','))) for l in lines if (s := l.strip())]
    max_size = 0
    for a_i, a in enumerate(red_tiles):
        for b_i, b in enumerate(red_tiles[a_i + 1:]):
            width = abs(a[0] - b[0]) + 1
            height = abs(a[1] - b[1]) + 1
            size = width * height
            if size > max_size:
                max_size = size
    return max_size

def part_two(lines: list[str]) -> int:
    red_tiles = [tuple(map(int, s.strip().split(','))) for l in lines if (s := l.strip())]
    polygon = Polygon(red_tiles)
    max_size = 0
    for a_i, a in enumerate(red_tiles):
        for b_i, b in enumerate(red_tiles[a_i + 1:]):
            min_x = min(a[0], b[0])
            max_x = max(a[0], b[0])
            min_y = min(a[1], b[1])
            max_y = max(a[1], b[1])
            size = (max_x - min_x + 1) * (max_y - min_y + 1)
            if size > max_size:
                rect = box(min_x, min_y, max_x, max_y)
                if rect.within(polygon):
                    max_size = size
    return max_size

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
        