import re


text = """

n = 40, r = 10, q = 10
RRR_algorithm Converged in 139 iterations.
n = 40, r = 10, q = 110
alternating_projections Converged in 860 iterations.
RRR_algorithm Converged in 1056 iterations.
n = 40, r = 10, q = 210
alternating_projections Converged in 8241 iterations.
RRR_algorithm Converged in 1686 iterations.
n = 40, r = 10, q = 310
RRR_algorithm Converged in 1669 iterations.
n = 40, r = 10, q = 410
n = 40, r = 10, q = 510
n = 40, r = 10, q = 610
RRR_algorithm Converged in 9537 iterations.
n = 40, r = 10, q = 710
RRR_algorithm Converged in 6708 iterations.
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
RRR_algorithm Converged in 1068 iterations.
n = 70, r = 10, q = 1210
alternating_projections Converged in 271 iterations.
RRR_algorithm Converged in 1001 iterations.
n = 70, r = 10, q = 1310
alternating_projections Converged in 439 iterations.
RRR_algorithm Converged in 524 iterations.
n = 70, r = 10, q = 1410
RRR_algorithm Converged in 684 iterations.
n = 70, r = 10, q = 1510
alternating_projections Converged in 516 iterations.
n = 70, r = 10, q = 1610
alternating_projections Converged in 433 iterations.
RRR_algorithm Converged in 532 iterations.
n = 70, r = 10, q = 1710
alternating_projections Converged in 543 iterations.
RRR_algorithm Converged in 629 iterations.
n = 70, r = 10, q = 1810
alternating_projections Converged in 726 iterations.
RRR_algorithm Converged in 634 iterations.
n = 70, r = 10, q = 1910
RRR_algorithm Converged in 1619 iterations.
n = 70, r = 10, q = 2010
alternating_projections Converged in 1066 iterations.
RRR_algorithm Converged in 814 iterations.
n = 70, r = 10, q = 2110
alternating_projections Converged in 1199 iterations.
RRR_algorithm Converged in 997 iterations.
n = 70, r = 10, q = 2210
alternating_projections Converged in 932 iterations.
RRR_algorithm Converged in 1454 iterations.
n = 70, r = 10, q = 2310
alternating_projections Converged in 2750 iterations.
RRR_algorithm Converged in 1613 iterations.
n = 70, r = 10, q = 2410
alternating_projections Converged in 3739 iterations.
RRR_algorithm Converged in 1108 iterations.
n = 70, r = 10, q = 2510
alternating_projections Converged in 2755 iterations.
RRR_algorithm Converged in 2706 iterations.
n = 70, r = 10, q = 2610
alternating_projections Converged in 5553 iterations.
RRR_algorithm Converged in 3376 iterations.
n = 70, r = 10, q = 2710
alternating_projections Converged in 4477 iterations.
RRR_algorithm Converged in 3653 iterations.
n = 70, r = 10, q = 2810
RRR_algorithm Converged in 8885 iterations.
n = 70, r = 10, q = 2910
RRR_algorithm Converged in 8615 iterations.
n = 70, r = 10, q = 3010
n = 70, r = 10, q = 3110
n = 70, r = 10, q = 3210
'n = 70, r = 20, q = 1710\nRRR_algorithm Converged in 8158 iterations.\nn = 70, r = 20, q = 1810\nn = 70, r = 20, q = 1910\nn = 70, r = 20, q = 2010\nn = 70, r = 20, q = 2110\nn = 70, r = 20, q = 2210\nn = 70, r = 20, q = 2310\nn = 70, r = 20, q = 2410\nn = 70, r = 30, q = 10\nRRR_algorithm Converged in 1252 iterations.\nn = 70, r = 30, q = 110\nRRR_algorithm Converged in 5598 iterations.\nn = 70, r = 30, q = 210\nRRR_algorithm Converged in 8209 iterations.\nn = 70, r = 30, q = 310\nn = 70, r = 30, q = 410\nn = 70, r = 30, q = 510\nn = 70, r = 30, q = 610\nn = 70, r = 30, q = 710\nn = 70, r = 30, q = 810\nn = 70, r = 30, q = 910\nn = 70, r = 30, q = 1010\nn = 70, r = 30, q = 1110\nn = 70, r = 30, q = 1210\nn = 70, r = 30, q = 1310\nn = 70, r = 30, q = 1410\nn = 70, r = 30, q = 1510\nn = 100, r = 10, q = 10\nalternating_projections Converged in 12 iterations.\nRRR_algorithm Converged in 35 iterations.\nn = 100, r = 10, q = 110\nalternating_projections Converged in 15 iterations.\nRRR_algorithm Converged in 44 iterations.\nn = 100, r = 10, q = 210\nalternating_projections Converged in 15 iterations.\nRRR_algorithm Converged in 46 iterations.\nn = 100, r = 10, q = 310\nalternating_projections Converged in 20 iterations.\nRRR_algorithm Converged in 54 iterations.\nn = 100, r = 10, q = 410\nalternating_projections Converged in 27 iterations.\nRRR_algorithm Converged in 54 iterations.\nn = 100, r = 10, q = 510\nalternating_projections Converged in 26 iterations.\nRRR_algorithm Converged in 66 iterations.\nn = 100, r = 10, q = 610\nalternating_projections Converged in 25 iterations.\nRRR_algorithm Converged in 67 iterations.\nn = 100, r = 10, q = 710\nalternating_projections Converged in 28 iterations.\nRRR_algorithm Converged in 74 iterations.\nn = 100, r = 10, q = 810\nalternating_projections Converged in 30 iterations.\nRRR_algorithm Converged in 78 iterations.\nn = 100, r = 10, q = 910\nalternating_projections Converged in 32 iterations.\nRRR_algorithm Converged in 78 iterations.\nn = 100, r = 10, q = 1010\nalternating_projections Converged in 36 iterations.\nRRR_algorithm Converged in 79 iterations.\nn = 100, r = 10, q = 1110\nalternating_projections Converged in 44 iterations.\nRRR_algorithm Converged in 78 iterations.\nn = 100, r = 10, q = 1210\nalternating_projections Converged in 34 iterations.\nRRR_algorithm Converged in 80 iterations.\nn = 100, r = 10, q = 1310\nalternating_projections Converged in 88 iterations.\nRRR_algorithm Converged in 86 iterations.\nn = 100, r = 10, q = 1410\nalternating_projections Converged in 99 iterations.\nRRR_algorithm Converged in 85 iterations.\nn = 100, r = 10, q = 1510\nalternating_projections Converged in 59 iterations.\nRRR_algorithm Converged in 85 iterations.\nn = 100, r = 10, q = 1610\nalternating_projections Converged in 98 iterations.\nRRR_algorithm Converged in 153 iterations.\nn = 100, r = 10, q = 1710\nalternating_projections Converged in 106 iterations.\nRRR_algorithm Converged in 187 iterations.\nn = 100, r = 10, q = 1810\nalternating_projections Converged in 123 iterations.\nRRR_algorithm Converged in 245 iterations.\nn = 100, r = 10, q = 1910\nalternating_projections Converged in 149 iterations.\nRRR_algorithm Converged in 233 iterations.\nn = 100, r = 10, q = 2010\nalternating_projections Converged in 223 iterations.\nRRR_algorithm Converged in 195 iterations.\nn = 100, r = 10, q = 2110\nalternating_projections Converged in 207 iterations.\nRRR_algorithm Converged in 246 iterations.\nn = 100, r = 10, q = 2210\nalternating_projections Converged in 207 iterations.\nRRR_algorithm Converged in 504 iterations.\nn = 100, r = 10, q = 2310\nalternating_projections Converged in 184 iterations.\nRRR_algorithm Converged in 251 iterations.\nn = 100, r = 10, q = 2410\nalternating_projections Converged in 193 iterations.\nRRR_algorithm Converged in 276 iterations.\nn = 100, r = 10, q = 2510\nalternating_projections Converged in 249 iterations.\nRRR_algorithm Converged in 262 iterations.\nn = 100, r = 10, q = 2610\nalternating_projections Converged in 268 iterations.\nRRR_algorithm Converged in 265 iterations.\nn = 100, r = 10, q = 2710\nalternating_projections Converged in 213 iterations.\nRRR_algorithm Converged in 369 iterations.\nn = 100, r = 10, q = 2810\nalternating_projections Converged in 303 iterations.\nRRR_algorithm Converged in 334 iterations.\nn = 100, r = 10, q = 2910\nalternating_projections Converged in 570 iterations.\nRRR_algorithm Converged in 340 iterations.\nn = 100, r = 10, q = 3010\nalternating_projections Converged in 358 iterations.\nRRR_algorithm Converged in 307 iterations.\nn = 100, r = 10, q = 3110\nalternating_projections Converged in 423 iterations.\nRRR_algorithm Converged in 325 iterations.\nn = 100, r = 10, q = 3210\nalternating_projections Converged in 228 iterations.\nRRR_algorithm Converged in 342 iterations.\nn = 100, r = 10, q = 3310\nalternating_projections Converged in 696 iterations.\nRRR_algorithm Converged in 440 iterations.\nn = 100, r = 10, q = 3410\nalternating_projections Converged in 442 iterations.\nRRR_algorithm Converged in 463 iterations.\nn = 100, r = 10, q = 3510\nalternating_projections Converged in 476 iterations.\nRRR_algorithm Converged in 348 iterations.\nn = 100, r = 10, q = 3610\nalternating_projections Converged in 735 iterations.\nRRR_algorithm Converged in 366 iterations.\nn = 100, r = 10, q = 3710\nalternating_projections Converged in 605 iterations.\nRRR_algorithm Converged in 336 iterations.\nn = 100, r = 10, q = 3810\nalternating_projections Converged in 862 iterations.\nRRR_algorithm Converged in 895 iterations.\nn = 100, r = 10, q = 3910\nalternating_projections Converged in 1823 iterations.\nRRR_algorithm Converged in 387 iterations.\nn = 100, r = 10, q = 4010\nalternating_projections Converged in 1054 iterations.\nRRR_algorithm Converged in 420 iterations.\nn = 100, r = 10, q = 4110\nalternating_projections Converged in 453 iterations.\nRRR_algorithm Converged in 360 iterations.\nn = 100, r = 10, q = 4210\nalternating_projections Converged in 1611 iterations.\nRRR_algorithm Converged in 507 iterations.\nn = 100, r = 10, q = 4310\nalternating_projections Converged in 440 iterations.\nRRR_algorithm Converged in 493 iterations.\nn = 100, r = 10, q = 4410\nalternating_projections Converged in 4100 iterations.\nRRR_algorithm Converged in 550 iterations.\nn = 100, r = 10, q = 4510\nalternating_projections Converged in 1233 iterations.\nRRR_algorithm Converged in 489 iterations.\nn = 100, r = 10, q = 4610\nalternating_projections Converged in 2625 iterations.\nRRR_algorithm Converged in 667 iterations.\nn = 100, r = 10, q = 4710\nalternating_projections Converged in 555 iterations.\nRRR_algorithm Converged in 511 iterations.\nn = 100, r = 10, q = 4810\nalternating_projections Converged in 551 iterations.\nRRR_algorithm Converged in 627 iterations.\nn = 100, r = 10, q = 4910\nalternating_projections Converged in 487 iterations.\nRRR_algorithm Converged in 583 iterations.\nn = 100, r = 10, q = 5010\nRRR_algorithm Converged in 742 iterations.\nn = 100, r = 10, q = 5110\nalternating_projections Converged in 930 iterations.\nRRR_algorithm Converged in 1067 iterations.\nn = 100, r = 10, q = 5210\nalternating_projections Converged in 1711 iterations.\nRRR_algorithm Converged in 1042 iterations.\nn = 100, r = 10, q = 5310\nalternating_projections Converged in 1502 iterations.\nRRR_algorithm Converged in 1077 iterations.\nn = 100, r = 10, q = 5410\nalternating_projections Converged in 2411 iterations.\nRRR_algorithm Converged in 825 iterations.\nn = 100, r = 10, q = 5510\nalternating_projections Converged in 1830 iterations.\nRRR_algorithm Converged in 803 iterations.\nn = 100, r = 10, q = 5610\nalternating_projections Converged in 2218 iterations.\nRRR_algorithm Converged in 968 iterations.\nn = 100, r = 10, q = 5710\nRRR_algorithm Converged in 1186 iterations.\nn = 100, r = 10, q = 5810\nalternating_projections Converged in 1296 iterations.\nRRR_algorithm Converged in 1084 iterations.\nn = 100, r = 10, q = 5910\nalternating_projections Converged in 2007 iterations.\nRRR_algorithm Converged in 1158 iterations.\nn = 100, r = 10, q = 6010\nalternating_projections Converged in 2058 iterations.\nRRR_algorithm Converged in 1075 iterations.\nn = 100, r = 10, q = 6110\nRRR_algorithm Converged in 1179 iterations.\nn = 100, r = 10, q = 6210\nRRR_algorithm Converged in 1396 iterations.\nn = 100, r = 10, q = 6310\nRRR_algorithm Converged in 1713 iterations.\nn = 100, r = 10, q = 6410\nRRR_algorithm Converged in 1601 iterations.\nn = 100, r = 10, q = 6510\nRRR_algorithm Converged in 2953 iterations.\nn = 100, r = 10, q = 6610\nRRR_algorithm Converged in 2008 iterations.\nn = 100, r = 10, q = 6710\nn = 100, r = 10, q = 6810\nRRR_algorithm Converged in 3660 iterations.\nn = 100, r = 10, q = 6910\nRRR_algorithm Converged in 3860 iterations.\nn = 100, r = 10, q = 7010\nRRR_algorithm Converged in 4849 iterations.\nn = 100, r = 10, q = 7110\nRRR_algorithm Converged in 6172 iterations.\nn = 100, r = 10, q = 7210\nRRR_algorithm Converged in 8480 iterations.\nn = 100, r = 10, q = 7310\nn = 100, r = 10, q = 7410\nn = 100, r = 10, q = 7510\nn = 100, r = 10, q = 7610\nn = 100, r = 10, q = 7710\nn = 100, r = 10, q = 7810\nn = 100, r = 10, q = 7910\nn = 100, r = 10, q = 8010\nn = 100, r = 20, q = 10\nalternating_projections Converged in 24 iterations.\nRRR_algorithm Converged in 62 iterations.\nn = 100, r = 20, q = 110\nalternating_projections Converged in 100 iterations.\nRRR_algorithm Converged in 169 iterations.\nn = 100, r = 20, q = 210\nalternating_projections Converged in 89 iterations.\nRRR_algorithm Converged in 267 iterations.\nn = 100, r = 20, q = 310\nalternating_projections Converged in 86 iterations.\nRRR_algorithm Converged in 115 iterations.\nn = 100, r = 20, q = 410\nalternating_projections Converged in 176 iterations.\nRRR_algorithm Converged in 909 iterations.\nn = 100, r = 20, q = 510\nalternating_projections Converged in 394 iterations.\nRRR_algorithm Converged in 983 iterations.\nn = 100, r = 20, q = 610\nalternating_projections Converged in 312 iterations.\nRRR_algorithm Converged in 590 iterations.\nn = 100, r = 20, q = 710\nalternating_projections Converged in 197 iterations.\nRRR_algorithm Converged in 705 iterations.\nn = 100, r = 20, q = 810\nalternating_projections Converged in 439 iterations.\nRRR_algorithm Converged in 769 iterations.\nn = 100, r = 20, q = 910\nalternating_projections Converged in 497 iterations.\nRRR_algorithm Converged in 2061 iterations.\nn = 100, r = 20, q = 1010\nalternating_projections Converged in 772 iterations.\nRRR_algorithm Converged in 1481 iterations.\nn = 100, r = 20, q = 1110\nalternating_projections Converged in 914 iterations.\nRRR_algorithm Converged in 2073 iterations.\nn = 100, r = 20, q = 1210\nalternating_projections Converged in 810 iterations.\nRRR_algorithm Converged in 2131 iterations.\nn = 100, r = 20, q = 1310\nalternating_projections Converged in 896 iterations.\nn = 100, r = 20, q = 1410\nRRR_algorithm Converged in 3120 iterations.\nn = 100, r = 20, q = 1510\nalternating_projections Converged in 954 iterations.\nRRR_algorithm Converged in 1926 iterations.\nn = 100, r = 20, q = 1610\nn = 100, r = 20, q = 1710\nRRR_algorithm Converged in 2384 iterations.\nn = 100, r = 20, q = 1810\nn = 100, r = 20, q = 1910\nn = 100, r = 20, q = 2010\nRRR_algorithm Converged in 3140 iterations.\nn = 100, r = 20, q = 2110\nRRR_algorithm Converged in 2396 iterations.\nn = 100, r = 20, q = 2210\nRRR_algorithm Converged in 2091 iterations.\nn = 100, r = 20, q = 2310\nRRR_algorithm Converged in 2268 iterations.\nn = 100, r = 20, q = 2410\nRRR_algorithm Converged in 1157 iterations.\nn = 100, r = 20, q = 2510\nalternating_projections Converged in 1913 iterations.\nRRR_algorithm Converged in 1513 iterations.\nn = 100, r = 20, q = 2610\nalternating_projections Converged in 4934 iterations.\nRRR_algorithm Converged in 1291 iterations.\nn = 100, r = 20, q = 2710\nalternating_projections Converged in 7335 iterations.\nRRR_algorithm Converged in 1153 iterations.\nn = 100, r = 20, q = 2810\nalternating_projections Converged in 2518 iterations.\nRRR_algorithm Converged in 1176 iterations.\nn = 100, r = 20, q = 2910\nRRR_algorithm Converged in 3383 iterations.\nn = 100, r = 20, q = 3010\nalternating_projections Converged in 2097 iterations.\nRRR_algorithm Converged in 1240 iterations.\nn = 100, r = 20, q = 3110\nRRR_algorithm Converged in 4054 iterations.\nn = 100, r = 20, q = 3210\nalternating_projections Converged in 3544 iterations.\nRRR_algorithm Converged in 4864 iterations.\nn = 100, r = 20, q = 3310\nalternating_projections Converged in 2313 iterations.\nRRR_algorithm Converged in 1481 iterations.\nn = 100, r = 20, q = 3410\nRRR_algorithm Converged in 3106 iterations.\nn = 100, r = 20, q = 3510\nalternating_projections Converged in 3225 iterations.\nRRR_algorithm Converged in 2215 iterations.\nn = 100, r = 20, q = 3610\nRRR_algorithm Converged in 4470 iterations.\nn = 100, r = 20, q = 3710\nn = 100, r = 20, q = 3810\nRRR_algorithm Converged in 2175 iterations.\nn = 100, r = 20, q = 3910\nalternating_projections Converged in 4300 iterations.\nRRR_algorithm Converged in 2073 iterations.\nn = 100, r = 20, q = 4010\nRRR_algorithm Converged in 1472 iterations.\nn = 100, r = 20, q = 4110\nRRR_algorithm Converged in 2591 iterations.\nn = 100, r = 20, q = 4210\nRRR_algorithm Converged in 5317 iterations.\nn = 100, r = 20, q = 4310\nRRR_algorithm Converged in 4348 iterations.\nn = 100, r = 20, q = 4410\nRRR_algorithm Converged in 2493 iterations.\nn = 100, r = 20, q = 4510\nRRR_algorithm Converged in 2832 iterations.\nn = 100, r = 20, q = 4610\nRRR_algorithm Converged in 4084 iterations.\nn = 100, r = 20, q = 4710\nRRR_algorithm Converged in 2512 iterations.\nn = 100, r = 20, q = 4810\nRRR_algorithm Converged in 3255 iterations.\nn = 100, r = 20, q = 4910\nRRR_algorithm Converged in 3695 iterations.\nn = 100, r = 20, q = 5010\nn = 100, r = 20, q = 5110\nRRR_algorithm Converged in 4175 iterations.\nn = 100, r = 20, q = 5210\nRRR_algorithm Converged in 5047 iterations.\nn = 100, r = 20, q = 5310\nRRR_algorithm Converged in 5875 iterations.\nn = 100, r = 20, q = 5410\nRRR_algorithm Converged in 7498 iterations.\nn = 100, r = 20, q = 5510\nRRR_algorithm Converged in 9742 iterations.\nn = 100, r = 20, q = 5610\nn = 100, r = 20, q = 5710\nn = 100, r = 20, q = 5810\nn = 100, r = 20, q = 5910\nn = 100, r = 20, q = 6010\nn = 100, r = 20, q = 6110\nn = 100, r = 20, q = 6210\nn = 100, r = 20, q = 6310\nn = 100, r = 30, q = 10\nalternating_projections Converged in 1401 iterations.\nRRR_algorithm Converged in 2167 iterations.\nn = 100, r = 30, q = 110\nalternating_projections Converged in 594 iterations.\nRRR_algorithm Converged in 3015 iterations.\nn = 100, r = 30, q = 210\nRRR_algorithm Converged in 1224 iterations.\nn = 100, r = 30, q = 310\nRRR_algorithm Converged in 1163 iterations.\nn = 100, r = 30, q = 410\nalternating_projections Converged in 2614 iterations.\nRRR_algorithm Converged in 6360 iterations.\nn = 100, r = 30, q = 510\nalternating_projections Converged in 2434 iterations.\nRRR_algorithm Converged in 7179 iterations.\nn = 100, r = 30, q = 610\nalternating_projections Converged in 2639 iterations.\nRRR_algorithm Converged in 9402 iterations.\nn = 100, r = 30, q = 710\nalternating_projections Converged in 3269 iterations.\nn = 100, r = 30, q = 810\nRRR_algorithm Converged in 5016 iterations.\nn = 100, r = 30, q = 910\nalternating_projections Converged in 7204 iterations.\nRRR_algorithm Converged in 9503 iterations.\nn = 100, r = 30, q = 1010\nn = 100, r = 30, q = 1110\nalternating_projections Converged in 5966 iterations.\nn = 100, r = 30, q = 1210\nn = 100, r = 30, q = 1310\nRRR_algorithm Converged in 8221 iterations.\nn = 100, r = 30, q = 1410\nn = 100, r = 30, q = 1510\nalternating_projections Converged in 8372 iterations.\nRRR_algorithm Converged in 6152 iterations.\nn = 100, r = 30, q = 1610\nalternating_projections Converged in 6646 iterations.\nn = 100, r = 30, q = 1710\nn = 100, r = 30, q = 1810\nn = 100, r = 30, q = 1910\nn = 100, r = 30, q = 2010\nRRR_algorithm Converged in 5673 iterations.\nn = 100, r = 30, q = 2110\nRRR_algorithm Converged in 7002 iterations.\nn = 100, r = 30, q = 2210\nRRR_algorithm Converged in 6994 iterations.\nn = 100, r = 30, q = 2310\nRRR_algorithm Converged in 7532 iterations.\nn = 100, r = 30, q = 2410\nalternating_projections Converged in 9270 iterations.\nRRR_algorithm Converged in 5165 iterations.\nn = 100, r = 30, q = 2510\nRRR_algorithm Converged in 8008 iterations.\nn = 100, r = 30, q = 2610\nRRR_algorithm Converged in 6444 iterations.\nn = 100, r = 30, q = 2710\nRRR_algorithm Converged in 7031 iterations.\nn = 100, r = 30, q = 2810\nRRR_algorithm Converged in 7766 iterations.\nn = 100, r = 30, q = 2910\nn = 100, r = 30, q = 3010\nn = 100, r = 30, q = 3110\nn = 100, r = 30, q = 3210\nn = 100, r = 30, q = 3310\nn = 100, r = 30, q = 3410\nn = 100, r = 30, q = 3510\nRRR_algorithm Converged in 9166 iterations.\nn = 100, r = 30, q = 3610\nn = 100, r = 30, q = 3710\nn = 100, r = 30, q = 3810\nn = 100, r = 30, q = 3910\nn = 100, r = 30, q = 4010\nn = 100, r = 30, q = 4110\nn = 100, r = 30, q = 4210\nn = 100, r = 30, q = 4310\nn = 100, r = 30, q = 4410\nn = 100, r = 30, q = 4510\nn = 100, r = 30, q = 4610\nn = 100, r = 30, q = 4710\nn = 100, r = 30, q = 4810\nn = 100, r = 40, q = 10\nn = 100, r = 40, q = 110\nRRR_algorithm Converged in 6311 iterations.\nn = 100, r = 40, q = 210\nRRR_algorithm Converged in 6443 iterations.\nn = 100, r = 40, q = 310\nn = 100, r = 40, q = 410\nn = 100, r = 40, q = 510\nn = 100, r = 40, q = 610\nRRR_algorithm Converged in 8716 iterations.\nn = 100, r = 40, q = 710'
"""
lines = text.strip().split('\n')
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

for item in n_r_q_n_iter:
    n, r, q = item[:3]
    AP_iter, RRR_iter = item[3:5]
    if AP_iter == -1 and RRR_iter == -1:
        ax.scatter(n, r, q, c='black', marker='x')
    elif AP_iter == 1 and RRR_iter == 1:
        ax.scatter(n, r, q, c='green', marker='o')
    elif AP_iter == -1:
        ax.scatter(n, r, q, c='orange', marker='o')
    elif RRR_iter == -1:
        ax.scatter(n, r, q, c='blue', marker='o')

# Show the legend
ax.legend()

# Show the plot
plt.show()
