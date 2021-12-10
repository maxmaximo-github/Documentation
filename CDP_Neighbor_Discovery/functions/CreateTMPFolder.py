#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create a empty folder with name "tmp".

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "0.5.0"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"


# Import functions
from pathlib import Path


def CreateTMPFolder():
    """
    Create TMP Folder.

    Function to create TMP Folder in current directory work
    """
    cwd = Path.cwd()
    Path(f"{cwd}/tmp").mkdir(parents=True, exist_ok=True)