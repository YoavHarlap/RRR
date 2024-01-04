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
RRR Converged in 2220 iterations.


m = 120 , n = 80
AP Converged in 761 iterations.
RRR Converged in 606 iterations.


m = 120 , n = 90
AP Converged in 269 iterations.
RRR Converged in 313 iterations.


m = 120 , n = 100
AP Converged in 110 iterations.
RRR Converged in 229 iterations.


m = 120 , n = 110
AP Converged in 62 iterations.
RRR Converged in 103 iterations.


m = 120 , n = 120
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 120 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 120 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 120 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 120 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 120 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 120 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 120 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 120 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 130 , n = 10
AP Converged in 53 iterations.


m = 130 , n = 20
AP Converged in 105 iterations.


m = 130 , n = 30
AP Converged in 218 iterations.


m = 130 , n = 40


m = 130 , n = 50


m = 130 , n = 60


m = 130 , n = 70
RRR Converged in 8701 iterations.


m = 130 , n = 80
AP Converged in 1681 iterations.
RRR Converged in 2169 iterations.


m = 130 , n = 90
AP Converged in 459 iterations.
RRR Converged in 611 iterations.


m = 130 , n = 100
AP Converged in 168 iterations.
RRR Converged in 265 iterations.


m = 130 , n = 110
AP Converged in 107 iterations.
RRR Converged in 171 iterations.


m = 130 , n = 120
AP Converged in 64 iterations.
RRR Converged in 105 iterations.


m = 130 , n = 130
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 130 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 130 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 130 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 130 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 130 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 130 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 130 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 140 , n = 10
AP Converged in 68 iterations.


m = 140 , n = 20
AP Converged in 111 iterations.


m = 140 , n = 30
AP Converged in 150 iterations.


m = 140 , n = 40
AP Converged in 487 iterations.


m = 140 , n = 50


m = 140 , n = 60


m = 140 , n = 70


m = 140 , n = 80
AP Converged in 4477 iterations.
RRR Converged in 4041 iterations.


m = 140 , n = 90
AP Converged in 1036 iterations.
RRR Converged in 1043 iterations.


m = 140 , n = 100
AP Converged in 280 iterations.
RRR Converged in 433 iterations.


m = 140 , n = 110
AP Converged in 186 iterations.
RRR Converged in 344 iterations.


m = 140 , n = 120
AP Converged in 92 iterations.
RRR Converged in 153 iterations.


m = 140 , n = 130
AP Converged in 61 iterations.
RRR Converged in 99 iterations.


m = 140 , n = 140
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 140 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 140 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 140 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 140 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 140 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 140 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 150 , n = 10
AP Converged in 57 iterations.


m = 150 , n = 20
AP Converged in 94 iterations.


m = 150 , n = 30
AP Converged in 227 iterations.


m = 150 , n = 40


m = 150 , n = 50
AP Converged in 1720 iterations.


m = 150 , n = 60


m = 150 , n = 70


m = 150 , n = 80
RRR Converged in 8026 iterations.


m = 150 , n = 90
AP Converged in 4989 iterations.
RRR Converged in 2314 iterations.


m = 150 , n = 100
AP Converged in 581 iterations.
RRR Converged in 640 iterations.


m = 150 , n = 110
AP Converged in 235 iterations.
RRR Converged in 386 iterations.


m = 150 , n = 120
AP Converged in 174 iterations.
RRR Converged in 266 iterations.


m = 150 , n = 130
AP Converged in 92 iterations.
RRR Converged in 164 iterations.


m = 150 , n = 140
AP Converged in 60 iterations.
RRR Converged in 103 iterations.


m = 150 , n = 150
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 150 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 150 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 150 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 150 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 150 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 160 , n = 10
AP Converged in 54 iterations.


m = 160 , n = 20
AP Converged in 80 iterations.


m = 160 , n = 30
AP Converged in 152 iterations.


m = 160 , n = 40
AP Converged in 460 iterations.


m = 160 , n = 50


m = 160 , n = 60


m = 160 , n = 70


m = 160 , n = 80


m = 160 , n = 90
RRR Converged in 2951 iterations.


m = 160 , n = 100
AP Converged in 2057 iterations.
RRR Converged in 1271 iterations.


m = 160 , n = 110
AP Converged in 760 iterations.
RRR Converged in 610 iterations.


m = 160 , n = 120
AP Converged in 298 iterations.
RRR Converged in 395 iterations.


m = 160 , n = 130
AP Converged in 149 iterations.
RRR Converged in 266 iterations.


m = 160 , n = 140
AP Converged in 79 iterations.
RRR Converged in 154 iterations.


m = 160 , n = 150
AP Converged in 58 iterations.
RRR Converged in 105 iterations.


m = 160 , n = 160
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 160 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 160 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 160 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 160 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 170 , n = 10
AP Converged in 55 iterations.


m = 170 , n = 20
AP Converged in 86 iterations.


m = 170 , n = 30
AP Converged in 120 iterations.


m = 170 , n = 40
AP Converged in 260 iterations.


m = 170 , n = 50


m = 170 , n = 60


m = 170 , n = 70


m = 170 , n = 80


m = 170 , n = 90


m = 170 , n = 100
AP Converged in 6848 iterations.
RRR Converged in 1931 iterations.


m = 170 , n = 110
AP Converged in 1197 iterations.
RRR Converged in 1149 iterations.


m = 170 , n = 120
AP Converged in 345 iterations.
RRR Converged in 566 iterations.


m = 170 , n = 130
AP Converged in 222 iterations.
RRR Converged in 294 iterations.


m = 170 , n = 140
AP Converged in 172 iterations.
RRR Converged in 207 iterations.


m = 170 , n = 150
AP Converged in 86 iterations.
RRR Converged in 141 iterations.


m = 170 , n = 160
AP Converged in 53 iterations.
RRR Converged in 94 iterations.


m = 170 , n = 170
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 170 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 170 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 170 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 180 , n = 10
AP Converged in 63 iterations.


m = 180 , n = 20
AP Converged in 87 iterations.


m = 180 , n = 30
AP Converged in 123 iterations.


m = 180 , n = 40


m = 180 , n = 50
AP Converged in 385 iterations.


m = 180 , n = 60


m = 180 , n = 70


m = 180 , n = 80


m = 180 , n = 90


m = 180 , n = 100
RRR Converged in 4438 iterations.


m = 180 , n = 110
AP Converged in 2588 iterations.
RRR Converged in 1746 iterations.


m = 180 , n = 120
AP Converged in 447 iterations.
RRR Converged in 988 iterations.


m = 180 , n = 130
AP Converged in 340 iterations.
RRR Converged in 484 iterations.


m = 180 , n = 140
AP Converged in 195 iterations.
RRR Converged in 289 iterations.


m = 180 , n = 150
AP Converged in 140 iterations.
RRR Converged in 208 iterations.


m = 180 , n = 160
AP Converged in 83 iterations.
RRR Converged in 147 iterations.


m = 180 , n = 170
AP Converged in 53 iterations.
RRR Converged in 104 iterations.


m = 180 , n = 180
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 180 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 180 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 190 , n = 10
AP Converged in 52 iterations.


m = 190 , n = 20
AP Converged in 63 iterations.


m = 190 , n = 30
AP Converged in 126 iterations.


m = 190 , n = 40
AP Converged in 518 iterations.


m = 190 , n = 50
AP Converged in 507 iterations.


m = 190 , n = 60
AP Converged in 1854 iterations.


m = 190 , n = 70


m = 190 , n = 80


m = 190 , n = 90


m = 190 , n = 100


m = 190 , n = 110
RRR Converged in 2530 iterations.


m = 190 , n = 120
AP Converged in 2507 iterations.
RRR Converged in 998 iterations.


m = 190 , n = 130
AP Converged in 448 iterations.
RRR Converged in 735 iterations.


m = 190 , n = 140
AP Converged in 349 iterations.
RRR Converged in 359 iterations.


m = 190 , n = 150
AP Converged in 159 iterations.
RRR Converged in 273 iterations.


m = 190 , n = 160
AP Converged in 112 iterations.
RRR Converged in 182 iterations.


m = 190 , n = 170
AP Converged in 68 iterations.
RRR Converged in 132 iterations.


m = 190 , n = 180
AP Converged in 55 iterations.
RRR Converged in 92 iterations.


m = 190 , n = 190
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 190 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.


m = 200 , n = 10
AP Converged in 48 iterations.


m = 200 , n = 20
AP Converged in 76 iterations.


m = 200 , n = 30
AP Converged in 118 iterations.


m = 200 , n = 40
AP Converged in 279 iterations.


m = 200 , n = 50
AP Converged in 864 iterations.


m = 200 , n = 60


m = 200 , n = 70
 

m = 200 , n = 80


m = 200 , n = 90


m = 200 , n = 100


m = 200 , n = 110
AP Converged in 8930 iterations.
RRR Converged in 5819 iterations.


m = 200 , n = 120
AP Converged in 2558 iterations.
RRR Converged in 1888 iterations.


m = 200 , n = 130
AP Converged in 1152 iterations.
RRR Converged in 1000 iterations.


m = 200 , n = 140
AP Converged in 396 iterations.
RRR Converged in 631 iterations.


m = 200 , n = 150
AP Converged in 288 iterations.
RRR Converged in 339 iterations.


m = 200 , n = 160
AP Converged in 135 iterations.
RRR Converged in 274 iterations.


m = 200 , n = 170
AP Converged in 107 iterations.
RRR Converged in 187 iterations.


m = 200 , n = 180
AP Converged in 79 iterations.
RRR Converged in 124 iterations.


m = 200 , n = 190
AP Converged in 58 iterations.
RRR Converged in 88 iterations.


m = 200 , n = 200
AP Converged in 1 iterations.
RRR Converged in 1 iterations.



Process finished with exit code 0


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
    plt.text(entry['m'], entry['n'], f"AP: {entry['AP_iterations']}, RRR: {entry['RRR_iterations']}", fontsize=4)

plt.title('Convergence Plot')
plt.xlabel('m')
plt.ylabel('n')
plt.show()
