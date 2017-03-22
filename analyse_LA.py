'''a module containing analytic tools necessary for understanding the
   behavior of learning automata.'''

# Written by Steven Porretta.


class Tsetlin(object):
    '''Analysis tools for the Tsetlin automaton.'''

    def stationary_probability(self, is_analytic, c):
        '''This only assumes reasonable functionality for a two action
           automaton, due to time constraints.'''

        probability = 0
        if(is_analytic):
            probability = self.stationary_probability_analytic()
        else:
            probability = self.stationary_probability_estimate()

        return probability

    def stationary_probability_analytic(self, c, N):
        '''This computes the exact stationary probability, iff the
           automaton is 2 action.  Since the requirement is only for p1
           at infinity, then p2 is discarded, due to time constraints.'''
        N = N / 2  # Assume that N has been doubled to 2N.
        d1 = 1 - c[0]
        d2 = 1 - c[1]
        term1 = pow(c[0] / c[1], N) * ((c[0] * d1) / (c[1] * d2))
        term2 = (pow(c[0], N) - pow(d1, N)) / (pow(c[1], N) - pow(d2, N))
        p1_inf = 1 / [1 + term1 * term2]

        return p1_inf

    def has_accuracy(self, desired_accuracy, current_probability):
        '''Return true, if the probability vector is within the desired
           accuracy parameter.'''
        desired_percent_diff = 1 - desired_accuracy
        # Need to know the desired probability limit to determine the accuracy.
        probability = self.stationary_probability_analytic(self.c, self.N)
        denom = (probability + current_probability) / 2
        percent_diff = abs(probability - current_probability) / denom
        if(percent_diff <= desired_percent_diff):
            return True

        return False

    def stationary_probability_estimate(self, c, desired_accuracy=0.95):
        '''Find the probability of selecting the mininum penalties for a 2
           action automaton with a desired accuracy. (95% by default)'''

        # Need range betwee 0, 1. Accuracy is in {0, 1}.
        low = 0
        high = 1
        mid = 0

        computed_probability = 0

        while(True):
            mid = (low + high) / 2
            a = self.stationary_probability_analytic(self.c, mid)
            computed_probability = a
            if(self.has_accuracy(desired_accuracy, computed_probability)):
                return mid
