[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPI Version](https://img.shields.io/pypi/v/simple-google-vision.svg)](https://pypi.org/project/simple-google-vision/)
[![build status](http://img.shields.io/travis/robmarkcole/simple-google-vision/master.svg?style=flat)](https://travis-ci.org/robmarkcole/simple-google-vision

# simple-google-vision
Unofficial helper utilities for using Google Vision, providing helper utilities for using Google Vision. Currently supports object detection endpoint with functions for processing the result or requests.

## Development
* Use `venv` -> `python3 -m venv venv` & `source venv/bin/activate`
* `pip install -e .`
* `pip install -r requirements-dev.txt`
* Run tests with `venv/bin/pytest tests/*`
* Black format with `venv/bin/black gvision/core.py` and `venv/bin/black tests/test_gvision.py`