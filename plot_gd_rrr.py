import matplotlib.pyplot as plt

# Initialize lists to store data
betas = []
rrr_iterations = []
gd_iterations = []

import numpy as np

# Parse the text data
with open(r"C:\Users\ASUS\PycharmProjects\RRR\texts\RRR_and_GD.txt", "r") as file:
    for line in file:
        if "RRR_algorithm" in line:
            beta_index = line.find("beta = ") + len("beta = ")
            beta = float(line[beta_index:])
            iteration_index = line.find("Converged in ") + len("Converged in ")
            iterations = int(line[iteration_index:line.find("iterations")])
            rrr_iterations.append(iterations)
            betas.append(beta)
        elif "GD" in line:
            beta_index = line.find("beta = ") + len("beta = ")
            beta = float(line[beta_index:])
            iteration_index = line.find("Converged in ") + len("Converged in ")
            iterations = int(line[iteration_index:line.find("iterations")])
            gd_iterations.append(iterations)

# Plotting
plt.plot(betas, np.log(rrr_iterations), label='RRR_algorithm')
plt.plot(betas, np.log(gd_iterations), label='GD')


plt.xlabel('Beta')
plt.ylabel('Iterations')
plt.title('Convergence Iterations')
plt.legend()
plt.show()
