'''a module containing analytic tools necessary for understanding the
   behavior of learning automata.'''

# Written by Steven Porretta.


class Tsetlin(object):
    '''Analysis tools for the Tsetlin automaton.'''

    def stationary_probability_analytic(c, N):
        '''This computes the exact stationary probability, iff the
           automaton is 2 action.  Since the requirement is only for p1
           at infinity, then p2 is discarded, due to time constraints.'''
        N = N / 2  # Assume that N has been doubled to 2N.
        d1 = 1 - c[0]
        d2 = 1 - c[1]
        term1 = pow((c[0] / c[1]), N) * ((c[0] - d1) / (c[1] - d2))
        numer = pow(c[1], N) - pow(d2, N)
        term2 = numer / (pow(c[0], N) - pow(d1, N))
        p1_inf = 1 / (1 + term1 * term2)

        return p1_inf

    def number_of_states_estimate(c, desired_accuracy=0.95):
        '''Find the probability of selecting the mininum penalties for a 2
           action automaton with a desired accuracy. (95% by default)'''

        # Need range between 0, 1. Accuracy is in {0, 1}.
        low = 0
        high = 100
        mid = int((low + high) / 2)
        mini = 0

        computed_accuracy = 0
        # Apparently, the internet knows all... googled binary search lel.
        while(low <= high):
            mid = int((low + high) / 2)
            a = Tsetlin.stationary_probability_analytic(c, mid)
            computed_accuracy = a
            if(computed_accuracy >= desired_accuracy):
                high = mid - 1
                mini = mid
            else:
                low = mid + 1
        return mini
