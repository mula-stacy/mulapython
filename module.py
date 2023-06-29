import statistics
from cmath import pi
from math import sin

import mymodule

mymodule.eMobilis("eMobilis Mobile Technology")
mymodule.Ajira("Ajira")
dataset = [3, 6, 7, 1, 5, 8, 9]
x = statistics.mean(dataset)
y = sin(pi / 2)
print("mean is", x)
variables = [4, 7, 8, 6, 9, 0]
z = statistics.mean(variables)
x = statistics.mode(variables)
w = statistics.median(variables)
print(z)
print(x)
print(w)
