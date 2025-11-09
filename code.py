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