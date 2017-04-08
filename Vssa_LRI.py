'''Linear Reward-Inaction Variable Structure Stochastic Automaton.'''
from random import uniform
import helpers as h
import numpy as np

# ToDo: Make R action.


class Linear_R(object):
    '''The Linear Reward-Inaction model (for now).'''

    def __init__(self, c_nparray):
        '''Create a new Linear Reward-Inaction object.'''
        self.p = np.array(h.make_p(len(c_nparray)))
        self.c = c_nparray
        self.a = 0  # gi = a * pi
        self.n = 0

    def next_action(self):
        randy = uniform(0, 1)  # Throwback to Archer.
        index = 0  # Worst case select the first action.
        # print("The p is: " + str(self.p))
        cdf = h.cdf(self.p)
        # print("The cdf is: " + str(cdf))
        for i in range(len(self.p)):
            # Not actually looking for p looking for the CDF.
            if(randy < cdf[i]):
                index = i
                break
        return index

    def environment_response(self, action):
        rando = uniform(0, 1)
        penalty = self.c[action]
        return int(rando < penalty)

    def do_reward(self, action):
        self.p[action] += self.a * (1 - self.p[action])
        for i in range(len(self.p)):
            if(i != action):
                # print("i = " + str(i) + ". P = " + str(self.p))
                self.p[i] = (1 - self.a) * self.p[i]

    def do_penalty(self):
        pass

    def simulate(self, a):
        act = np.zeros(len(self.c))
        action = 0
        self.p = np.array(h.make_p(len(self.c)))
        self.a = a
        self.n = 0
        while(True):
            if(max(self.p) > 0.98 or min(self.p) < 0.02):
                # Close enough to 1.
                # Treat as convergence.
                break
            action = self.next_action()
            act[action] += 1
            # print("The next action is: " + str(action + 1))
            b = self.environment_response(action)
            if(b == 0):
                # Reward.
                self.do_reward(action)
            self.n += 1
        # Return the action average.
        return round(act[1] / sum(act), 0)

    def find_accuracy(self, ensemble_size, a):

        ensemble_average = 0

        for i in range(0, ensemble_size):
            ensemble_average += self.simulate(a)
            self.n += 1

        ensemble_average = ensemble_average / ensemble_size

        return ensemble_average

    def find_optimal_a(self, ensemble_size, low=1, high=5,
                       desired_accuracy=0.95):
        L = low
        H = high

        while(self.percent_diff(L, H) >= 0.05):
            a_mid = (L + H) / 2
            accuracy = self.find_accuracy(ensemble_size, a_mid)
            if(accuracy >= desired_accuracy):
                H = a_mid
            else:
                L = a_mid
        return H

    def percent_diff(self, value1, value2):
        return abs(value1 - value2) / ((value1 + value2) / 2)
