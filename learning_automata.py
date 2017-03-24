'''Learning_automata.py is a module containing some learning automata.'''

# Written by: Steven Porretta.

# For now it only contains a Tsetlin 2N,2 automaton.

from random import uniform
import numpy as np

# Write a Tsetlin automaton.
# A Tsetlin automaton is defined by N memory states, R actions,
# and c penalties.
#
# N is expected to be a whole number indicating memory depth.
# R is expected to be a while number indicating the number of,
# actions.
# c is a vector quantity indicating the penalties for actions
# 1 to i.

# There should be an abstract class that defines the important parameters
# of a learning automaton, shared by all learning automata.


class LA(object):
    '''A learning automaton.'''

    def __init__(self):
        '''Set up states, penalties, etc.'''
        pass

    def next_state_on_reward(self):
        '''Define the state translation, or action selection,
           on reward.'''
        pass

    def next_state_on_penalty(self):
        '''Define the state translation, or action selection,
           on penalty.'''
        pass

    def environment_response(self):
        '''Determine the reward, and then call for the appropriate
           response.'''
        pass

    def simulate(self):
        '''Define the simulation for the automaton.'''
        pass


class Tsetlin(LA):
    '''Tsetlin automata. N, R positive integers. c a structure
       of penalties from action 1 to action i. First state starts at 1 not
       0.'''

    def __init__(self, N, R, c):
        '''initialize a Tsetlin automaton with N memory states,
           R actions, and c penalty probabilities for each R.'''
        self.N = 2 * N
        self.n = N
        self.R = R
        self.c = c
        # define the initial state as the state leaning toward action one.
        self.current_state = int(self.N / R)
        self.states = []
        self.actions = np.zeros(self.R)
        self.action_average = 0

    # Find the next state given that the teacher rewarded.
    def next_state_on_reward(self):
        '''Find the next state of the learner, given that the teacher
           rewarded.'''

        # I need to know what state is the next loopback state.
        # There are R actions, and therefore there are 2N/R memory blocks.
        # If the current state is <= 2N/R in action 1
        # If 2N/R < current state < 2(2N/R) in action 2

        # If the mod is 1, then the current state is the loopback state.
        if (self.current_state % (self.N / self.R) != 1):
            self.current_state -= 1

    # Find the next state given that the teacher penalized.
    def next_state_on_penalty(self):
        '''Find the next state of the learner, given that the teacher
           penalized.'''

        # The hard part here is not looping back, but instead jumping to
        # the next 2N / R state.

        if(self.current_state % (self.N / self.R) != 0):
            self.current_state += 1
        elif(self.current_state % (self.N / self.R) == 0):
            # Don't really add states, just cycle through N, 2N, 4N, etc.
            if(self.current_state != self.N):
                a = (self.N / self.R) % self.N
                self.current_state = a + self.current_state
            else:
                self.current_state = self.N / self.R

    # Determine the next state as the teacher.
    def environment_response(self):
        '''Determine the next state of the learner from the perspective
        of the teacher.'''
        response = uniform(0, 1)
        # The penality index is the index of the penalty array.
        # Do 2 action for now
        penalty_index = 1
        if(self.current_state <= self.n):
            self.actions[0] += 1
            penalty_index = 0
        else:
            self.actions[1] += 1

        if(response > self.c[penalty_index]):
            # Reward.
            self.next_state_on_reward()
        else:
            # Penalty.
            self.next_state_on_penalty()

    # for action counting pretend it is always 2 action for now.
    def action_count(self):
        if(self.current_state <= self.n):
            # In action 1.
            self.actions[0] += 1
        else:
            self.actions[1] += 1

    # Run a simulation of a Tsetlin automaton.
    # It might be best to put this function somewhere else...
    def simulate(self, n, ensemble_size):
        '''Run a simulation of a Tsetlin automaton for a size of
           experiment, n, and a number of experiments, ensemble_size.'''

        for i in range(ensemble_size):
            self.states.append(np.zeros(self.N))
            for j in range(n):
                self.environment_response()

        self.action_average = self.actions / (n * ensemble_size)


class Krylov(Tsetlin):
    '''Krylov automaton.  Inherits from the Tsetlin automaton.'''

    def __init__(self, N, R, c):
        '''The constructor of a Krylov is exactly the same as the Tsetlin.
           The only difference between the machines is how penalties are
           handled.'''

        Tsetlin.__init__(self, N, R, c)

    def next_state_on_penalty(self):
        '''Find the next state of the learner, given that the teacher
           penalized.'''

        # If this number is greater than 0.5, then penalize the learner.
        is_penalty = uniform(0, 1)

        if(is_penalty >= 0.5):
            Tsetlin.next_state_on_penalty(self)
        else:
            Tsetlin.next_state_on_reward(self)


class Linear(object):
    '''The Linear Reward-Inaction model (for now).'''

    # This time separate all concerns, no vectors.
    def __init__(self, c1, c2):
        self.c1 = c1
        self.p1 = 0.5  # Always start in the 0.5 state at the beginning.
        self.c2 = c2
        self.p2 = 0.5  # Always start in the 0.5 state at the beginning.
        self.k_r = 0  # k_r = 1 - lambdaR

    def next_action(self):
        randy = uniform(0, 1)  # Throwback to Archer.
        if(randy < self.p1):
            # Choose action 1.
            return 1
        return 2

    def environment_response(self):
        # For now let's always give a reward.
        return 0

    def do_reward(self, action):
        if(action == 2):
            self.p1 = self.k * self.p1
        else:
            self.p1 = (1 - self.k) * self.p2
        self.p2 = 1 - self.p1

    def do_penalty(self):
        pass

    def simulate(self):
        a1_counter = 0
        a2_counter = 0

        while(True):
            if(self.p1 or self.p2 > 0.4):
                # Close enough to 1.
                # Treat as convergence.
                break
            if(self.next_action() == 1):
                # Do action 1
            else:
                # Do action 2
        return 0  # Return the action average.
