# Install poetry
install_poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Run pytest
test:
	poetry run pytest tests

# Install pyenv
install_pyenv:
	sudo apt -y update
	sudo apt -y upgrade
	git clone https://github.com/pyenv/pyenv.git ~/.pyenv
	echo 'eval "$(pyenv init -)"' >> ~/.bashrc
	source ~/.bashrc