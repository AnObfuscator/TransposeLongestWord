#!/usr/bin/env python
import setuptools


with open('README.md', 'r') as r_file:
    LDINFO = r_file.read()

VERSION = "1.0.0"

INSTALL_REQUIRES = [
]

DEPENDENCY_LINKS = [
]

ENTRY_POINTS = {
    "console_scripts": [
        "tlp-cli = transpose_longest_word.main:main",
    ]
}

setuptools.setup(
    name="TransposeLongestWord",
    version=VERSION,
    author="Jonathan Evans",
    author_email="jonathan.evans@multifariam.net",
    description="A tool to extract and transpose the longest word from a file",
    long_description=LDINFO,
    packages=setuptools.find_packages(exclude=["test"]),
    url="https://github.com/AnObfuscator/TransposeLongestWord",
    install_requires=INSTALL_REQUIRES,
    dependency_links=DEPENDENCY_LINKS,
    entry_points=ENTRY_POINTS,
    classifiers=[]
)
