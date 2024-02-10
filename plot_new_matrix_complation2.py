import re


text = """
n = 40, r = 10, q = 10
RRR_algorithm Converged in 139 iterations.
n = 40, r = 10, q = 110
alternating_projections Converged in 860 iterations.
RRR_algorithm Converged in 1056 iterations.
n = 40, r = 10, q = 210
alternating_projections Converged in 8241 iterations.
RRR_algorithm Converged in 1708 iterations.
n = 40, r = 10, q = 310
RRR_algorithm Converged in 1671 iterations.
n = 40, r = 10, q = 410
n = 40, r = 10, q = 510
n = 40, r = 10, q = 610
n = 40, r = 10, q = 710
RRR_algorithm Converged in 7227 iterations.
n = 40, r = 10, q = 810
n = 40, r = 20, q = 10
alternating_projections Converged in 2631 iterations.
RRR_algorithm Converged in 5480 iterations.
n = 40, r = 20, q = 110
n = 40, r = 20, q = 210
n = 40, r = 20, q = 310
n = 40, r = 30, q = 10
n = 70, r = 10, q = 10
alternating_projections Converged in 15 iterations.
RRR_algorithm Converged in 44 iterations.
n = 70, r = 10, q = 110
alternating_projections Converged in 28 iterations.
RRR_algorithm Converged in 67 iterations.
n = 70, r = 10, q = 210
alternating_projections Converged in 96 iterations.
RRR_algorithm Converged in 311 iterations.
n = 70, r = 10, q = 310
alternating_projections Converged in 132 iterations.
RRR_algorithm Converged in 325 iterations.
n = 70, r = 10, q = 410
alternating_projections Converged in 105 iterations.
RRR_algorithm Converged in 214 iterations.
n = 70, r = 10, q = 510
alternating_projections Converged in 76 iterations.
RRR_algorithm Converged in 201 iterations.
n = 70, r = 10, q = 610
alternating_projections Converged in 137 iterations.
RRR_algorithm Converged in 316 iterations.
n = 70, r = 10, q = 710
alternating_projections Converged in 120 iterations.
RRR_algorithm Converged in 144 iterations.
n = 70, r = 10, q = 810
alternating_projections Converged in 216 iterations.
RRR_algorithm Converged in 259 iterations.
n = 70, r = 10, q = 910
alternating_projections Converged in 181 iterations.
RRR_algorithm Converged in 448 iterations.
n = 70, r = 10, q = 1010
alternating_projections Converged in 235 iterations.
RRR_algorithm Converged in 351 iterations.
n = 70, r = 10, q = 1110
alternating_projections Converged in 612 iterations.
RRR_algorithm Converged in 1081 iterations.
n = 70, r = 10, q = 1210
alternating_projections Converged in 271 iterations.
RRR_algorithm Converged in 1000 iterations.
n = 70, r = 10, q = 1310
alternating_projections Converged in 439 iterations.
RRR_algorithm Converged in 524 iterations.
n = 70, r = 10, q = 1410
RRR_algorithm Converged in 685 iterations.
n = 70, r = 10, q = 1510
alternating_projections Converged in 516 iterations.
n = 70, r = 10, q = 1610
alternating_projections Converged in 433 iterations.
RRR_algorithm Converged in 613 iterations.
n = 70, r = 10, q = 1710
alternating_projections Converged in 543 iterations.
RRR_algorithm Converged in 634 iterations.
n = 70, r = 10, q = 1810
alternating_projections Converged in 726 iterations.
RRR_algorithm Converged in 638 iterations.
n = 70, r = 10, q = 1910
RRR_algorithm Converged in 1631 iterations.
n = 70, r = 10, q = 2010
alternating_projections Converged in 1066 iterations.
RRR_algorithm Converged in 811 iterations.
n = 70, r = 10, q = 2110
alternating_projections Converged in 1199 iterations.
RRR_algorithm Converged in 992 iterations.
n = 70, r = 10, q = 2210
alternating_projections Converged in 932 iterations.
RRR_algorithm Converged in 1439 iterations.
n = 70, r = 10, q = 2310
alternating_projections Converged in 2750 iterations.
RRR_algorithm Converged in 1613 iterations.
n = 70, r = 10, q = 2410
alternating_projections Converged in 3739 iterations.
RRR_algorithm Converged in 1140 iterations.
n = 70, r = 10, q = 2510
alternating_projections Converged in 2755 iterations.
RRR_algorithm Converged in 2709 iterations.
n = 70, r = 10, q = 2610
alternating_projections Converged in 5553 iterations.
RRR_algorithm Converged in 3435 iterations.
n = 70, r = 10, q = 2710
alternating_projections Converged in 4477 iterations.
RRR_algorithm Converged in 3653 iterations.
n = 70, r = 10, q = 2810
RRR_algorithm Converged in 8474 iterations.
n = 70, r = 10, q = 2910
RRR_algorithm Converged in 8886 iterations.
n = 70, r = 10, q = 3010
n = 70, r = 10, q = 3110
n = 70, r = 10, q = 3210
n = 70, r = 10, q = 3310
n = 70, r = 10, q = 3410
n = 70, r = 10, q = 3510
n = 70, r = 20, q = 10
alternating_projections Converged in 33 iterations.
RRR_algorithm Converged in 81 iterations.
n = 70, r = 20, q = 110
alternating_projections Converged in 633 iterations.
RRR_algorithm Converged in 481 iterations.
n = 70, r = 20, q = 210
alternating_projections Converged in 332 iterations.
RRR_algorithm Converged in 580 iterations.
n = 70, r = 20, q = 310
alternating_projections Converged in 1255 iterations.
RRR_algorithm Converged in 3166 iterations.
n = 70, r = 20, q = 410
RRR_algorithm Converged in 2896 iterations.
n = 70, r = 20, q = 510
alternating_projections Converged in 1604 iterations.
RRR_algorithm Converged in 2335 iterations.
n = 70, r = 20, q = 610
alternating_projections Converged in 7881 iterations.
RRR_algorithm Converged in 1679 iterations.
n = 70, r = 20, q = 710
alternating_projections Converged in 9766 iterations.
n = 70, r = 20, q = 810
alternating_projections Converged in 4230 iterations.
n = 70, r = 20, q = 910
RRR_algorithm Converged in 3077 iterations.
n = 70, r = 20, q = 1010
RRR_algorithm Converged in 4315 iterations.
n = 70, r = 20, q = 1110
alternating_projections Converged in 7503 iterations.
n = 70, r = 20, q = 1210
n = 70, r = 20, q = 1310
RRR_algorithm Converged in 9947 iterations.
n = 70, r = 20, q = 1410
RRR_algorithm Converged in 8154 iterations.
n = 70, r = 20, q = 1510
RRR_algorithm Converged in 8927 iterations.
n = 70, r = 20, q = 1610
RRR_algorithm Converged in 6129 iterations.
n = 70, r = 20, q = 1710
RRR_algorithm Converged in 8158 iterations.
n = 70, r = 20, q = 1810
n = 70, r = 20, q = 1910
n = 70, r = 20, q = 2010
n = 70, r = 20, q = 2110
n = 70, r = 20, q = 2210
n = 70, r = 20, q = 2310
n = 70, r = 20, q = 2410
n = 70, r = 30, q = 10
RRR_algorithm Converged in 1252 iterations.
n = 70, r = 30, q = 110
RRR_algorithm Converged in 5598 iterations.
n = 70, r = 30, q = 210
RRR_algorithm Converged in 8209 iterations.
n = 70, r = 30, q = 310
n = 70, r = 30, q = 410
n = 70, r = 30, q = 510
n = 70, r = 30, q = 610
n = 70, r = 30, q = 710
n = 70, r = 30, q = 810
n = 70, r = 30, q = 910
n = 70, r = 30, q = 1010
n = 70, r = 30, q = 1110
n = 70, r = 30, q = 1210
n = 70, r = 30, q = 1310
n = 70, r = 30, q = 1410
n = 70, r = 30, q = 1510
n = 70, r = 40, q = 10
n = 70, r = 40, q = 110
n = 70, r = 40, q = 210
n = 70, r = 40, q = 310
n = 70, r = 40, q = 410
n = 70, r = 40, q = 510
n = 70, r = 40, q = 610
n = 70, r = 40, q = 710
n = 70, r = 40, q = 810
n = 70, r = 50, q = 10
-----
n = 120, r = 30, q = 5
alternating_projections Converged in 80 iterations.
RRR_algorithm Converged in 67 iterations.
n = 120, r = 30, q = 50
RRR_algorithm Converged in 76 iterations.

"""

text1 = """
n = 40, r = 10, q = 10
RRR_algorithm Converged in 139 iterations.
n = 40, r = 10, q = 110
RRR_algorithm Converged in 1056 iterations.
n = 40, r = 10, q = 210
RRR_algorithm Converged in 1708 iterations.
n = 40, r = 10, q = 310
RRR_algorithm Converged in 1671 iterations.
n = 40, r = 10, q = 410
n = 40, r = 10, q = 510
n = 40, r = 10, q = 610
n = 40, r = 10, q = 710
RRR_algorithm Converged in 7227 iterations.
n = 40, r = 10, q = 810
n = 40, r = 20, q = 10
RRR_algorithm Converged in 5480 iterations.
n = 40, r = 20, q = 110
n = 40, r = 20, q = 210
n = 40, r = 20, q = 310
n = 40, r = 30, q = 10
n = 70, r = 10, q = 10
RRR_algorithm Converged in 44 iterations.
n = 70, r = 10, q = 110
RRR_algorithm Converged in 67 iterations.
n = 70, r = 10, q = 210
RRR_algorithm Converged in 311 iterations.
n = 70, r = 10, q = 310
RRR_algorithm Converged in 325 iterations.
n = 70, r = 10, q = 410
RRR_algorithm Converged in 214 iterations.
n = 70, r = 10, q = 510
RRR_algorithm Converged in 201 iterations.
n = 70, r = 10, q = 610
RRR_algorithm Converged in 316 iterations.
n = 70, r = 10, q = 710
RRR_algorithm Converged in 144 iterations.
n = 70, r = 10, q = 810
RRR_algorithm Converged in 259 iterations.
n = 70, r = 10, q = 910
RRR_algorithm Converged in 448 iterations.
n = 70, r = 10, q = 1010
RRR_algorithm Converged in 351 iterations.
n = 70, r = 10, q = 1110
RRR_algorithm Converged in 1081 iterations.
n = 70, r = 10, q = 1210
RRR_algorithm Converged in 1000 iterations.
n = 70, r = 10, q = 1310
RRR_algorithm Converged in 524 iterations.
n = 70, r = 10, q = 1410
RRR_algorithm Converged in 685 iterations.
n = 70, r = 10, q = 1510
n = 70, r = 10, q = 1610
RRR_algorithm Converged in 613 iterations.
n = 70, r = 10, q = 1710
RRR_algorithm Converged in 634 iterations.
n = 70, r = 10, q = 1810
RRR_algorithm Converged in 638 iterations.
n = 70, r = 10, q = 1910
RRR_algorithm Converged in 1631 iterations.
n = 70, r = 10, q = 2010
RRR_algorithm Converged in 811 iterations.
n = 70, r = 10, q = 2110
RRR_algorithm Converged in 992 iterations.
n = 70, r = 10, q = 2210
RRR_algorithm Converged in 1439 iterations.
n = 70, r = 10, q = 2310
RRR_algorithm Converged in 1613 iterations.
n = 70, r = 10, q = 2410
RRR_algorithm Converged in 1140 iterations.
n = 70, r = 10, q = 2510
RRR_algorithm Converged in 2709 iterations.
n = 70, r = 10, q = 2610
RRR_algorithm Converged in 3435 iterations.
n = 70, r = 10, q = 2710
RRR_algorithm Converged in 3653 iterations.
n = 70, r = 10, q = 2810
RRR_algorithm Converged in 8474 iterations.
n = 70, r = 10, q = 2910
RRR_algorithm Converged in 8886 iterations.
n = 70, r = 10, q = 3010
n = 70, r = 10, q = 3110
n = 70, r = 10, q = 3210
n = 70, r = 10, q = 3310
n = 70, r = 10, q = 3410
n = 70, r = 10, q = 3510
n = 70, r = 20, q = 10
RRR_algorithm Converged in 81 iterations.
n = 70, r = 20, q = 110
=RRR_algorithm Converged in 481 iterations.
n = 70, r = 20, q = 210
=RRR_algorithm Converged in 580 iterations.
n = 70, r = 20, q = 310
RRR_algorithm Converged in 3166 iterations.
n = 70, r = 20, q = 410
RRR_algorithm Converged in 2896 iterations.
n = 70, r = 20, q = 510
RRR_algorithm Converged in 2335 iterations.
n = 70, r = 20, q = 610
RRR_algorithm Converged in 1679 iterations.
n = 70, r = 20, q = 710
n = 70, r = 20, q = 810
n = 70, r = 20, q = 910
RRR_algorithm Converged in 3077 iterations.
n = 70, r = 20, q = 1010
RRR_algorithm Converged in 4315 iterations.
n = 70, r = 20, q = 1110
n = 70, r = 20, q = 1210
n = 70, r = 20, q = 1310
RRR_algorithm Converged in 9947 iterations.
n = 70, r = 20, q = 1410
RRR_algorithm Converged in 8154 iterations.
n = 70, r = 20, q = 1510
RRR_algorithm Converged in 8927 iterations.
n = 70, r = 20, q = 1610
RRR_algorithm Converged in 6129 iterations.
n = 70, r = 20, q = 1710
RRR_algorithm Converged in 8158 iterations.
n = 70, r = 20, q = 1810
n = 70, r = 20, q = 1910
n = 70, r = 20, q = 2010
n = 70, r = 20, q = 2110
n = 70, r = 20, q = 2210
n = 70, r = 20, q = 2310
n = 70, r = 20, q = 2410
n = 70, r = 30, q = 10
RRR_algorithm Converged in 1252 iterations.
n = 70, r = 30, q = 110
RRR_algorithm Converged in 5598 iterations.
n = 70, r = 30, q = 210
RRR_algorithm Converged in 8209 iterations.
n = 70, r = 30, q = 310
n = 70, r = 30, q = 410
n = 70, r = 30, q = 510
n = 70, r = 30, q = 610
n = 70, r = 30, q = 710
n = 70, r = 30, q = 810
n = 70, r = 30, q = 910
n = 70, r = 30, q = 1010
n = 70, r = 30, q = 1110
n = 70, r = 30, q = 1210
n = 70, r = 30, q = 1310
n = 70, r = 30, q = 1410
n = 70, r = 30, q = 1510
n = 70, r = 40, q = 10
n = 70, r = 40, q = 110
n = 70, r = 40, q = 210
n = 70, r = 40, q = 310
n = 70, r = 40, q = 410
n = 70, r = 40, q = 510
n = 70, r = 40, q = 610
n = 70, r = 40, q = 710
n = 70, r = 40, q = 810
n = 70, r = 50, q = 10


n = 20, r = 10, q = 10
n = 50, r = 10, q = 10
RRR_algorithm Converged in 64 iterations.
n = 50, r = 10, q = 110
RRR_algorithm Converged in 197 iterations.
n = 50, r = 10, q = 210
RRR_algorithm Converged in 599 iterations.
n = 50, r = 10, q = 310
RRR_algorithm Converged in 358 iterations.
n = 50, r = 10, q = 410
RRR_algorithm Converged in 313 iterations.
n = 50, r = 10, q = 510
RRR_algorithm Converged in 333 iterations.
n = 50, r = 10, q = 610
RRR_algorithm Converged in 579 iterations.
n = 50, r = 10, q = 710
RRR_algorithm Converged in 412 iterations.
n = 50, r = 10, q = 810
RRR_algorithm Converged in 1370 iterations.
n = 50, r = 10, q = 910
RRR_algorithm Converged in 1014 iterations.
n = 50, r = 10, q = 1010
RRR_algorithm Converged in 1346 iterations.
n = 50, r = 10, q = 1110
RRR_algorithm Converged in 2232 iterations.
n = 50, r = 10, q = 1210
RRR_algorithm Converged in 4036 iterations.
n = 50, r = 10, q = 1310
RRR_algorithm Converged in 5333 iterations.
n = 50, r = 10, q = 1410
RRR_algorithm Converged in 8979 iterations.
n = 50, r = 10, q = 1510
n = 50, r = 20, q = 10
RRR_algorithm Converged in 329 iterations.
n = 50, r = 20, q = 110
n = 50, r = 20, q = 210
n = 50, r = 20, q = 310
n = 50, r = 20, q = 410
n = 50, r = 20, q = 510
n = 50, r = 20, q = 610
n = 50, r = 20, q = 710
n = 50, r = 20, q = 810
n = 50, r = 30, q = 10
RRR_algorithm Converged in 5469 iterations.
n = 50, r = 30, q = 110
n = 50, r = 30, q = 210
n = 50, r = 30, q = 310
n = 50, r = 40, q = 10
n = 80, r = 10, q = 10
RRR_algorithm Converged in 39 iterations.
n = 80, r = 10, q = 110
RRR_algorithm Converged in 60 iterations.
n = 80, r = 10, q = 210
RRR_algorithm Converged in 66 iterations.
n = 80, r = 10, q = 310
RRR_algorithm Converged in 72 iterations.
n = 80, r = 10, q = 410
RRR_algorithm Converged in 81 iterations.
n = 80, r = 10, q = 510
RRR_algorithm Converged in 84 iterations.
n = 80, r = 10, q = 610
RRR_algorithm Converged in 85 iterations.
n = 80, r = 10, q = 710
RRR_algorithm Converged in 99 iterations.
n = 80, r = 10, q = 810
RRR_algorithm Converged in 107 iterations.
n = 80, r = 10, q = 910
RRR_algorithm Converged in 104 iterations.
n = 80, r = 10, q = 1010
RRR_algorithm Converged in 119 iterations.
n = 80, r = 10, q = 1110
RRR_algorithm Converged in 117 iterations.
n = 80, r = 10, q = 1210
RRR_algorithm Converged in 142 iterations.
n = 80, r = 10, q = 1310
RRR_algorithm Converged in 130 iterations.
n = 80, r = 10, q = 1410
RRR_algorithm Converged in 173 iterations.
n = 80, r = 10, q = 1510
RRR_algorithm Converged in 144 iterations.
n = 80, r = 10, q = 1610
RRR_algorithm Converged in 253 iterations.
n = 80, r = 10, q = 1710
RRR_algorithm Converged in 300 iterations.
n = 80, r = 10, q = 1810
RRR_algorithm Converged in 373 iterations.
n = 80, r = 10, q = 1910
RRR_algorithm Converged in 298 iterations.
n = 80, r = 10, q = 2010
RRR_algorithm Converged in 1343 iterations.
n = 80, r = 10, q = 2110
RRR_algorithm Converged in 270 iterations.
n = 80, r = 10, q = 2210
RRR_algorithm Converged in 429 iterations.
n = 80, r = 10, q = 2310
RRR_algorithm Converged in 376 iterations.
n = 80, r = 10, q = 2410
RRR_algorithm Converged in 329 iterations.
n = 80, r = 10, q = 2510
RRR_algorithm Converged in 422 iterations.
n = 80, r = 10, q = 2610
RRR_algorithm Converged in 443 iterations.
n = 80, r = 10, q = 2710
RRR_algorithm Converged in 878 iterations.
n = 80, r = 10, q = 2810
RRR_algorithm Converged in 1216 iterations.
n = 80, r = 10, q = 2910
RRR_algorithm Converged in 728 iterations.
n = 80, r = 10, q = 3010
RRR_algorithm Converged in 1113 iterations.
n = 80, r = 10, q = 3110
RRR_algorithm Converged in 1089 iterations.
n = 80, r = 10, q = 3210
RRR_algorithm Converged in 1100 iterations.
n = 80, r = 10, q = 3310
RRR_algorithm Converged in 1377 iterations.
n = 80, r = 10, q = 3410
RRR_algorithm Converged in 1808 iterations.
n = 80, r = 10, q = 3510
RRR_algorithm Converged in 1910 iterations.
n = 80, r = 10, q = 3610
RRR_algorithm Converged in 2082 iterations.
n = 80, r = 10, q = 3710
RRR_algorithm Converged in 2613 iterations.
n = 80, r = 10, q = 3810
RRR_algorithm Converged in 3047 iterations.
n = 80, r = 10, q = 3910
RRR_algorithm Converged in 2902 iterations.
n = 80, r = 10, q = 4010
RRR_algorithm Converged in 3751 iterations.
n = 80, r = 10, q = 4110
RRR_algorithm Converged in 4181 iterations.
n = 80, r = 10, q = 4210
RRR_algorithm Converged in 6613 iterations.
n = 80, r = 10, q = 4310
RRR_algorithm Converged in 7735 iterations.
n = 80, r = 10, q = 4410
n = 80, r = 10, q = 4510
n = 80, r = 10, q = 4610
n = 80, r = 10, q = 4710
n = 80, r = 10, q = 4810
n = 80, r = 20, q = 10
RRR_algorithm Converged in 70 iterations.
n = 80, r = 20, q = 110
RRR_algorithm Converged in 194 iterations.
n = 80, r = 20, q = 210
RRR_algorithm Converged in 1014 iterations.
n = 80, r = 20, q = 310
RRR_algorithm Converged in 933 iterations.
n = 80, r = 20, q = 410
RRR_algorithm Converged in 1022 iterations.
n = 80, r = 20, q = 510
RRR_algorithm Converged in 1289 iterations.
n = 80, r = 20, q = 610
RRR_algorithm Converged in 1164 iterations.
n = 80, r = 20, q = 710
RRR_algorithm Converged in 720 iterations.
n = 80, r = 20, q = 810
RRR_algorithm Converged in 1363 iterations.
n = 80, r = 20, q = 910
RRR_algorithm Converged in 3969 iterations.
n = 80, r = 20, q = 1010
RRR_algorithm Converged in 3942 iterations.
n = 80, r = 20, q = 1110
RRR_algorithm Converged in 1745 iterations.
n = 80, r = 20, q = 1210
RRR_algorithm Converged in 1618 iterations.
n = 80, r = 20, q = 1310
RRR_algorithm Converged in 1513 iterations.
n = 80, r = 20, q = 1410
RRR_algorithm Converged in 1510 iterations.
n = 80, r = 20, q = 1510
RRR_algorithm Converged in 1545 iterations.
n = 80, r = 20, q = 1610
RRR_algorithm Converged in 2921 iterations.
n = 80, r = 20, q = 1710
RRR_algorithm Converged in 1589 iterations.
n = 80, r = 20, q = 1810
RRR_algorithm Converged in 1409 iterations.
n = 80, r = 20, q = 1910
RRR_algorithm Converged in 1723 iterations.
n = 80, r = 20, q = 2010
RRR_algorithm Converged in 6243 iterations.
n = 80, r = 20, q = 2110
RRR_algorithm Converged in 3753 iterations.
n = 80, r = 20, q = 2210
RRR_algorithm Converged in 2647 iterations.
n = 80, r = 20, q = 2310
RRR_algorithm Converged in 4780 iterations.
n = 80, r = 20, q = 2410
RRR_algorithm Converged in 3090 iterations.
n = 80, r = 20, q = 2510
RRR_algorithm Converged in 2738 iterations.
n = 80, r = 20, q = 2610
RRR_algorithm Converged in 4173 iterations.
n = 80, r = 20, q = 2710
RRR_algorithm Converged in 4810 iterations.
n = 80, r = 20, q = 2810
RRR_algorithm Converged in 6313 iterations.
n = 80, r = 20, q = 2910
RRR_algorithm Converged in 8928 iterations.
n = 80, r = 20, q = 3010
n = 80, r = 20, q = 3110
n = 80, r = 20, q = 3210
n = 80, r = 20, q = 3310
n = 80, r = 20, q = 3410
n = 80, r = 20, q = 3510
n = 80, r = 30, q = 10
RRR_algorithm Converged in 3753 iterations.
n = 80, r = 30, q = 110
n = 80, r = 30, q = 210
n = 80, r = 30, q = 310
n = 80, r = 30, q = 410
n = 80, r = 30, q = 510
n = 80, r = 30, q = 610
n = 80, r = 30, q = 710
n = 80, r = 30, q = 810
n = 80, r = 30, q = 910
n = 80, r = 30, q = 1010
n = 80, r = 30, q = 1110
n = 80, r = 30, q = 1210
n = 80, r = 30, q = 1310
n = 80, r = 30, q = 1410
n = 80, r = 30, q = 1510
n = 80, r = 30, q = 1610
n = 80, r = 30, q = 1710
n = 80, r = 30, q = 1810
n = 80, r = 30, q = 1910
n = 80, r = 30, q = 2010
n = 80, r = 30, q = 2110
n = 80, r = 30, q = 2210
n = 80, r = 30, q = 2310
n = 80, r = 30, q = 2410
n = 80, r = 40, q = 10
n = 80, r = 40, q = 110
n = 80, r = 40, q = 210
n = 80, r = 40, q = 310
n = 80, r = 40, q = 410
n = 80, r = 40, q = 510
n = 80, r = 40, q = 610
n = 80, r = 40, q = 710
n = 80, r = 40, q = 810
n = 80, r = 40, q = 910
n = 80, r = 40, q = 1010
n = 80, r = 40, q = 1110
n = 80, r = 40, q = 1210
n = 80, r = 40, q = 1310
n = 80, r = 40, q = 1410
n = 80, r = 40, q = 1510
n = 80, r = 50, q = 10
n = 80, r = 50, q = 110
n = 80, r = 50, q = 210
n = 80, r = 50, q = 310
n = 80, r = 50, q = 410
n = 80, r = 50, q = 510
n = 80, r = 50, q = 610
n = 80, r = 50, q = 710
n = 80, r = 50, q = 810
n = 80, r = 60, q = 10
-----
n = 120, r = 30, q = 500
RRR_algorithm Converged in 1564 iterations.
n = 120, r = 30, q = 5000
RRR_algorithm Converged in 9307 iterations.
n = 120, r = 10, q = 5000
RRR_algorithm Converged in 154 iterations.
n = 120, r = 10, q = 10000
RRR_algorithm Converged in 1864 iterations.
n = 20, r = 2, q = 350
n = 60, r = 30, q = 350
n = 20, r = 2, q = 300
RRR_algorithm Converged in 5572 iterations.

"""

lines = text1.strip().split('\n')
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

import matplotlib.pyplot as plt
import numpy as np


# Define the function q = (n - r)^2
def q_function(n, r):
    return (n - r) ** 2


# Generate data for n and r
n_values = np.linspace(10, 125, 50)
r_values = np.linspace(10, 125, 50)

n_mesh, r_mesh = np.meshgrid(n_values, r_values)

# Filter out values where r is greater than n
valid_indices = r_mesh <= n_mesh
n_values_valid = n_mesh[valid_indices]
r_values_valid = r_mesh[valid_indices]

# Calculate q values for valid indices
q_values_valid = q_function(n_values_valid, r_values_valid)


# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for calculated points
ax.scatter(n_values_valid, r_values_valid, q_values_valid, c=q_values_valid, cmap='viridis', label='Calculated Points')

# Scatter plot for random points
# ax.scatter(n_random, r_random, q_random, c='red', marker='o', label='Random Points')
# ax.scatter(n_random, r_random, q_random, c='red', marker='x', label='Random Points')


# Set labels
ax.set_xlabel('n')
ax.set_ylabel('r')
ax.set_zlabel('q')

for element in n_r_q_n_iter:
    n, r, q = element[:3]
    if(n ==120 and r ==30 and q ==5):
        print("item:", element)
        
        
    AP_iter, RRR_iter = element[3:5]
    if AP_iter == -1 and RRR_iter == -1:
        ax.scatter(n, r, q, c='black', marker='x')
    elif AP_iter == -1:
        ax.scatter(n, r, q, c='orange', marker='o')
    elif RRR_iter == -1:
        ax.scatter(n, r, q, c='blue', marker='o')
    else:
        ax.scatter(n, r, q, c='green', marker='o')

# Show the legend
ax.legend()

# Show the plot
plt.show()
