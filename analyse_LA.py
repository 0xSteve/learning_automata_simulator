'''a module containing analytic tools necessary for understanding the
   behavior of learning automata.'''

# Written by Steven Porretta.


class Tsetlin(object):
    '''Analysis tools for the Tsetlin automaton.'''
    def stationary_probability(self, is_analytic):
        probability = 0
        if(is_analytic):
            probability = self.stationary_probability_analytic()
        else:
            probability = self.stationary_probability_estimate()

        return probability

    def stationary_probability_analytic(self):
        pass

    def stationary_probability_estimate(self):
        pass
