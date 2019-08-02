
# Introduction

This is a CLI that will return the transpose of the longest word in a list of words in a file. If multiple words are the same length, it will return the first word of the longest length.

This has been tested with Python 3.7 and Fedora 30.

## Installation

This can be installed from GitHub using:
```bash
pip install -e git+https://github.com/AnObfuscator/TransposeLongestWord.git#egg=TransposeLongestWord
```

## Usage
To run against an input file after installation, use:
```bash
tlw-cli path/to/input/file
```

For help, you can use:
```bash
tlw-cli -h
```

## Development

Clone this repo:

```bash
git clone git@github.com:AnObfuscator/TransposeLongestWord.git
```

Make a virtual environment in the repo directory and install 

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-devel.txt
python setup.py develop
```

You can run the tests with `tox`.
