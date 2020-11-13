#!/usr/bin/env python3

import os,sys
from fabric.api import local

import sentry_sdk
sentry_sdk.init(
    "https://6c8f526768b74eada5b400a38737f100@o321364.ingest.sentry.io/5516015",
    traces_sample_rate=1.0
)

local('hostname')
