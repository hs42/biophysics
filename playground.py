import numpy as np
import matplotlib.pyplot as plt
from methods import *

height, width = 10,10

grid = HexGrid(NubotCell, height, width, {"state": 0})


#for i, j in np.ndindex((1,1)):
grid.get_cell(1,1).set_state(1) grid.get_cell(2,1).set_state(1)


grid.plot_states([0, 1,2,3])
plt.title("initial position")
plt.show()

steps = 5
for _ in range(steps):
    grid.perform_step()

grid.plot_states([0,1,2,3])
plt.title(f"after {steps} steps")
plt.show()
