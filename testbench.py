'''A testbench / playground to test automata and any analytic tools to report
   automata behavior.'''

# Written by: Steven Porretta.

import learning_automata as la

# Define the initial Tsetlin machine described in Q1 of the assignment.
# Instead of changing c1 in the LA, it will be modified throught the test
# bench, and analytics will be run on it using scipy.
tsetlin_6_2 = la.Tsetlin(3, 2, [0.5, 0.5])

print("state prior to transition is: " + str(tsetlin_6_2.current_state))

# a better test...

for i in range(100):

    tsetlin_6_2.environment_response()

    print("state after to transition is: " + str(tsetlin_6_2.current_state))
