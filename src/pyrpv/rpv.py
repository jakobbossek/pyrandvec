import random
import math
import matplotlib.pyplot as plt


def rpv(n: int, d: int, method: str = "normalisation", shuffle: bool = False) -> list[list[float]]:
    '''
    Generates a list of random probability vectors (rpv) with different methods.

    Args:
        n (int): desired number of vectors.
        d (int): dimension.
        method (str): desired method (see rpv_* functions in this module).
        shuffle (bool): shall each rpv be randomly shuffled? Default is False.
    Returns:
        List of length n of d-dimensional lists.
    '''
    assert n >= 1
    assert d >= 2

    funs = {
        'normalisation': rpv_normalisation,
        'exponential': rpv_exponential,
        'iterative': rpv_iterative,
        'trigonometric': rpv_trigonometric,
        'simplex': rpv_simplex
    }
    assert method in funs.keys()

    fun = funs[method]
    vecs = fun(n, d)

    if not shuffle:
        return vecs

    return list(map(lambda e: random.sample(e, k = len(e)), vecs))


def normalise(x: list[float]) -> list[float]:
    '''
    Utility function to normalise a list of floating point numbers.
    I.e., the function divides each component of the list by its sum.

    Args:
        x (list[float]): Input list.
    Returns:
        Normalised list.
    '''
    return list(map(lambda e: e / sum(x), x))


def rpv_normalisation(n: int, d: int) -> list[list[float]]:
    '''
    Generates a list of random probability vectors (rpv) via normalisation.
    I.e., (1) each component is sampled from a U(0,1) distribution and subsequently
    (2) each component is divided by the components' sum.

    Args:
        n (int): desired number of vectors.
        d (int): dimension.
    Returns:
        List of length n of d-dimensional lists.
    '''
    assert n >= 1
    assert d >= 2

    # TODO: ugly as hell and not 'Pythonesque' at all
    vecs = [None] * n
    for i in range(n):
        vec = [random.random() for _ in range(d)]
        vecs[i] = normalise(vec)

    return vecs


def rpv_iterative(n: int, d: int) -> list[list[float]]:
    '''
    Generates a list of random probability vectors (rpv) via an iterative approach:
    I.e., the i-th component of the rpv is sampled uniformly at random from [0, s] where s is
    the sum of the 0, ..., (i-1)st components. The last component is finally (1-s). This
    way it is unsured that the vectors are normalised.

    Args:
        n (int): desired number of vectors.
        d (int): dimension.
    Returns:
        List of length n of d-dimensional lists.
    '''
    assert n >= 1
    assert d >= 2

    def sample_rpv_iterative(d):
        s = 0.0
        vec = [None] * d
        for j in range(d - 1):
            vec[j] = random.uniform(0, 1 - s)
            s += vec[j]
        vec[d - 1] = 1 - s
        return vec

    vecs = [sample_rpv_iterative(d) for _ in range(n)]
    return list(vecs)


def rpv_trigonometric(n: int, d: int) -> list[list[float]]:
    '''
    Generates a list of random probability vectors (rpv) via a trigonometric method.
    Section 5 in the following paper contains the details: Maziero, J. Generating Pseudo-Random
    Discrete Probability Distributions. Brazilian Journal of Physics 45, 377–382 (2015).
    https://doi.org/10.1007/s13538-015-0337-8)

    Args:
        n (int): desired number of vectors.
        d (int): dimension.
    Returns:
        List of length n of d-dimensional lists.
    '''
    assert n >= 1
    assert d >= 2

    def sample_rpv_trigonometric(d):
        ts = [random.random() for _ in range(d - 1)]

        # build vector of weights
        thetas = [None] * d
        thetas[0] = 3.1415 / 2  # pi/2
        for j in range(d - 1, 0, -1):
            thetas[j] = math.acos(math.sqrt(ts[j - 1]))

        # build the pRPV
        vec = [None] * d
        for j in range(d - 1, -1, -1):
            r = math.sin(thetas[j]) * math.sin(thetas[j])
            for k in range(j + 1, d):
                r = r * math.cos(thetas[k]) * math.cos(thetas[k])
            vec[j] = r

        return vec

    return [sample_rpv_trigonometric(d) for _ in range(n)]


def rpv_exponential(n: int, d: int) -> list[list[float]]:
    '''
    Generates a list of random probability vectors (rpv) by means of the inverse
    exponential distribution function: I.e., the i-th component of the rpv is sampled
    uniformly at random from [0, s] where s is the sum of the 0, ..., (i-1)st
    components. The last component is finally (1-s). This way it is unsured that
    the vectors are normalised.

    Args:
        n (int): desired number of vectors.
        d (int): dimension.
    Returns:
        List of length n of d-dimensional lists.
    '''
    assert n >= 1
    assert d >= 2

    vecs = []
    for i in range(n):
        vec = [(-1) * math.log(1 - random.random()) for _ in range(d)]
        vecs.append(normalise(vec))

    return vecs


def rpv_simplex(n: int, d: int) -> list[list[float]]:
    '''
    Generates a list of random probability vectors (rpv) via simplex sampling.

    See [1] for details on this method.

    [1] Grimme, C. Picking a Uniformly Random Point from an Arbitrary Simplex.
    Technical Report. https://doi.org/10.13140/RG.2.1.3807.6968

    Args:
        n (int): desired number of vectors.
        d (int): dimension.
    Returns:
        List of length n of d-dimensional lists.
    '''
    assert n >= 1
    assert d >= 2

    def sample_vector_from_unit_simplex(d):
        unifs = [random.random() for _ in range(d - 1)]
        unifs = sorted(unifs)

        unifs2 = [0] * (d + 1)
        for i in range(d - 1):
            unifs2[i + 1] = unifs[i]
        unifs2[d] = 1

        vec = (unifs2[i] - unifs2[i - 1] for i in range(1, d + 1))
        return vec

    vecs = [list(sample_vector_from_unit_simplex(d)) for _ in range(n)]
    return vecs


if __name__ == "__main__":
    # parameters
    n, d = 1000, 3

    # plot
    fig = plt.figure()

    methods = ["normalisation", "iterative", "exponential", "simplex", "trigonometric"]
    k = 1
    for i, method in enumerate(methods):
        for j, shuffle in enumerate([True, False]):
            vecs = list(rpv(n, d, method = method, shuffle = shuffle))
            # print(list(vecs))
            ss = map(sum, vecs)
            # print(list(ss))

            sp = fig.add_subplot(1, 2 * len(methods), k, projection = '3d')
            k += 1

            xs = [x[0] for x in vecs]
            ys = [x[1] for x in vecs]
            zs = [x[2] for x in vecs]

            sp.set_xlabel('x')
            sp.set_ylabel('y')
            sp.set_zlabel('z')
            title = method
            if shuffle:
                title += " (shuffled)"
            sp.set_title(title)
            sp.scatter(xs, ys, zs, marker = 'o')

    plt.show()
