'''A testbench / playground to test automata and any analytic tools to report
   automata behavior.'''

# Written by: Steven Porretta.

import learning_automata as la
import analyse_LA as ala

c2 = 0.7
c1 = 0.05

# for i in range(0, 7):
#     print("c1 = " + str(c1) + ", c2 = " + str(c2) + ", N = 13.")
#     a = la.Tsetlin(13, 2, [c1 / 2, c2 / 2])
#     a.simulate(50, 30001)
#     b = ala.Tsetlin.stationary_probability_analytic([c1, c2], 13)
#     c = ala.Tsetlin.number_of_states_estimate([c1, c2])
#     d = la.Krylov(13, 2, [c1, c2])
#     d.simulate(10, 50000)
#     e = ala.Tsetlin.stationary_probability_analytic([c1, c2], 13)
#     f = ala.Tsetlin.number_of_states_estimate([c1, c2])
#     print("Tsetlin P1(infinity) = " + str(b) + "(Analytic)")
#     print("Tsetlin P1(infinity) = " + str(a.action_average[0]) + "(Simulated)")
#     print("Tsetlin # of states required = " + str(c) + "(Estimate)")
#     print("Krylov P1(infinity) = " + str(e) + "(Analytic)")
#     print("Krylov P1(infinity) = " + str(d.action_average[0]) + "(Simulated)")
#     print("Krylov # of states required = " + str(f) + "(Estimate)")
#     c1 += 0.1
#     c1 = round(c1, 2)

# for i in range(0, 7):
#     lri = la.Linear([0.5, 0.5], [c1, c2], 0.1)
#     best = lri.find_best_lambda()
#     print("c1 = " + str(c1) + " c2 = " + str(c2))
#     print("Best lambda approaches: " + str(best))
#     print("Mean time to converge in steps = " + str(lri.n))
#     c1 += 0.1
#     c1 = round(c1, 2)
lri = la.Linear(0.05, 0.7)
k = 0.00
for i in range(1, 100):
    k += 0.01
    ave = lri.find_ensemble_average(1000, k)
    # b = lri.environment_response(1)
    print("Converges to correct action: " + str(ave))
    print("k = " + str(k) + " iteration number: " + str(i))
    # print("The response is: " + str(b))
    print("=========================================")

# # lri = la.Linear([0.5, 0.5], [c1, c2], 0.2)
# # lri.simulate(1)
# # print("=========================================")
# # lri = la.Linear([0.5, 0.5], [c1, c2], 0.3)
# # lri.simulate(1)
# # print("=========================================")
# # lri = la.Linear([0.5, 0.5], [c1, c2], 0.4)
# # lri.simulate(1)
# # print("=========================================")
# # lri = la.Linear([0.5, 0.5], [c1, c2], 0.5)
# # lri.simulate(1)
# # print("=========================================")
# # lri = la.Linear([0.5, 0.5], [c1, c2], 0.6)
# # lri.simulate(1)
# best = lri.find_best_lambda()
# print("Lambda R converges to: " + str(best))
