#!/usr/bin/env bash

set -ex

# pip install pyppeteer
# pip install pytest-playwright
pip install playwright
pip install nest_asyncio


# pip install pytest-playwright playwright -U

# python3 ./helloworld.py
pytest
