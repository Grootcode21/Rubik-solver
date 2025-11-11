"""
3x3 Rubik's Cube Solver with Static 3D Visualization
----------------------------------------------------
Solves a Rubik's Cube using the rubik-solver library and shows a 3D cube using matplotlib.

Install:
    pip install rubik-solver matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from typing import Dict, List

try:
    from rubik_solver import utils as rubik_utils
except Exception:
    rubik_utils = None


COLOR_MAP = {
    'U': 'white',
    'R': 'red',
    'F': 'green',
    'D': 'yellow',
    'L': 'orange',
    'B': 'blue'
}


def solve_with_rubik_solver(facelet_string: str) -> List[str]:
    if not rubik_utils:
        raise RuntimeError("rubik-solver not available. Install with: pip install rubik-solver")
    return [str(m) for m in rubik_utils.solve(facelet_string, 'Kociemba')]


def draw_static_cube():
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1, 1, 1])
    ax.view_init(30, 45)
    ax.axis('off')

    faces = {
        'U': (0, 1, 0),
        'D': (0, -1, 0),
        'F': (0, 0, 1),
        'B': (0, 0, -1),
        'L': (-1, 0, 0),
        'R': (1, 0, 0)
    }

    for face, normal in faces.items():
        color = COLOR_MAP[face]
        for i in range(3):
            for j in range(3):
                offset = np.array([i - 1, j - 1, 0]) * 0.32
                center = np.array(normal) + offset
                size = 0.15
                verts = [
                    [center + [size, size, 0]],
                    [center + [-size, size, 0]],
                    [center + [-size, -size, 0]],
                    [center + [size, -size, 0]]
                ]
                square = np.array([v[0] for v in verts])
                ax.add_collection3d(Poly3DCollection([square], facecolors=color, edgecolors='black'))

    plt.title("3x3 Rubik's Cube (Solved State)")
    plt.show()


def main():
    print("3x3 Rubik's Cube Solver (rubik-solver based)")
    if not rubik_utils:
        print("Install rubik-solver with: pip install rubik-solver")
        return

    solved = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
    print("\nPaste a 54-character facelet string (or press Enter for solved cube):")
    s = input().strip()
    if not s:
        s = solved

    if len(s) != 54:
        print("Input must be exactly 54 characters long.")
        return

    try:
        solution = solve_with_rubik_solver(s)
        print("\nSolution moves:")
        print(' '.join(solution))
    except Exception as e:
        print("Error:", e)
        print("Make sure your cube string is valid (54 characters, each representing a color).")

    print("\nDisplaying 3D cube...")
    draw_static_cube()


if __name__ == "__main__":
    main()
