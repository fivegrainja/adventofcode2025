#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = [
# ]
# ///

from pathlib import Path
from functools import reduce
from queue import PriorityQueue
from typing import Optional
from collections import deque

def breadth_first_search(graph, start, goal):
    frontier = deque()
    frontier.append(start)
    came_from = dict()
    came_from[start] = None

    while frontier:
        current = frontier.popleft()

        if current == goal:
            break           

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.append(next)
                came_from[next] = current
    
    return came_from

def count_presses(came_from: dict[str], start: str, goal: str) -> int:
    # print(came_from)
    # print(start)
    # print(goal)
    current = goal
    presses = 0
    while current != start:
        current = came_from[current]
        presses += 1
    return presses

class LightGraph:

    def __init__(self, buttons: list[tuple]):
        self.buttons = buttons

    def neighbors(self, node: str) -> list[str]:
        neighbors = []
        for button in self.buttons:
            neighbor = list(node)
            for i in button:
                neighbor[i] = '.' if neighbor[i] == '#' else '#'
            neighbors.append(''.join(neighbor))
        return neighbors
    
    def cost(self, current: str, next: str) -> float:
        return 1


def part_one(lines: list[str]) -> int:
    total_presses = 0
    for line in lines:
        parts = line.split()
        lights = parts[0].strip('[]')
        buttons = [tuple(map(int, p.strip('()').split(','))) for p in parts[1:-1]]
        # joltages = parts[-1]
        graph = LightGraph(buttons)
        came_from = breadth_first_search(graph, '.' * len(lights), lights)
        button_presses = count_presses(came_from, '.' * len(lights), lights)
        total_presses += button_presses
    return total_presses

def part_two(lines: list[str]) -> int:
    return None

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
        