import re

import matplotlib.pyplot as plt
import numpy as np

# Your data
data_text = """
m = 10 , n = 10
AP Converged in 1 iterations.
RRR Converged in 1 iterations.

"""
import os

filename = "savesdftiter100000.txt"

folder_path = r"C:\Users\ASUS\PycharmProjects\RRR"
file_path = os.path.join(folder_path, filename)

try:
    with open(file_path, "r") as file:
        data_text = file.read()
except FileNotFoundError:
    # Handle file not found error by trying another location
    folder_path = r"//home//yoavharlap//PycharmProjects//RRR"

    new_file_path = os.path.join(folder_path, filename)

    try:
        with open(new_file_path, "r") as file:
            data_text = file.read()
    except FileNotFoundError:
        print("File not found in both locations.")

print(data_text)
# Ignore lines containing "The projections is not same" before processing
data_text = '\n'.join(line for line in data_text.split('\n') if "The projections is not same" not in line)


# Extract relevant information using regular expressions
pattern = re.compile(
    r"m = (\d+), n = (\d+)\n(?:alternating_projections Converged in (\d+) iterations\.)?(?:\n?RRR_algorithm Converged in (\d+) iterations\.)?")
matches = pattern.findall(data_text)


# Convert matches to dictionary
data = []
for match in matches:
    m, n, ap_iterations, rrr_iterations = map(lambda x: int(x) if x else None, match)
    data.append({'m': m, 'n': n, 'AP_iterations': ap_iterations, 'RRR_iterations': rrr_iterations})

# Plotting
colors = []
for entry in data:
    if entry['AP_iterations'] is not None and entry['RRR_iterations'] is not None:
        colors.append('green')
    elif entry['AP_iterations'] is None and entry['RRR_iterations'] is None:
        colors.append('red')
    elif entry['AP_iterations'] is not None and entry['RRR_iterations'] is None:
        colors.append('blue')  # Choose your color for AP Converged only
    elif entry['AP_iterations'] is None and entry['RRR_iterations'] is not None:
        colors.append('orange')  # Choose your color for RRR Converged only

flag = True


for i, entry in enumerate(data):
    p = np.floor((-1 + np.sqrt(1+8*i))/2)
    plt.scatter(entry['m'], entry['n'], color=colors[i])
    plt.text(entry['m'], entry['n'] + 1.6+1.6*(-1)**p, f"AP: {entry['AP_iterations']}"
                                               f", RRR: {entry['RRR_iterations']}", fontsize=6)


plt.title('Convergence Plot with DFT matrix')
plt.xlabel('m')
plt.ylabel('n')

plt.show()
