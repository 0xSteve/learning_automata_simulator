'''Learning_automata.py is a module containing some learning automata.'''

# Written by: Steven Porretta.

# For now it only contains a Tsetlin 2N,2 automaton.

from random import uniform

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
        '''set up states, penalties, etc.'''
        pass

    def next_state_on_reward(self):
        '''define the state translation, or action selection,
           on reward.'''
        pass

    def next_state_on_penalty(self):
        '''define the state translation, or action selection,
           on penalty.'''
        pass

    def environment_response(self):
        '''determine the reward, and then call for the appropriate
           response.'''
        pass


class Tsetlin(LA):
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
        penalty_index = self.N % self. R
        # print("The penalty index is: " + str(penalty_index) +
        #       " and the penalty is: " + str(self.c[penalty_index]))

        if(response > self.c[penalty_index]):
            # Reward.
            self.next_state_on_reward()
        else:
            # Penalty.
            self.next_state_on_penalty()

    # Run a simulation of a Tsetlin automaton.
    # It might be best to put this function somewhere else...
    def simulate(self, n, ensemble_size):
        '''Run a simulation of a Tsetlin automaton for a size of
           experiment, n, and a number of experiments, ensemble_size.'''
        for i in range(n):
            for j in range(ensemble_size):
                self.environment_response()


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


class Linear(LA):
    '''The Linear Reward-Inaction model (for now).'''

    # the init needs the initial probability vector.
    # for the sake of simplicity, assume only 2 actions, but parameterize
    # for more.
    # Need a meaningful value for a.  Have to check the books for that.

    def __init__(self, a, p, c):
        '''p and c are vector quantities.'''
        pass

    def next_state_on_penalty(self):
        '''Do nothing, for now...'''
        pass

    def next_state_on_reward(self):
        '''increase probabilities by a factor of a.'''
        pass

    # Not sure exactly what to do with this.  Need to do a little more
    # reading to fully comprehend state translations.
    def environment_response(self):
        '''Determine the next state of the learner from the perspective
        of the teacher.'''
        response = uniform(0, 1)
        # The penalty index is the index of the penalty array.
        # penalty_index = self.N % self. R

        if(response > self.c[0]):  # penalty_index]):
            # Reward.
            self.next_state_on_reward()
        else:
            # Penalty.
            self.next_state_on_penalty()
