'''Learning_automata.py is a module containing some learning automata.'''

# Written by: Steven Porretta.

# For now it only contains a Tsetlin 2N,2 automaton.

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
       of penalties from action 1 to action i.'''

    def __init__(self, N, R, c):
        '''initialize a Tsetlin automaton with N memory states,
           R actions, and c penalty probabilities for each R.'''
        self.N = 2 * N
        self.R = R
        self.c = c
        # define the initial state as the state leaning toward action one.
        self.current_state = self.N / 2

    # Find the next state given that the teacher rewarded.
    def next_state_on_reward(self):
        '''Find the next state of the learner, given that the teacher
           rewarded.'''
        pass

    # Find the next state given that the teacher penalized.
    def next_state_on_penalty(self):
        '''Find the next state of the learner, given that the teacher
           penalized.'''
        pass

    # Determine the next state as the teacher.
    def environment_response(self):
        '''Determine the next state of the learner from the perspective
        of the teacher.'''
        pass
