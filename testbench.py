'''A testbench / playground to test automata and any analytic tools to report
   automata behavior.'''

# Written by: Steven Porretta.

import learning_automata as la
# import analyse_LA as ala

# Define the initial Tsetlin machine described in Q1 of the assignment.
# Instead of changing c1 in the LA, it will be modified throught the test
# bench, and analytics will be run on it using scipy.

# # The Tsetlin automaton is now working.  This test is no longer needed.

# tsetlin_6_2 = la.Tsetlin(3, 2, [0.5, 0.5])

# print("state prior to transition is: " + str(tsetlin_6_2.current_state))

# # a better test...

# for i in range(100):

#     tsetlin_6_2.environment_response()

#     print("state after to transition is: " + str(tsetlin_6_2.current_state))
#
# # End Tsetlin state translation test.

# # Krylov state translation test.
# krylov = la.Krylov(3, 2, [0.4, 0.5])

# print("state prior to transition is: " + str(krylov.current_state))

# # force a penalty...
# krylov.environment_response()

# print("state after to transition is: " + str(krylov.current_state))

# krylov.environment_response()

# print("state after to transition is: " + str(krylov.current_state))

# krylov.environment_response()

# print("state after to transition is: " + str(krylov.current_state))
# # End Krylov state transition test.

lri = la.Linear(1, [0.5, 0.5], [0.4, 0.6], 20)
kry = la.Krylov(18, 2, [0.05, 0.7])
tset = la.Tsetlin(18, 2, [0.05 / 2, 0.7 / 2])
tset.simulate(10, 500)
print(tset.ensemble_average)
kry.simulate(10, 500)
print(kry.ensemble_average)
print(len(kry.ensemble_average))
