<p align="center">
    <img src="./img/ask_lib_logo.png">
</p>

![](https://img.shields.io/pypi/l/ask_lib) 
![](https://img.shields.io/pypi/v/ask_lib) 
![](https://img.shields.io/pypi/pyversions/ask_lib)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation Status](https://readthedocs.org/projects/ask-lib/badge/?version=latest)](https://ask-lib.readthedocs.io/en/latest/?badge=latest)
[![CallMePixelMan's Workflow](https://github.com/CallMePixelMan/ask_lib/actions/workflows/callmepixelman-workflow.yaml/badge.svg)](https://github.com/CallMePixelMan/ask_lib/actions/workflows/callmepixelman-workflow.yaml)


# ask_lib
ask_lib is a small Python package available on PyPi that lets you ask user's confirmation from a [CLI](https://en.wikipedia.org/wiki/Command-line_interface).


## Documentation
You can take a look to [the documentation](https://ask-lib.readthedocs.io/en/latest/index.html), hosted by ReadTheDocs.


## Features
- [x] Simple API.
- [x] No dependencies.
- [x] Well tested.
- [x] Featuring CI.

## Install
```sh
pip install ask_lib

# Or, if you are using poetry
poetry add ask_lib
```

## Examples
```py
from ask_lib import ask, AskResult


to_remove = "file.txt"

if ask("Are you sure to delete this file ?", AskResult.NO):
    os.remove(to_remove)
```
```py
import os
import sys

from ask_lib import ask, AskResult


yes_to_all = AskFlag.YES_TO_ALL if "-force" in sys.argv else None
to_remove = "file.txt"

if ask("Are you sure to delete this file ?", flag=yes_to_all):
    os.remove(to_remove)
```