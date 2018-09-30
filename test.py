import numpy as np
epsilon = 0.5
print (np.random.choice([True, False], p=[epsilon, 1.0-epsilon]))
