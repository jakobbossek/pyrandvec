# clean-up
clean:
	rm -rfv build dist randvec.egg-info \_\_pycache\_\_

# clean-up cache (TODO: does not work yet)
clean-pycache:
	find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

upgrade:
	# Make sure you have the latest version of PyPA’s build installed
	python -m pip install --user --upgrade setuptools wheel
	python -m pip install --upgrade build
	python -m pip install --upgrade twine

# source distribution
build:
	python -m build

# upload to TestPyPi (see ~/.pypirc for token)
testpypi-upload:
	python -m twine upload --repository testpypi dist/*

testpypi-web:
	open https://test.pypi.org/project/randvec

# install TestPyPi version
testpypi-install:
	python -m pip install --index-url https://test.pypi.org/simple/ --no-deps pyrandvec

# upload to PyPi (see ~/.pypirc for token)
pypi-upload:
	python -m twine upload dist/*

pypi-web:
	open https://pypi.org/project/randvec

# install PyPi version
pypi-install:
	python -m pip install pyrandvec

install-local:
	pip install --editable .

test:
	pytest -v

flake8:
	flake8

conda:
	conda env create -f environment.yml
	conda activate pyrandvec
