'''Testbench for the new LRI R-action automaton.'''
import Vssa_LRI as vssa
import numpy as np

c = np.array([0.1, 0.25, 0.4, 0.44])
print("===========================================================================================================================================")
print("===========================================================================================================================================")
lri = vssa.Linear_R(c)
print("The probability of next action is: " + str(lri.p))
# Test the next action function
# for i in range(10):
# print("The next action is: " + str(lri.next_action()))
# print("The environment response is: " + str(lri.environment_response(1)))
# print("The next action is: " + str(lri.do_reward(1)) +
#       ". The probability vector is: " + str(lri.p))
a = lri.find_optimal_a(100)
print("The optimal a is: " + str(a))
print("P(inf) = " + str(lri.p))
