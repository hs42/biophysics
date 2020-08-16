import numpy as np
import matplotlib.pyplot as plt
from methods import *

height, width = 10,10

grid = HexGrid(NubotCell, height, width, {"state": 0})


#for i, j in np.ndindex((1,1)):
grid.get_cell(1,1).set_state(1)
grid.get_cell(0,1).set_state(1)


#grid.plot_states([0, 1,2,3])
#plt.title("initial position")
#plt.show()

steps = 7
for _ in range(steps):
    grid.perform_step()

#grid.plot_states([0,1,2,3])
#plt.title(f"after {steps} steps")
#plt.show()

grid.get_cell(4,1).set_state(2)
grid.get_cell(5,1).set_state(1)

grid.plot_states([0,1,2,3])
plt.show()

grid.simple_turn(np.array([-1, 1]), np.array([5, 1]), start=True)


#reset all states to 1
grid.reset_states()

grid.get_cell(4,2).set_state(2)
grid.get_cell(4,3).set_state(1)

grid.plot_states([0,1,2,3])
plt.show()

grid.simple_turn(np.array([-1, -1]), np.array([4, 3]), start=True)
grid.reset_states()

#grid.simple_turn(np.array([-1, 1]), np.array([2, 2]))

#grid.get_cell(2,2).set_state(2)
grid.plot_states([0,1,2,3])
plt.title(f"after turning")
plt.show()

