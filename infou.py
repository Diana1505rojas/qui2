
import numpy as np


dim = (10, 20, 30, 200)
matriz1 = np.random.rand(*dim)

print(matriz1.shape) 
print(matriz1)

matriz3d = matriz1[0].copy()
print("matriz copia")
print(matriz3d.shape)
print(matriz3d)


print("Shape:", matriz3d.shape)
print("Dimension:", matriz3d.ndim)
print("Size:", matriz3d.size)
print("Data type:", matriz3d.dtype)
print("Item size:", matriz3d.itemsize, "bytes")
print("Number of bytes:", matriz3d.nbytes, "bytes")
print("Strides:", matriz3d.strides)