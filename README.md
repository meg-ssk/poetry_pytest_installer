# poetry_pytest_installer

I have prepared a Makefile for easy installation of poetry to ease the creation of a Python development and testing environment.

I hope this will help you as you build your development and testing environment.

The appeal points are listed below.

- We can easily install `poetry`, which is useful tool for Python packages and dependencies management. It can be installed with just one simple command.
- A test environment with `pytest` can also be built with a single command.
- The functions for basic arithmetic operations and their unit tests are prepared as simple examples.

## Installation

### poetry
`poetry` is very useful tool for Python packages and dependencies management.

We can install `poetry` by:
```
make install_poetry
```

### pytest
We can install various Python packages by:
```
poetry install
``` 
The files in this repository make it easy to install `pytest` with just this one command.

### other packages
If you would like to install other package,
run the following command.
```
poetry add package_name (e.g. numpy)
```

## Unit test
We can run unit tests by the following command:
```
make test
```

## Usage of sample code for basic arithmetic operation
The four calculations results can be obtained with the following commands:
```
poetry run python src/main.py ${val1} ${val2}
```

Try entering any real values for `${val1}` and `${val2}`.

```
% poetry run python src/main.py 1 2
add: 3.0
sub: -1.0
mul: 2.0
dev: 0.5
```

If `${val2}` is zero, the following warning message for division by zero is shown.

```
% poetry run python src/main.py 1 0
add: 1.0
sub: 1.0
mul: 0.0
dev: Zero division is not possible.
```