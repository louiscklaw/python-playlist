#!/usr/bin/env python3

import os,sys


def func(x):
  return x + 1

def test_pass_testcase1(json_metadata):
  json_metadata['TEST_ID'] = 'TID_PASS01'
  assert func(4) == 5

def test_pass_testcase2(json_metadata):
  json_metadata['TEST_ID'] = 'TID_PASS02'
  assert func(4) == 5

def test_pass_testcase3(json_metadata):
  json_metadata['TEST_ID'] = 'TID_PASS03'
  assert func(4) == 5

def test_pass_testcase4(json_metadata):
  json_metadata['TEST_ID'] = 'TID_PASS04'
  assert func(4) == 5

def test_pass_testcase5(json_metadata):
  json_metadata['TEST_ID'] = 'TID_PASS05'
  assert func(4) == 5

def test_failed_testcase1(json_metadata):
  json_metadata['TEST_ID'] = 'TID_FAIL01'
  assert func(4) != 5

def test_failed_testcase2(json_metadata):
  json_metadata['TEST_ID'] = 'TID_FAIL02'
  assert func(4) != 5

def test_failed_testcase3(json_metadata):
  json_metadata['TEST_ID'] = 'TID_FAIL03'
  assert func(4) != 5
