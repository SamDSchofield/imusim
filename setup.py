#!/usr/bin/env python
#
# Copyright (C) 2009-2011 University of Edinburgh
#
# This file is part of IMUSim.
#
# IMUSim is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IMUSim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with IMUSim.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

import numpy
cythonize("imusim/maths/*.pyx")
setup(
    name = "imusim",
    version = "0.2",
    author = "Alex Young and Martin Ling",
    license = "GPLv3",
    url = "http://www.imusim.org/",
    install_requires = ["simpy>=2.3,<3", "pyparsing", "scipy", "pylab-sdk", "requests"],
    packages = find_packages(),
    include_dirs = [numpy.get_include()],
    ext_modules = [
        Extension("imusim.maths.quaternions",
            ['imusim/maths/quaternions.c'], include_dirs=[numpy.get_include()]),
        Extension("imusim.maths.quat_splines",
            ['imusim/maths/quat_splines.c'], include_dirs=[numpy.get_include()]),
        Extension("imusim.maths.vectors",['imusim/maths/vectors.c'], include_dirs=[numpy.get_include()]),
        Extension("imusim.maths.natural_neighbour",[
            'imusim/maths/natural_neighbour/utils.c',
            'imusim/maths/natural_neighbour/delaunay.c',
            'imusim/maths/natural_neighbour/natural.c',
            'imusim/maths/natural_neighbour.c'], include_dirs=[numpy.get_include()])]
)
