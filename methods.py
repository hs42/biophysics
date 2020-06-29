import os
import numpy as np
import matplotlib.pyplot as plt

translate_neighbours = [np.array([-1, 1]), np.array([0, 1]), np.array([-1, 0]), np.array([1, 0]), np.array([-1, -1]), np.array([-1, 0])]

class Cell:
    """ The automaton class implements the topology (here a simple 1-D lattice), the
        initialization and the generation of the next step with the implementation of
        the rule that govern the update of the cell.
        
    Args:
        
    """
    def __init__(self):
        self.prev_state = 0
        self.state = 0
        
    def get_state(self):
        return self.state
    
    def set_state(self , state):
        self.state = state

    def get_prev_state(self):
        return self.prev_state

    def set_prev_state(self, state):
        self.prev_state = state

    def copy_state(self):
        self.prev_state = self.state


        
class Automata:
    def __init__(self, numcols):
        self.cols = numcols
        self.cells = []
        for i in range (numcols):
            cell = Cell()
            self.cells.append(cell)

    def get_all_cells(self):
        return self.cells

    def next_generation(self):
        for i in range(self.cols):
            self.cells[i].copy_state()
            for i in range(self.cols):
                curr_cell = self.cells[i]
                Automata.apply_rule(self,i)

    def apply_rule(self,i):
        state = self.cells[i].get_prev_state()
        left = i-1
        if(left < 0):
            left = self.cols-1
            right = i+1
        if (right == self.cols):
            right = 0
        if (self.cells[left].get_prev_state() != self.cells[right].get_prev_state()):
            self.cells[i].set_state(1)
        else:
            self.cells[i].set_state(0)
    def init_automata(self):
        center = int(self.cols / 2)
        
# Game of Life

class HexGrid:
    """
    Hexagonal grid that houses cells
    """
    def __init__(self, Celltype, height, width, cellkwds={}):
        """
        Celltype: The constructor function of the cells
        cellkwds: dict that contains config for cell constructor
        """

        self.Celltype = Celltype
        self.cells = []
        self.height = height
        self.width = width

        for w in range(width):
            self.cells += [[]]
            for h in range(height):
                self.cells[w] += [self.Celltype(**cellkwds)]

    
    def get_six_neighbours(self, x, y):
        """
        return the six adjacent cells to the cell at pos. x, y.
        Assumes periodic boundary conditions.
        """
        left = (x-1)%self.width
        right = (x+1)%self.width
        up = (y+1)%self.height
        down = (y-1)%self.height

        return [self.cells[left][up], self.cells[x][up], 
                self.cells[left][y], self.cells[right][y], 
                self.cells[down][left], self.cells[down][y]]

    def get_cell(self, x, y, w=0):
        x = (x-w)%self.width
        y = (y+w)%self.height

        return self.cells[x][y]

    def plot_states(self, states=[]):

        """
        states: which states are supposed to be plotted
        returns figure and axis with scatterplot

        use like:

        grid.plot_states(states=[1,2,3])
        plt.show()
        """

        xvals = []
        yvals = []
        cellstates = []

        for w in range(self.width):
            for h in range(self.height):
                state = self.cells[w][h].get_state()
                if state in states:
                    xvals += [(w+h/2)%self.width]
                    yvals += [h]
                    cellstates += [state]


        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        scatter = plt.scatter(xvals, yvals, c=cellstates, cmap="tab20")
        labels = list(set(cellstates))
        plt.legend(handles=scatter.legend_elements()[0], labels=labels)

        return fig, ax

    def perform_step(self):
        for i,j in np.ndindex(self.height, self.width):
            self.get_cell(i,j).simple_forward(self.get_six_neighbours(i,j))
        
        for i,j in np.ndindex(self.height, self.width):
            self.get_cell(i,j).update()

    def simple_turn(self, direction, pivot, start=False):
        """
        now moved to grid to get access to neighbours

        a first trial to implement a rotating arm

        Note that this function is rather a quick hack. 
        You'd rather want to implement it by using bonds and checking if a movement is possible in the first place
        in: expects a line of monomers to start with; initial kink at pivoting monomer must have been initialized by user. direction in {1,...,6 } correspoding to sites of neighbours
            pivot = np.array([x,y]), direction also np-array -> allows for addition of direction
        out: produces line with a a kink
        state 0: lattice site free
        state 1: monomer exists
        state 2: just moved. it remains static
        state 3: just moved. shall not be moved by neighbours but rather by next iteration
        state 4: pivoting monomer
        fct = translate cell by direction
        recursive -> apply functions for all neighbours. some are bound to not change
        """

        if start:
            newstarts = []
        # firstly translate first cell
        if pivot[0] <= 0 or pivot[1] <= 0: #if coordinates out of range
            return 

        if self.get_cell(*pivot).get_state() not in [0, 2]:
                self.get_cell(*(pivot + direction)).set_state(2)
                self.get_cell(*pivot).set_state(0)
            
        for i, n in enumerate(self.get_six_neighbours(*pivot)):
            if n.get_state() not in [0, 2, 3]:
                self.get_cell(*(pivot + translate_neighbours[i] + direction)).set_state(3)
                n.set_state(0)

                self.simple_turn(direction, pivot + translate_neighbours[i]) # also make neighbours drag their neighbours along direction
                if start:
                    newstarts += [pivot + translate_neighbours[i] + direction]
        
        #for i, n in enumerate(self.get_six_neighbours(*pivot)):
            #self.simple_turn(direction, pivot + translate_neighbours[i] + direction)
            #print(pivot + translate_neighbours[i] + direction)

        #wende jetzt simple turn auf pivot + direction site an


        if start:
            for i,j in np.ndindex(self.height, self.width):
                if self.get_cell(i,j).get_state() == 3:
                    self.get_cell(i,j).set_state(1)
            for newstart in newstarts:
                self.simple_turn(direction, newstart, start=True)


        return 

class NubotCell:
    """
    Cells of the Nubot model. Is supposed to live on the HexGrid.
    """

    def __init__(self, state):
        self.state = state
        self.new_state = state

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.new_state = state
    
    def queue_state(self, state):
        """
        queues new state, needs to update() after
        """ 
        self.new_state = state

    def update(self):
        self.state = self.new_state

    def simple_forward(self, neighbours=[]):
        #neighbours is list of six adjacent neighbour cells in order as defined in HexGrid.get_six_neighbours()
        if not neighbours:# if list is empty
            return 1
        if self.state == 1 and neighbours[2].get_state() == 1 and neighbours[3].get_state() == 0:#1=occupied, 0=unoccupied
            neighbours[3].queue_state(1) #update next neighbour

        return 0

    
