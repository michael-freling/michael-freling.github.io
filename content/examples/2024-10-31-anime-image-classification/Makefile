.PHONY: setup
setup:
	python3 -m venv ./.venv
	source ./.venv/bin/activate
	pip install -r requirements.txt

# \
	# The Exempi is required to handle xmp files exported by DigiKam \
	# https://python-xmp-toolkit.readthedocs.io/en/latest/installation.html
	sudo apt install -y libexempi8

download:
	source ./.venv/bin/activate
	python scraper.py

compress:
	zip -r source.zip source

uncompress:
	unzip source.zip
