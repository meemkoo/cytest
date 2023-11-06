from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name='cytest',
    version='0.0.1',
    install_requires=[],
    packages=find_packages(
        where='.',
        include=['src'],
        exclude=['tests', 'buildcyth']
    ),
    # ext_modules=cythonize("main.pyx"),
    entry_points={
        'console_scripts': [
            'cytest = src:EP',
        ]
    }
)