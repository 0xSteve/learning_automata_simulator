'''A testbench / playground to test automata and any analytic tools to report
   automata behavior.'''

# Written by: Steven Porretta.

import learning_automata as la
import analyse_LA as ala

c2 = 0.7
c1 = 0.05

# for i in range(0, 7):
#     print("c1 = " + str(c1) + ", c2 = " + str(c2) + ", N = 13.")
#     a = la.Tsetlin(13, 2, [c1, c2])
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
lri = la.Linear([0.5, 0.5], [c1, c2], 0.1)
lri.simulate(1)
