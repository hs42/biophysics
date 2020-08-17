import numpy as np
import matplotlib.pyplot as plt
from methods import *

height, width = 10,10

grid = HexGrid(NubotCell, height, width, {"state": 0})


#for i, j in np.ndindex((1,1)):
grid.get_cell(2,1).set_state(1)
grid.get_cell(1,1).set_state(1)


#grid.plot_states([0, 1,2,3])
#plt.title("initial position")
#plt.show()

steps = 6
for _ in range(steps):
    grid.perform_step()

grid.plot_states([0,1,2,3])
plt.title(f"after elongating monomers")
plt.show()





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
#grid.get_cell(2,1).set_state(1)
#grid.get_cell(0,1).set_state(0)

grid.plot_states([0,1,2,3])
plt.title(f"after turning")
plt.show()


steps = 2
for _ in range(steps):
    grid.perform_step()

grid.plot_states([0,1,2,3])
plt.title(f"after extending along x")
plt.show()
steps = 4
for _ in range(steps):
    grid.perform_step_upward()

#grid.simple_turn(np.array([-1, 1]), np.array([2, 2]))

#grid.get_cell(2,2).set_state(2)


grid.plot_states([0,1,2,3])
plt.title(f"after extending along y")
plt.show()

grid.draw(1, 1)

grid.plot_states([0,1,2,3])
plt.title(f"after deciding which lattice sites should remain occupied")
plt.show()

