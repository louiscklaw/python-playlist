#!/usr/bin/env bash

set -ex

nodemon -w . -e "py,sh" --ignore './node_modules' --ignore './public' --ignore './reports'  --delay 500ms --exec './run.sh'