######################################################################
# BioSimSpace: Making biomolecular simulation a breeze!
#
# Copyright: 2017-2018
#
# Authors: Lester Hedges <lester.hedges@gmail.com>
#
# BioSimSpace is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# BioSimSpace is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BioSimSpace. If not, see <http://www.gnu.org/licenses/>.
#####################################################################

"""
Custom context managers.
Author: Lester Hedges <lester.hedges@gmail.com>
"""

from contextlib import contextmanager as _contextmanager

import os as _os

__all__ = ["cd"]

# Adapted from: http://ralsina.me/weblog/posts/BB963.html
@_contextmanager
def cd(work_dir):
    """Execute the context in the directory 'dir'


       Positional arguments
       --------------------

       work_dir : str
           The working directory for the context.
    """
    # Store the current directory.
    old_dir = _os.getcwd()

    # Create the working directory if it doesn't exist.
    if not _os.path.isdir(work_dir):
        _os.makedirs(work_dir)

    # Change to the new directory.
    _os.chdir(work_dir)

    # Execute the context.
    try:
        yield

    # Return to original directory.
    finally:
        _os.chdir(old_dir)
