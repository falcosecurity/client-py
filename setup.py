import os

import setuptools
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


about = {}
with open(os.path.join(here, "falco", "__version__.py"), "r") as f:
    exec(f.read(), about)

requires = ["grpcio==1.26.0", "python-dateutil==2.8.1", "protobuf==3.12.2"]
tests_require = ["pytest==5.3.5"]

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=requires,
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    tests_require=tests_require,
)
