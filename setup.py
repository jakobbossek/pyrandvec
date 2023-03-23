import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "randvec",
    version = "1.0.2",
    author = "Jakob Bossek",
    author_email = "j.bossek@gmail.com",
    description = "Generate random and uniform vectors whose components sum up to one",
    long_description = long_description,
    url = "https://github.com/jakobbossek/randvec/",
    # tell PyPi that we use markdown and not RestructuredText
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(exclude = ["tests"]),
    python_requires = '>=3.7',
    py_modules = ["randvec"],
    package_dir = {},
    # make it easy for users to find the package
    # (see https://pypi.org/classifiers/)
    classifiers = [
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    # for production dependencies
    install_requires = [],
    # for optional (development) requirements
    extras_require = {
        "dev": [
            "pytest >=3.7",
        ]
    },
)
