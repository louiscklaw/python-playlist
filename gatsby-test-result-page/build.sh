#!/usr/bin/env bash

set -ex

yarn

yarn build

cd public
  live-server .
