import matplotlib.pyplot as plt
from randvec.methods import sample

# parameters
n, d = 1000, 3

# plot
fig = plt.figure()

methods = ["normalisation", "iterative", "exponential", "simplex", "trigonometric"]
k = 1
for i, method in enumerate(methods):
    for j, shuffle in enumerate([True, False]):
        vecs = list(sample(n, d, method = method, shuffle = shuffle))
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
