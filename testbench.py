'''A testbench / playground to test automata and any analytic tools to report
   automata behavior.'''

# Written by: Steven Porretta.

import learning_automata as la

c2 = 0.7
c1 = 0.05
for i in range(0, 7):
    lri = la.Linear(c1, 0.7)
    a = lri.find_optimal_kr(1000)
    b = lri.find_accuracy(1000, a)
    print("=============================================================")
    print("The optimal K_r value is: " + str(a))
    print("The optimal lambda_r value is: " + str(1 - a))
    print("The accuracy for k_r = " + str(a) + " is: " + str(b))
    print("The computation time in iterations is: " + str(lri.n))
    print("=============================================================")
    c1 += 0.1
    c1 = round(c1, 2)
