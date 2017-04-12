'''Discretized Linear Reward-Inaction Variable Structure
   Stochastic Automaton.'''

# from random import uniform
# import helpers as h
import numpy as np

# In this case it is not possible to feed the penalty probability vector,
# c, as an input. For this, one will have to be a little bit more
# creative in the environmental response.


class dlri(object):

    def __init__(self, num_actions):
        '''Create a new discrete linear reward inaction automaton.'''
        # In this case we divide the interval [0,1] by the number of
        # actions in the DLRI automaton.
        self.p = np.zeros(num_actions)

    def do_reward(self, vars):
        pass

    def do_penalty(self, vars):
        pass

    def simulate(self, vars):
        pass

    def enemble_simulation(self, vars):
        pass