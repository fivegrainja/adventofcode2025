#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

from pathlib import Path

def get_line_joltage(digits: list[int]) -> int:
    """ Select two digits, A and B, from input list that together as "AB" make
        the largest possible integer. A must come before B in the list.
        Return the integer AB
    """
    first_digit_i = 0
    second_digit_i = 1
    final_i = len(digits) - 1
    for i in range(1, len(digits)):
        if i < final_i and digits[i] > digits[first_digit_i]:
            first_digit_i = i
            second_digit_i = i + 1
        elif digits[i] > digits[second_digit_i]:
            second_digit_i = i
    result = (10 * digits[first_digit_i]) + digits[second_digit_i]
    return result

def index_of_max(digits: list[int]) -> int:
    """ Return the index of the largest number in the input list.
    """
    max_i = 0
    for i in range(1, len(digits)):
        if digits[i] > digits[max_i]:
            max_i = i
    return max_i

def get_fancy_line_joltage(digits: list[int], num_digits_needed: int = 12) -> int:
    # Find the first occurance of the largest digit within digits[:-num_digits_needed]
    # Then append to that the result a recursively calling this with
    # all the digits after the the one we pick and num_digits_needed-1
    my_digit_i = index_of_max(digits if num_digits_needed == 1 else digits[:-(num_digits_needed-1)])
    if num_digits_needed > 1:
        joltage_to_right = get_fancy_line_joltage(digits[my_digit_i+1:], num_digits_needed-1)
    else:
        joltage_to_right = ''
    result = int(str(digits[my_digit_i]) + str(joltage_to_right))
    if len(str(result)) != num_digits_needed:
        raise Exception('We should never return more digits than requested')
    return result

def add_joltages(lines: list[str], calculator: callable) -> int:
    total = 0
    for line in lines:
        digits = [int(c) for c in line]
        total += calculator(digits)
    return total

for calculator in (('Part One', get_line_joltage), ('Part Two', get_fancy_line_joltage)):
    print(calculator[0])
    for input_file in ('test.txt', 'input.txt'):
        with open(Path(__file__).resolve().parent / input_file, 'r') as file:
            lines = [s for l in file.readlines() if (s := l.strip())]
        total = add_joltages(lines, calculator[1])
        print(f'For {input_file}:')
        print(f'  total: {total}')
    print()

