'''
setup.py - Python distutils setup file for GooMPy package.

Copyright (C) 2015 Alec Singer and Simon D. Levy
This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with this code.  If not, see <http://www.gnu.org/licenses/>.

Updated by Bruno Vermeulen @2019
'''

from distutils.core import setup

setup(
    name='GooMPy',
    version='0.1',
    install_requires=['PIL'],
    description='Google Maps for Python',
    packages=['goompy',],
    author='Alec Singer and Simon D. Levy',
    author_email='simon.d.levy@gmail.com',
    license='LGPL',
    platforms='Linux; Windows; OS X'
    )
