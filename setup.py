from setuptools import setup, find_packages

setup(
    name='TASTEset',
    version='0.1',
    packages=find_packages(),
    # If you have dependencies, list them here
    install_requires=[
        'spacy',
    ],
)