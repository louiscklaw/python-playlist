#!/usr/bin/env python3
import os,sys
import pytest

from config import *
from src.main import *

# hooking test
from lib.test_helloworld import *

def test_funcABCDE():
  funcABCDE()
