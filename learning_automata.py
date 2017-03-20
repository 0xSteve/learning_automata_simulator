'''Learning_automata.py is a module containing some learning automata.'''

# Written by: Steven Porretta.

# For now it only contains a Tsetlin 2N,2 automaton.

from random import random

# Write a Tsetlin automaton.
# A Tsetlin automaton is defined by N memory states, R actions,
# and c penalties.
#
# N is expected to be a whole number indicating memory depth.
# R is expected to be a while number indicating the number of,
# actions.
# c is a vector quantity indicating the penalties for actions
# 1 to i.


class Tsetlin(object):
    '''Tsetlin automata. N, R positive integers. c a structure
       of penalties from action 1 to action i. First state starts at 1 not
       0.'''

    def __init__(self, N, R, c):
        '''initialize a Tsetlin automaton with N memory states,
           R actions, and c penalty probabilities for each R.'''
        self.N = 2 * N
        self.R = R
        self.c = c
        # define the initial state as the state leaning toward action one.
        self.current_state = self.N / R

    # Find the next state given that the teacher rewarded.
    def next_state_on_reward(self):
        '''Find the next state of the learner, given that the teacher
           rewarded.'''

        # I need to know what state is the next loopback state.
        # There are R actions, and therefore there are 2N/R memory blocks.
        # If the current state is <= 2N/R in action 1
        # if 2N/R < current state < 2(2N/R) in action 2

        if (self.current_state % (self.N / self.R) == 0):
            self.current_state -= self.N / self.R
        elif(self.current_state - (self.N / self.R) != 1):
            self.current_state -= 1

    # Find the next state given that the teacher penalized.
    def next_state_on_penalty(self):
        '''Find the next state of the learner, given that the teacher
           penalized.'''

        # The hard part here is not looping back, but instead jumping to
        # the next 2N / R state.
        print(self.N / self.R)
        print(self.current_state % (self.N / self.R))

        if(self.current_state % (self.N / self.R) != 0):
            self.current_state += 1
        else:
            self.current_state += self.N / self.R

    # Determine the next state as the teacher.
    def environment_response(self):
        '''Determine the next state of the learner from the perspective
        of the teacher.'''
        response = 0.04  # random()
        # The penality index is the index of the penalty array.
        penalty_index = self.N % self. R
        print("The penalty index is: " + str(penalty_index) +
              " and the penalty is: " + str(self.c[penalty_index]))

        if(response > self.c[penalty_index]):
            # Reward.
            print("Reward!")
            self.next_state_on_reward()
        else:
            # Penalty.
            print("Penalty!")
            self.next_state_on_penalty()

    # Run a simulation of a Tsetlin automaton.
    def simulate(self, n, ensemble_size):
        '''Run a simulation of a Tsetlin automaton for a size of
           experiment, n, and a number of experiments, ensemble_size.'''
        pass
