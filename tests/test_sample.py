import itertools
from randvec.methods import sample


def test_that_rpvs_sum_up_to_one():
    n = 5
    ds = [2, 4]
    methods = ["normalisation", "iterative", "exponential", "simplex", "trigonometric"]
    shuffling = [True, False]

    for d, method, shuffle in list(itertools.product(ds, methods, shuffling)):
        vecs = list(sample(n, d, method = method, shuffle = shuffle))
        assert all([(sum(vec) - 1) < 0.00000001 for vec in vecs])
