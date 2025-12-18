#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = [
#    "z3-solver"
# ]
# ///

from pathlib import Path
# from functools import reduce, lru_cache, cmp_to_key
# from queue import PriorityQueue
# from typing import Optional
from collections import deque #, Counter
# from itertools import chain

from z3 import Int, Optimize, sat

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

# def heuristic(a: tuple, b: tuple) -> int:
#     return sum(abs(x - y) for x, y in zip(a, b))

# def a_star_search(graph, start, goal):
#     frontier = PriorityQueue()
#     frontier.put((0, start))
#     came_from = {}
#     cost_so_far = {}
#     came_from[start] = None
#     cost_so_far[start] = 0

#     while not frontier.empty():
#         current_priority, current = frontier.get()
#         if current == goal:
#             break           
#         for next in graph.neighbors(current):
#             new_cost = cost_so_far[current] + 1
#             if next not in cost_so_far or new_cost < cost_so_far[next]:
#                 cost_so_far[next] = new_cost
#                 priority = new_cost + heuristic(next, goal)
#                 frontier.put((priority, next))
#                 came_from[next] = current
    
#     return came_from

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


# def fancy_sort(buttons: tuple, joltages: tuple) -> list[tuple]:
#     joltage_counts = reversed(Counter(chain(buttons)).most_common())

#     def compare(b1: tuple, b2: tuple) -> int:
#         for j, c in joltage_counts:
#             if j in b1 and j not in b2:
#                 return -1
#             if j in b2 and j not in b1:
#                 return 1
#             if j in b1 and j in b2:
#                 return len(b1) - len(b2)
#         return 0
    
#     new_buttons = sorted(buttons, key=cmp_to_key(compare))
#     return new_buttons


# @lru_cache
# def depth_first_search(buttons: tuple[tuple], joltages: tuple) -> int:
#     # Order the buttons by desirableness
#     # Apply that button
#     # Call this recursively on each.

#     # This is the ending condition of the recursion
#     if not any(joltages):
#         return 0

#     # Remember to sort buttons later
#     min_presses = None
#     local_buttons = fancy_sort(buttons, joltages)
#     for button in local_buttons:
#         new_joltage = list(joltages)
#         for v in button:
#             new_joltage[v] -= 1
#             if new_joltage[v] < 0:
#                 break
#         else:
#             new_joltage = tuple(new_joltage)
#             new_presses = depth_first_search(buttons, new_joltage)
#             if new_presses is not None:
#                 if min_presses is None or new_presses + 1 < min_presses:
#                     min_presses = new_presses + 1

#     return min_presses
    

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

# class JoltageGraph:

#     def __init__(self, buttons: list[tuple], goal: tuple):
#         self.buttons = buttons
#         self.goal = goal

#     def neighbors(self, node: tuple) -> list[tuple]:
#         neighbors = []
#         for button in self.buttons:
#             neighbor = list(node)
#             for i in button:
#                 neighbor[i] += 1
#             neighbor = tuple(neighbor)
#             for i in range(len(neighbor)):
#                 if neighbor[i] > self.goal[i]:
#                     break
#             else:
#                 neighbors.append(tuple(neighbor))
#         return neighbors


def solve_joltages(joltages: tuple, buttons: list[tuple]) -> list[int] | None:
    len_joltages = len(joltages)
    len_buttons = len(buttons)
    # Create coefficient matrix B
    B = [[0]*len_buttons for _ in range(len_joltages)]
    for j, btn in enumerate(buttons):
        for i in btn:
            B[i][j] += 1
    # Z3 integer variables: x_j = number of presses of button j
    x = [Int(f"x_{j}") for j in range(len_buttons)]
    opt = Optimize()
    # Variables must be nonnegative integers
    for j in range(len_buttons):
        opt.add(x[j] >= 0)
    # Constraints: B * x = target
    for i in range(len_joltages):
        opt.add(sum(B[i][j] * x[j] for j in range(len_buttons)) == joltages[i])
    # Objective: minimize total presses
    opt.minimize(sum(x))
    if opt.check() != sat:
        print("No solution")
        return None
    mod = opt.model()
    solution = [mod[x[j]].as_long() for j in range(len_buttons)]
    return sum(solution)

def part_two(lines: list[str]) -> int:
    total_presses = 0
    for line in lines:
        parts = line.split()
        buttons = [tuple(map(int, p.strip('()').split(','))) for p in parts[1:-1]]
        joltages = tuple(map(int, parts[-1].strip('{}').split(',')))
        button_presses = solve_joltages(joltages, buttons)
        total_presses += button_presses
    return total_presses

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
        