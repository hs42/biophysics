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
        if (self.cells[left].get_prev_state() <> self.cells[right].get_prev_state()):
            self.cells[i].set_state(1)
        else:
            self.cells[i].set_state(0)
    def init_automata(self):
        center = int(self.cols / 2)
        
# Game of Life