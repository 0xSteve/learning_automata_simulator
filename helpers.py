'''Some helper functions.'''


def make_p(count):
    '''A helper function that generates count based on the number of
    actions.'''
    a = []
    for i in range(count):
        a.append(1 / count)
    return a


def make_c(count):
    # I might need this, who knows?
    pass


def cdf(p_vector):
    '''get the cumulative distribution vector for a given input vector.'''
    cdf = []
    sigma = 0
    for i in range(len(p_vector)):
        sigma += p_vector[i]
        cdf.append(sigma)
    return cdf
