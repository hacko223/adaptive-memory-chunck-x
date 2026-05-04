from setuptools import setup, find_packages

setup(
    name="amcx",
    version="0.1.0",
    description="Adaptive Memory Chunk X - A library for efficient memory chunking",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="hacko223",
    author_email="",
    url="https://github.com/hacko223/adaptive-memory-chunk-x",
    license="LGPL-3.0-or-later",
    packages=find_packages(),
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
