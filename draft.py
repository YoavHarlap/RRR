import numpy as np
from scipy.linalg import eig, norm

# Example of eigenvalues
matrix = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = eig(matrix)
print("Eigenvalues:", eigenvalues)

# Example of norm
vector = np.array([3, -4])
vector_norm = norm(vector)
print("Norm of the vector:", vector_norm)
