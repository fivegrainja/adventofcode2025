#! /usr/bin/env python3


def is_bad_id_part_one(i: int) -> bool:
    i_str = str(i)
    i_len = len(i_str)
    if i_len % 2 == 0:
        if i_str[:i_len//2] == i_str[i_len//2:]:
            return True
    return False

def is_bad_id_part_two(i: int) -> bool:
    i_str = str(i)
    i_len = len(i_str)
    for sublength in range(1, (i_len // 2) + 1):
        if i_len % sublength == 0:
            substr = i_str[:sublength]
            if substr * (i_len//sublength) == i_str:
                return True
    return False

def get_bad_ids_in_range(range_start: int, range_end: int, evaluator: callable) -> list[int]:
    bad_ids = []
    for i in range(range_start, range_end+1):
        if evaluator(i):
            bad_ids.append(i)
    # print(f'For range {range_start}-{range_end}')
    # print(f'  bad_ids is {bad_ids}')
    # print(f'  num bad is {len(bad_ids)}')
    return bad_ids

def total_bad_ids(ranges: list[int, int], evaluator: callable) -> int:
    bad_ids = []
    for range in ranges:
        bad_ids.extend(get_bad_ids_in_range(range[0], range[1], evaluator))
    # print(f'bad_ids is {bad_ids}')
    total = sum(bad_ids)
    # print(f'Total bad ids is {total}')
    return total


for input_file in ('test.txt', 'input.txt'):
    print(input_file)
    with open(input_file, 'r') as file:
        i: str = file.readline().strip()
    ranges: list[list[int, int]] =  [[int(z) for z in r.split('-')] for r in i.split(',')]
    total = total_bad_ids(ranges, is_bad_id_part_one)
    print(f'  Part one: {total}')
    total = total_bad_ids(ranges, is_bad_id_part_two)
    print(f'  Part two: {total}')
    print

# Part 1: 38310256125
# Part 2: 58961152806
