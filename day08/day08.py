#! /usr/bin/env python3

import math
import networkx as nx

def part_one_and_two(lines: list[str], num_to_connect: int) -> tuple[int, int]:
    nodes: list[tuple[int, int, int]] = [tuple(map(int, l.split(','))) for l in lines]
    pairs: tuple[float, tuple[int, int, int], tuple[int, int, int]] = []
    for i_a, a in enumerate(nodes):
        for i_b, b in enumerate(nodes[i_a+1:]):
            pairs.append((math.dist(a, b), a, b))
    pairs.sort()

    result_part_one = None
    result_part_two = None

    g = nx.Graph()
    g.add_nodes_from(nodes)
    for pair_i, pair in enumerate(pairs):
        g.add_edge(pair[1], pair[2])
        if pair_i + 1 == num_to_connect:
            # Get answer to part one
            cc = sorted(nx.connected_components(g), key=len, reverse=True)
            result_part_one = math.prod([len(c) for c in cc[:3]])
        if nx.is_connected(g):
            result_part_two = pair[1][0] * pair[2][0]
            # Assuming part one will finish before part two.
            break
    return (result_part_one, result_part_two)

if __name__ == '__main__':      
    for input_file, num_to_connect in (('test.txt', 10 ), ('input.txt', 1000)):
        print(f'{input_file}:')
        with open(input_file, 'r') as file:
            lines = [s for l in file.readlines() if (s := l.strip())]
        part_one_result, part_two_result = part_one_and_two(lines, num_to_connect)
        print(f'  Part one: {part_one_result}')
        print(f'  Part two: {part_two_result}')
        print()
        