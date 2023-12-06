import numpy as np
from scipy.signal import convolve2d

lines = open('input_test.txt').readlines()
symbols = [*"*#+"]
schematic = np.array([[*i.strip()] for i in lines])
symbol_mask = np.isin(schematic, test_elements=symbols)
convolved = convolve2d(symbol_mask, 3 * [3 * [1]], mode="same") > 0
schematic_mask = schematic != '.'
masked = np.ma.masked_array(schematic, mask=np.invert(schematic_mask & convolved))
print(masked)
