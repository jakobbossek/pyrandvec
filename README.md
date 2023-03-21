# Random Probability Vectors

This python3 module implements a method 'rpv' which allow to generate d-dimensional probability vectors where the sum of the components adds up to one. The function offers different methods as discussed in [1].

[1] Maziero, J. Generating Pseudo-Random Discrete Probability Distributions. Brazilian Journal of Physics 45, 377–382 (2015). https://doi.org/10.1007/s13538-015-0337-8


## Installation

Run the following to install the module:

```bash
$ pip install pyrpv
```

## Usage

```python
from pyrpv import rpv

# Generate 10 4-dimensional vectors with the simplex-method
rpv(10, 4, method = "simplex")

# Generate 10 3-dimensional vectors with the trigonometric methdod with subsequent shuffling
rpv(10, 3, method = "trigonometric", shuffle = True)
```

# Developing pyrpv

To install the **pyrpv** module along with the tools you need to develop and run test, run the following command in your *virtual environment* (virtualenv):

```bash
$ pip install -e .[dev]
```

