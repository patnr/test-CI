#!/usr/bin/env python3
"""DAPPER benchmarks the performance of data assimilation (DA) methods.

It is usually best to install from source (github),
so that you the code is readily available to play with.
See full README on [github](https://github.com/nansencenter/DAPPER).
"""

import os
import re
import sys

from setuptools import setup

# with open("README.md", "r") as fh:
#     long_description = fh.read()
DOCLINES = __doc__.split('\n')

# Dependencies
# Why pin?: https://github.com/nansencenter/DAPPER/issues/41#issuecomment-1381616971
INSTALL_REQUIRES = [
    'scipy>=1.10',
    'jupyter',
    'ipdb',
    'ipython>=5.1',
    # 'jedi<0.18',  # ipython/issues/12740
    'tornado~=6.3.2',  # 6.2 breaks Jupyter plots (tested on local Mac, Linux)
    'matplotlib~=3.7',
    'mpl-tools==0.2.50',
    'tqdm~=4.31',
    'pyyaml',
    'colorama~=0.4.1',
    'tabulate~=0.8.3',
    'dill==0.3.2',  # >=0.3.1.1 for dataclass. Pin vers. to equal GCP.
    'patlib==0.3.5',
    'struct-tools==0.2.5',
    # TODO 5: replace by p-tqdm?
    'multiprocessing-on-dill==3.5.0a4',
    'threadpoolctl>=3.0.0,<4.0.0',
]

EXTRAS = {
    'Qt': ['PyQt5', 'qtpy'],
    'debug': ['line_profiler', 'pre-commit', 'pdbpp>=0.10.3'],
    'test': ['tox', 'coverage>=5.1', 'pytest',
             'pytest-cov', 'pytest-sugar', 'pytest-benchmark',
             'pytest-clarity', 'pytest-xdist', 'pytest-timeout'],
    'lint': ['flake8<5',  # https://github.com/flakeheaven/flakeheaven/issues/132
             'flakeheaven', 'autopep8'],
    # 'flake8-docstrings', 'flake8-bugbear', 'flake8-comprehensions'],
    'build': ['twine', 'pdoc', 'jupytext'],
}
EXTRAS['dev'] = EXTRAS['debug'] + EXTRAS['test'] + EXTRAS['lint'] + EXTRAS['build']


setup(
    # Basic meta
    name="dapper",
    version="0.1",
    author="Patrick N. Raanes",
    author_email="patrick.n.raanes@gmail.com",
    description=DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    long_description_content_type="text/markdown",

    # >=3.5 for @.
    # >=3.6 for mpl>=3.1.
    # >=3.7 for dataclass, capture_output, dict ordering, np>=1.20.
    # ==3.7 for Colab
    # ==3.9 for the DAPPER/GCP cluster, since dill isn't compat. across versions.
    python_requires='>=3.9',
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS,

    # url="https://github.com/nansencenter/DAPPER",
)
