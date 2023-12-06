import numpy as np


def doit(file: str):
    lines = open(file).readlines()
    symbols = [*"*#+"]
    print(symbols)
    x = np.array([[*i.strip()] for i in lines])
    print(x)


doit('input_test.txt')
