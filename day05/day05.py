#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

from pathlib import Path

def is_ingredient_fresh(fresh: list[(int, int)], ingredient: int) -> bool:
    for f in fresh:
        if f[0] <= ingredient <= f[1]:
            return True
    return False

def count_fresh_ingredients(fresh: list[(int, int)], ingredients: list[int]) -> int:
    count = 0
    for i in ingredients:
        if is_ingredient_fresh(fresh, i):
            count += 1
    return count

def count_fresh_ranges(fresh: list[(int, int)]) -> int:
    # The idea is ta sort the list of ranges by their starting value. This
    # ensures that as we consider them in order each new range will either
    # A) Start within the previous range, possibly going langer or
    # B) Start after the previuos range, with no overlap.
    fresh.sort(key=lambda f: f[0])
    # count is the running total of the number of valid id's we've considered.
    # We initial it with the length of the first range of ids
    count = fresh[0][1] - fresh[0][0] + 1
    # range_end is the size of the largest ingredient ID we've encountered
    # We initialize it to the end of the first range
    range_end = fresh[0][1]
    # Loop through all ranges after the first, incrementing count and range_end
    # as appropriate.
    for f in fresh[1:]:
        if f[0] <= range_end:
            # This range starts prior to our previous largest ID.
            if f[1] > range_end:
                # This range extends past the largest ID we've encountered so
                # far, so we are going to add these additional IDs to our count
                # and set range_end to be this new largest ID
                count += f[1] - range_end
                range_end = f[1]
        else:
            # No overlap between this range and previous ranges. We can add the
            # all IDs from this range to our count and let range_end to the end
            # of this range.
            count += f[1] - f[0] + 1
            range_end = f[1]
    return count
            
for input_file in ('test.txt', 'input.txt'):

    # Read fresh range lines into a list of tuples of 2 ints each.
    # Reach ingredient list into list of ints
    with open(Path(__file__).resolve().parent / input_file, 'r') as file:
        lines = file.readlines()
    separator_i = lines.index('\n')
    fresh_tuples = [l.strip().split('-') for l in lines[:separator_i]]
    fresh = [(int(f[0]), int(f[1])) for f in fresh_tuples]
    ingredient_lines = [s for l in lines[separator_i+1:] if (s := l.strip())]
    ingredients = [int(l) for l in ingredient_lines]

    num_fresh = count_fresh_ingredients(fresh, ingredients)
    print(f'{input_file}:')
    print(f'  part one: {num_fresh}')

    num_potentially_fresh = count_fresh_ranges(fresh)
    print(f'  part_two: {num_potentially_fresh}')

