from setuptools import setup, find_packages

VERSION = "0.4"

REQUIRES = [
    "google-cloud-vision",
    "google-oauth"
]

setup(
    name="simple-google-vision",
    version=VERSION,
    url="https://github.com/robmarkcole/simple-google-vision",
    author="Robin Cole",
    author_email="robmarkcole@gmail.com",
    description="Unofficial helpers for Google Vision",
    install_requires=REQUIRES,
    packages=find_packages(),
    license="Apache License, Version 2.0",
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
