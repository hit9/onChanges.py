from setuptools import setup
from onChanges import __version__


setup(
    name='onChanges',
    version=__version__,
    author='hit9',
    author_email='nz2324@126.com',
    description=(
        'Watch given files and run certain command on changes.'
    ),
    license='BSD',
    url='https://github.com/hit9/onChanges.py',
    install_requires = ['docopt'],
    scripts=['onChanges']
)
