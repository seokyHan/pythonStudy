import numpy as np


arr_n = np.ones((5,4),dtype=np.int8)

print(arr_n.shape)
arr_n2 = np.reshape(arr_n,(2,10))
print(arr_n2)