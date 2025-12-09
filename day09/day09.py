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
    corners = []
    for a_i, a in enumerate(red_tiles):
        for b_i, b in enumerate(red_tiles[a_i + 1:]):
            width = abs(a[0] - b[0]) + 1
            height = abs(a[1] - b[1]) + 1
            size = width * height
            if size > max_size:
                max_size = size
                corners = [a, b]
    return max_size

# def is_filled(red_tiles: list[tuple[int, int]], a: tuple[int, int], b: tuple[int, int]) -> bool:
#     # Make sure there is no red tile internal to this rectangle (on the edge
#     # of the rectangle is ok))
#     min_x = min(a[0], b[0])
#     max_x = max(a[0], b[0])
#     min_y = min(a[1], b[1])
#     max_y = max(a[1], b[1])
#     for tile in red_tiles:
#         if (min_x < tile[0] < max_x) and (min_y < tile[1] < max_y):
#             return False
#     # Now make sure all tiles in the rectangle are red
#     leftmost = a if a[0] < b[0] else b
#     rightmost = b if a[0] < b[0] else a
#     if leftmost[1] <= rightmost[1]:
#         # left is upper left, right is lower right
#         upper_right = (rightmost[0], leftmost[1])
#         # Ensure there is a red tile with x >= upper_right.x and
#         # y <= upper_right.y
#         for red_tile in red_tiles:
#             if red_tile in (a, b):
#                 continue
#             if red_tile[0] >= upper_right[0] and red_tile[1] <= upper_right[1]:
#                 break
#         else:
#             # did not find a suitable red tile above/right of upper_right
#             return False
#         lower_left = (leftmost[0], rightmost[1])
#         # Ensure there is a red tile with x <= lower_left.x and
#         # y >= lower_left.y
#         for red_tile in red_tiles:
#             if red_tile in (a, b):
#                 continue
#             if red_tile[0] <= lower_left[0] and red_tile[1] >= lower_left[1]:
#                 break
#         else:
#             # did not find a suitable red tile below/left of lower_left
#             return False
#     else:
#         # left is lower left, right is upper right
#         lower_right = (rightmost[0], leftmost[1])
#         # Ensure there is a red tile with x >= lower_right.x and
#         # y >= lower_right.y
#         for red_tile in red_tiles:
#             if red_tile in (a, b):
#                 continue
#             if red_tile[0] >= lower_right[0] and red_tile[1] >= lower_right[1]:
#                 break
#         else:
#             # did not find a suitable red tile below/right of lower_right
#             return False
#         upper_left = (leftmost[0], rightmost[1])
#         # Ensure there is a red tile with x <= upper_left.x and
#         # y <= upper_left.y
#         for red_tile in red_tiles:
#             if red_tile in (a, b):
#                 continue
#             if red_tile[0] <= upper_left[0] and red_tile[1] <= upper_left[1]:
#                 break
#         else:
#             # did not find a suitable red tile above/left of upper_left
#             return False
#     return True

# def part_two(lines: list[str]) -> int:
#     red_tiles = [tuple(map(int, s.strip().split(','))) for l in lines if (s := l.strip())]
#     max_size = 0
#     corners = []
#     for a_i, a in enumerate(red_tiles):
#         for b_i, b in enumerate(red_tiles[a_i + 1:]):
#             width = abs(a[0] - b[0]) + 1
#             height = abs(a[1] - b[1]) + 1
#             size = width * height
#             if size > max_size:
#                 # Ensure that it's filled with green
#                 if is_filled(red_tiles, a, b):
#                     max_size = size
#                     corners = [a, b]
#     print(corners)
#     return max_size

# 4619863120 is too high
# 4620005060 is too high (of course)

def part_two(lines: list[str]) -> int:
    red_tiles = [tuple(map(int, s.strip().split(','))) for l in lines if (s := l.strip())]
    polygon = Polygon(red_tiles)
    max_size = 0
    corners = []
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
                    corners = [a, b]
    print(corners)
    return max_size


if __name__ == '__main__':      
    for input_file in ('test.txt', 'input.txt'):
    # for input_file in ('input.txt',):
        print(f'{input_file}:')
        with open(Path(__file__).resolve().parent / input_file, 'r') as file:
            lines = [s for l in file.readlines() if (s := l.strip())]
        result = part_one(lines)
        print(f'  Part one: {result}')
        result = part_two(lines)
        print(f'  Part two: {result}')
        print()
        