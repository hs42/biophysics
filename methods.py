import os
import numpy as np

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
        up = (y+1)%self.heigth
        down = (y-1)%self.height

        return [self.cells[left][up], self.cells[x][up], 
                self.cells[left][y], self.cells[right][y], 
                self.cells[down][left], self.cells[down][y]]

    def get_cell(self, x, y, w=0):
        x = (x-w)%self.width
        y = (y+w)%self.height

        return self.cells[x][y]



class NubotCell:
    """
    Cells of the Nubot model. Is supposed to live on the HexGrid.
    """

    def __init__(self):
        raise NotImplementedError
