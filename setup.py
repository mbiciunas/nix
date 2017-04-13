# Nix
# Copyright (c) 2017  Mark Biciunas.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup
from setuptools import find_packages
import shutil

shutil.rmtree("build", ignore_errors=True)
shutil.rmtree("dist", ignore_errors=True)
shutil.rmtree("egg-info", ignore_errors=True)

setup(
    name='nix',
    version='0.2.0',
    package_dir={'': 'src'},
    packages=find_packages("src"),
    install_requires=['pytest', ],
    url='',
    license='GPLv3',
    author='Mark Biciunas',
    author_email='mbiciunas@gmail.com',
    description='Nix management system for Linux.',
    entry_points={
        'console_scripts': ['nix = nix:main',
                            'nixconfig = nixconfig:main', ],
    },


)
