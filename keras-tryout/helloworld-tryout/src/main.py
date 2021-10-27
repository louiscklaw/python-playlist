#!/usr/bin/env python3

import os,sys
from fabric.api import local

import numpy as np
import tensorflow as tf
from tensorflow import keras


local('hostname')
