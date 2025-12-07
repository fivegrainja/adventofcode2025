#! /usr/bin/env python3

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

if __name__ == '__main__':      
    for input_file in ('test.txt', 'input.txt'):
        with open(input_file, 'r') as file:
            lines = [s for l in file.readlines() if (s := l.strip())]
        part_one_result = part_one(lines)
        print(f'  Part one: {part_one_result}')
        # part_two_result = part_two(lines)
        # print(f'  Part two: {part_two_result}')
        print()

