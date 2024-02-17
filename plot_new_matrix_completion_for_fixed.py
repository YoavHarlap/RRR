import re

import matplotlib.pyplot as plt

filename = r"n_r_q_n_iter1.txt"
try:
    with open(filename, "r") as file:
        data_text = file.read()
except FileNotFoundError:
    print(f"filename{filename} not found")

lines = data_text.strip().split('\n')
n_r_q_n_iter = []

i = 0
while i < len(lines):
    offset = 0
    n_line = re.search(r'n = (\d+), r = (\d+), q = (\d+)', lines[i])
    ap_line = re.search(r'alternating_projections Converged in (\d+) iterations', lines[i + 1]) if i + 1 < len(
        lines) else 0
    if ap_line:
        offset = 1
    rrr_line = re.search(r'RRR_algorithm Converged in (\d+) iterations', lines[i + 1 + offset]) if i + 1 + offset < len(
        lines) else 0

    if not n_line:
        i += 1
        continue  # Skip lines without the 'n' line

    n = int(n_line.group(1))
    r = int(n_line.group(2))
    q = int(n_line.group(3))
    ap_n_iter = int(ap_line.group(1)) if ap_line else -1
    rrr_n_iter = int(rrr_line.group(1)) if rrr_line else -1

    n_r_q_n_iter.append([n, r, q, ap_n_iter, rrr_n_iter])

    # Move to the next set of lines
    i += 3 if ap_line and rrr_line else 1

print(n_r_q_n_iter)

# Extracting data for plotting
q_values = [item[2] for item in n_r_q_n_iter]
AP_iter_values = [item[3] for item in n_r_q_n_iter]
RRR_iter_values = [item[4] for item in n_r_q_n_iter]

# Filter out data points with iter values of -1
valid_indices_AP = [i for i, iter_value in enumerate(AP_iter_values) if iter_value != -1]
valid_indices_RRR = [i for i, iter_value in enumerate(RRR_iter_values) if iter_value != -1]

# valid_indices_AP = [i for i, iter_value in enumerate(AP_iter_values)]
# valid_indices_RRR = [i for i, iter_value in enumerate(RRR_iter_values)]

# Plotting AP_iter

plt.plot([q_values[i] for i in valid_indices_AP], [AP_iter_values[i] for i in valid_indices_AP], 'o', label='AP_iter',
         color='blue')

plt.plot([q_values[i] for i in valid_indices_RRR], [RRR_iter_values[i] for i in valid_indices_RRR], 'o',
         label='RRR_iter', color='green')


plt.title(f'n={n_r_q_n_iter[0][0]}, r={n_r_q_n_iter[0][1]}')
plt.xlabel('q')
plt.ylabel('AP_iter')
plt.legend()

plt.tight_layout()
plt.show()
