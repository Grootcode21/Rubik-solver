#pip install rubik-solver
#pip install pandas
#pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from typing import Dict, List
import time

try:
    from rubik_solver import utils as rubik_utils
except Exception:
    rubik_utils = None

# Define color map for faces
COLOR_MAP = {
    'U': 'white',
    'R': 'red',
    'F': 'green',
    'D': 'yellow',
    'L': 'orange',
    'B': 'blue'
}

def face_dict_to_facelet_string(face_dict: Dict[str, List[str]]) -> str:
    order = ['U', 'R', 'F', 'D', 'L', 'B']
    out = []
    for f in order:
        if f not in face_dict:
            raise ValueError(f"Missing face {f} in face_dict")
        vals = list(face_dict[f])
        if len(vals) != 9:
            raise ValueError(f"Face {f} must have exactly 9 stickers")
        out.extend(vals)
    return ''.join(out)

def solve_with_rubik_solver(facelet_string: str) -> List[str]:
    if not rubik_utils:
        raise RuntimeError('rubik-solver not available. Install it with: pip install rubik-solver')
    return [str(m) for m in rubik_utils.solve(facelet_string, 'Kociemba')] 

def draw_cube(ax, face_colors):
    # Simple representation: 6 faces, each a 3x3 grid.
    face_positions = {
        'U': np.array([0, 1, 0]),
        'D': np.array([0, -1, 0]),
        'F': np.array([0, 0, 1]),
        'B': np.array([0, 0, -1]),
        'L': np.array([-1, 0, 0]),
        'R': np.array([1, 0, 0])
     }

    for face, normal in face_positions.items():
        color = COLOR_MAP.get(face, 'gray')
        for i in range(3):
            for j in range(3):
                offset = np.array([i - 1, j - 1, 0]) * 0.32
                center = normal + offset
                verts = [
                    [center + [0.15, 0.15, 0]],
                    [center + [-0.15, 0.15, 0]],
                    [center + [-0.15, -0.15, 0]],
                    [center + [0.15, -0.15, 0]]
                ]
                square = np.array([v[0] for v in verts])
                collection = Poly3DCollection([square], facecolors=color, edgecolors='black')
                ax.add_collection3d(collection)

def visualize_solution(solution_moves: List[str]):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(30, 45)
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.axis('off')