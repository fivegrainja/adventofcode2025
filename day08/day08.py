#! /usr/bin/env python3

from dataclasses import dataclass
import math
import networkx as nx


# @dataclass
# class Pair:
#     a: tuple[int, int, int]
#     b: tuple[int, int, int]
#     distance: float

def part_one(lines: list[str], num_to_connect: int) -> int:
    # nodes: list[tuple[int, int, int]] = [l.split(',') for l in lines]
    nodes: list[tuple[int, int, int]] = [tuple(map(int, l.split(','))) for l in lines]
    # print('nodes')
    # print(nodes)
    pairs: tuple[float, tuple[int, int, int], tuple[int, int, int]] = []
    for i_a, a in enumerate(nodes):
        for i_b, b in enumerate(nodes[i_a+1:]):
            # print(f'a: {a}  b: {b}')
            pairs.append((math.dist(a, b), a, b))
    pairs.sort()

    g = nx.Graph()
    for pair in pairs[:num_to_connect]:
        # print(f'Adding {pair[1]} and {pair[2]} with distance {pair[0]}')
        g.add_edge(pair[1], pair[2], distance=pair[0])

    cc = sorted(nx.connected_components(g), key=len, reverse=True)
    # print(f'Number of connected components is {len(cc)}')
    # for c in cc:
    #     print(c)
    # cc_lens = [len(c) for c in sorted(nx.connected_components(g), key=len, reverse=True)][:3]
    result = math.prod([len(c) for c in cc[:3]])
    return result

    # networks: list[set] = []
    # for pair in pairs[:num_to_connect]:
    #     # Find network with a, if any
    #     network_a = network_b = None

    #     for i, n in enumerate(networks):
    #         if pair.a in n:
    #             network_a = n
    #             network_a_i = i
    #             break
    #     for i, n in enumerate(networks):
    #         if pair.b in n:
    #             network_b = n
    #             break
    #     if network_a and network_b:
    #         # Join the networks



def part_two(lines: list[str]) -> int:
    pass

if __name__ == '__main__':      
    for input_file, num_to_connect in (('test.txt', 10 ), ('input.txt', 1000)):
        print(f'{input_file}:')
        with open(input_file, 'r') as file:
            lines = [s for l in file.readlines() if (s := l.strip())]
        part_one_result = part_one(lines, num_to_connect)
        print(f'  Part one: {part_one_result}')
        # part_two_result = part_two(lines)
        # print(f'  Part two: {part_two_result}')
        # print()
        