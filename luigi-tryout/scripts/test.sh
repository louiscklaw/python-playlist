#!/usr/bin/env bash

set -x

# pipenv run python3 luigi --module my_module MyTask --x 123 --y 456 --local-scheduler

# pipenv run python -m luigi --module my_module MyTask --x 100 --local-scheduler

rm -rf tmp/helloworld.txt
rm -rf tmp/helloworld.txt.name_Adnan
rm -rf tmp/.*

pipenv run python luigitutorial.py --scheduler-host localhost NameSubstituter --name Adnan  &


wait
