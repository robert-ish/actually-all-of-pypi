import sys
import subprocess
from pypi_all_names.fetcher import fetch_all_package_names, save_as_txt
import os
import importlib

def install_all_packages():
    """Fetches all package names from pypi, then installs them. WARNING: DO NOT RUN! ITS KINDA LIKE A ZIPBOMB!"""
    package_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(package_dir, '__all_packages__.txt')

    names = fetch_all_package_names()
    if not os.path.exists(file_path):
        save_as_txt(names, file_path)
    cmd = [sys.executable, '-m', 'pip', 'install', '-r', str(file_path)]
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    for line in proc.stdout:
        print(line, end='')

    proc.wait()

def import_all_packages():
    """Imports all packages. Supposed to only be used after installing, otherwise raises error. Skips packages that cant import. DO NOT RUN, AS IT ALSO DOWNLOADS ALL PACKAGES!"""
    package_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(package_dir, '__all_packages__.txt')
    install_all_packages()
    with open(file_path, 'r') as f:
        for line in f:
            pkg = line.strip()
            try:
                importlib.import_module(pkg)
            except Exception:
                continue