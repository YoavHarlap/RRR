import re
import matplotlib.pyplot as plt

# Your data
data_text = """
m = 10 , n = 10
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 20
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 30
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 40
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 50
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 60
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 70
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 80
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 90
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 100
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 10 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 10


m = 20 , n = 20
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 30
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 40
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 50
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 60
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 70
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 80
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 90
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 100
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 20 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 10
AP Converged in 867 iterations.


m = 30 , n = 20
AP Converged in 325 iterations.
RRR Converged in 580 iterations.


m = 30 , n = 30
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 40
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 50
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 60
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 70
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 80
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 90
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 100
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 30 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 10
AP Converged in 195 iterations.


m = 40 , n = 20


m = 40 , n = 30
AP Converged in 320 iterations.
RRR Converged in 292 iterations.


m = 40 , n = 40
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 50
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 60
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 70
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 80
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 90
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 100
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 40 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 10
AP Converged in 225 iterations.


m = 50 , n = 20


m = 50 , n = 30
AP Converged in 3693 iterations.
RRR Converged in 984 iterations.


m = 50 , n = 40
AP Converged in 160 iterations.
RRR Converged in 462 iterations.


m = 50 , n = 50
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 60
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 70
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 80
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 90
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 100
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 50 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 10
AP Converged in 126 iterations.


m = 60 , n = 20


m = 60 , n = 30


m = 60 , n = 40
AP Converged in 319 iterations.
RRR Converged in 539 iterations.


m = 60 , n = 50
AP Converged in 95 iterations.
RRR Converged in 124 iterations.


m = 60 , n = 60
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 70
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 80
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 90
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 100
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 60 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 10
AP Converged in 81 iterations.


m = 70 , n = 20


m = 70 , n = 30


m = 70 , n = 40
AP Converged in 5010 iterations.
RRR Converged in 1960 iterations.


m = 70 , n = 50
AP Converged in 416 iterations.
RRR Converged in 368 iterations.


m = 70 , n = 60
AP Converged in 82 iterations.
RRR Converged in 135 iterations.


m = 70 , n = 70
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 80
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 90
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 100
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 70 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 10
AP Converged in 63 iterations.


m = 80 , n = 20


m = 80 , n = 30


m = 80 , n = 40


m = 80 , n = 50
AP Converged in 1416 iterations.
RRR Converged in 906 iterations.


m = 80 , n = 60
AP Converged in 205 iterations.
RRR Converged in 370 iterations.


m = 80 , n = 70
AP Converged in 82 iterations.
RRR Converged in 144 iterations.


m = 80 , n = 80
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 90
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 100
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 80 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 10
AP Converged in 66 iterations.


m = 90 , n = 20


m = 90 , n = 30
AP Converged in 525 iterations.


m = 90 , n = 40


m = 90 , n = 50
RRR Converged in 2934 iterations.


m = 90 , n = 60
AP Converged in 460 iterations.
RRR Converged in 630 iterations.


m = 90 , n = 70
AP Converged in 160 iterations.
RRR Converged in 240 iterations.


m = 90 , n = 80
AP Converged in 87 iterations.
RRR Converged in 120 iterations.


m = 90 , n = 90
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 100
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 90 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 10
AP Converged in 76 iterations.


m = 100 , n = 20
AP Converged in 142 iterations.


m = 100 , n = 30
AP Converged in 492 iterations.


m = 100 , n = 40


m = 100 , n = 50


m = 100 , n = 60
AP Converged in 1747 iterations.
RRR Converged in 1757 iterations.


m = 100 , n = 70
AP Converged in 277 iterations.
RRR Converged in 491 iterations.


m = 100 , n = 80
AP Converged in 165 iterations.
RRR Converged in 229 iterations.


m = 100 , n = 90
AP Converged in 62 iterations.
RRR Converged in 131 iterations.


m = 100 , n = 100
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 100 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 110 , n = 10
AP Converged in 67 iterations.


m = 110 , n = 20
AP Converged in 176 iterations.


m = 110 , n = 30


m = 110 , n = 40


m = 110 , n = 50


m = 110 , n = 60
RRR Converged in 4693 iterations.


m = 110 , n = 70
AP Converged in 1498 iterations.
RRR Converged in 893 iterations.


m = 110 , n = 80
AP Converged in 240 iterations.
RRR Converged in 361 iterations.


m = 110 , n = 90
AP Converged in 153 iterations.
RRR Converged in 206 iterations.


m = 110 , n = 100
AP Converged in 59 iterations.
RRR Converged in 113 iterations.


m = 110 , n = 110
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 110 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 110 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 110 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 110 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 110 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 110 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 110 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 110 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 110 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 120 , n = 10
AP Converged in 58 iterations.


m = 120 , n = 20


m = 120 , n = 30
AP Converged in 377 iterations.


m = 120 , n = 40


m = 120 , n = 50


m = 120 , n = 60


m = 120 , n = 70
AP Converged in 9361 iterations.


"""

# Extract relevant information using regular expressions
pattern = re.compile(r"m = (\d+) , n = (\d+)\n(?:AP Converged in (\d+) iterations\.)?(?:\nRRR Converged in (\d+) iterations\.)?")
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
    plt.text(entry['m'], entry['n'], f"AP: {entry['AP_iterations']}, RRR: {entry['RRR_iterations']}", fontsize=8)

plt.title('Convergence Plot')
plt.xlabel('m')
plt.ylabel('n')
plt.show()
