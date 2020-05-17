import numpy as np
from matplotlib import pyplot as plt

N = 100
t = 100

field = np.zeros((N, N))
field[0, int(N/2)] = 1

for i in range(0, t - 1):
	for x in range(1, N - 1):
		field[i+1, x] = bool(field[i, x-1]) ^ bool(field[i, x+1]) #logical XOR


plt.imshow(field)
plt.savefig('sierpinski_automaton.png', dpi=300, format='png')