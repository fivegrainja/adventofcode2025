#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "networkx"
# ]
# ///

from pathlib import Path
import networkx as nx
from pprint import pprint
from functools import lru_cache

def create_graph(lines: list[str]) -> tuple[str, list[str], nx.DiGraph]:
    g = nx.DiGraph()
    ends = []
    for line in lines:
        parts = line.split(':')
        node = parts[0]
        for child in parts[1].split():
            if child == 'out':
                child = f'out{len(ends)}'
                ends.append(child)
            g.add_edge(node, child)
    return (ends, g)

def part_one(lines: list[str]) -> int:
    ends, g = create_graph(lines)
    total_paths = 0
    for end in ends:
        paths = nx.all_simple_paths(g, 'you', end)
        paths = list(paths)
        total_paths += len(paths)
    return total_paths

def part_two(lines: list[str]) -> int:

    # Build the graph
    nodes: dict[tuple[str]] = {}
    for line in lines:
        parts = line.split(':')
        node = parts[0]
        children = (parts[1].split())
        nodes[node] = children

    @lru_cache
    def bfs(node: str) -> tuple[int, int, int, int]:
        # num_out, num_dac, num_fft, num_both
        if node == 'out':
            return (1, 0, 0, 0)
        num_out, num_dac, num_fft, num_both = 0, 0, 0, 0
        for child in nodes[node]:
            child_out, child_dac, child_fft, child_both = bfs(child)
            num_out += child_out
            num_dac += child_dac
            num_fft += child_fft
            num_both += child_both
            if node == 'dac':
                assert(child_dac == 0)
                assert(child_both == 0)
                num_dac += child_out
                num_both += child_fft
            if node == 'fft':
                assert(child_fft == 0)
                assert(child_both == 0)
                num_fft += child_out
                num_both += child_dac
        return (num_out, num_dac, num_fft, num_both)

    num_out, num_dac, num_fft, num_both = bfs('svr')
    return num_both

if __name__ == '__main__':      
    for input_file in ('test.txt', 'input.txt'):
        print(f'{input_file}:')
        with open(Path(__file__).resolve().parent / input_file, 'r') as file:
            lines = [s for l in file.readlines() if (s := l.strip())]
        result = part_one(lines)
        print(f'  Part one: {result}')
        print()
    for input_file in ('p2test.txt', 'input.txt'):
        print(f'{input_file}:')
        with open(Path(__file__).resolve().parent / input_file, 'r') as file:
            lines = [s for l in file.readlines() if (s := l.strip())]
        result = part_two(lines)
        print(f'  Part two: {result}')
        print()