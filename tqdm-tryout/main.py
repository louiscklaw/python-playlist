#!/usr/bin/env python3

import os,sys
from fabric.api import local
from time import sleep

from tqdm import tqdm, trange

for i in trange(100):
    sleep(0.1)