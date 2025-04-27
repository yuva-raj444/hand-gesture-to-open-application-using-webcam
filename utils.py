import numpy as np

# Calculate the Euclidean distance between two landmarks
def distance(lm1, lm2):
    return np.sqrt((lm1.x - lm2.x) ** 2 + (lm1.y - lm2.y) ** 2)
