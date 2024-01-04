import re
import matplotlib.pyplot as plt

# Your data
data_text = """
m = 10 , n = 10
AP Converged in 1 iterations.
RRR Converged in 1 iterations.

"""
# Read the content of the file "saves.txt"
with open(r"C:\Users\ASUS\PycharmProjects\RRR\saves.txt", "r") as file:
    print("ooooooooo")
    data_text = file.read()



# Extract relevant information using regular expressions
pattern = re.compile(r"m = (\d+) , n = (\d+)\n(?:alternating_projections Converged in (\d+) iterations\.)?(?:\nRRR_algorithm Converged in (\d+) iterations\.)?")
matches = pattern.findall(data_text)

# Convert matches to dictionary
data = []
for match in matches:
    m, n, ap_iterations, rrr_iterations = map(lambda x: int(x) if x else None, match)
    data.append({'m': m, 'n': n, 'AP_iterations': ap_iterations, 'RRR_iterations': rrr_iterations})

# Plotting
colors = []
for entry in data:
    if entry['AP_iterations'] and entry['RRR_iterations']:
        colors.append('green')
    elif not entry['AP_iterations'] and not entry['RRR_iterations']:
        colors.append('red')
    elif entry['AP_iterations'] and not entry['RRR_iterations']:
        colors.append('blue')  # Choose your color for AP Converged only
    elif not entry['AP_iterations'] and entry['RRR_iterations']:
        colors.append('orange')  # Choose your color for RRR Converged only

for i, entry in enumerate(data):
    plt.scatter(entry['m'], entry['n'], color=colors[i])
    plt.text(entry['m'], entry['n'], f"AP: {entry['AP_iterations']}, RRR: {entry['RRR_iterations']}", fontsize=4)

plt.title('Convergence Plot')
plt.xlabel('m')
plt.ylabel('n')
plt.show()
