# actually-all-of-pypi
> **WARNING: DO NOT RUN ANY OF THE THINGS FROM THIS LIBRARY UNLESS YOU'RE WILLING TO NUKE YOUR COMPUTER**

Functions to install and import every package on PyPI.
## installation
```bash
pip install actually-all-of-pypi
```
## Usage:
```python
#Install with actually-all-of-pypi but import with actually_all_of_pypi
from actually_all_of_pypi import import_all_packages
import_all_packages()
# Then you can do anything you want...
```
## Available functions:
### install_all_packages
Fetches then installs all packages from PyPI
can also be called with the bash command: install-all-of-pypi
### import_all_packages
Installs all packages from PyPI, then imports them.  
> Note: probably wont work, since some libraries have conflicting dependencies.
