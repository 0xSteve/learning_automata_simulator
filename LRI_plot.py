'''A version of the testbench.py file that produces plots for
   the LRI automata'''

# Written by: Steven Porretta

import learning_automata as la
import numpy as np
import matplotlib.pyplot as plt
import argparse

c1 = 0.05
lambda_r = []
n = []
for i in range(0, 7):
    lri = la.Linear(c1, 0.7)
    a = lri.find_optimal_kr(1000)
    #  b = lri.find_accuracy(1000, a)
    lambda_r.append(1-a)
    n.append(lri.n)
    print("=============================================================")
    print("The optimal K_r value is: " + str(a))
    print("The optimal lambda_r value is: " + str(1 - a))
    #  print("The accuracy for k_r = " + str(a) + " is: " + str(b))
    print("The computation time in iterations is: " + str(lri.n))
    print("=============================================================")
    c1 += 0.1
    c1 = round(c1, 2)

parser = argparse.ArgumentParser(usage=__doc__)
parser.add_argument("--output", default="plot.png", help="output image file")
args = parser.parse_args()
n = np.array(n)
print(n)
print(lambda_r)
lambda_r = np.array(lambda_r)
plt.plot(n, lambda_r)
plt.savefig(args.output, dpi=96)
