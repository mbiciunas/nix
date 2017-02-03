"""Setuptools configuration for nix.
"""

from setuptools import setup
from setuptools import find_packages
import shutil

shutil.rmtree("build", ignore_errors=True)
shutil.rmtree("dist", ignore_errors=True)
shutil.rmtree("egg-info", ignore_errors=True)

setup(
    name='nix',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages("src"),
    install_requires=['', ],
    url='',
    license='',
    author='Mark Biciunas',
    author_email='mbiciunas@gmail.com',
    description='Nix management system for Linux.',
    entry_points={
        'console_scripts': ['nix = nix:main', 'nixconfig = nixconfig:main', ]
    },
)
