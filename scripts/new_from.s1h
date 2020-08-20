#!/usr/bin/env bash

set -x

rm -rf * &
rm -rf .* &
wait

TEST=`echo $PWD|rev |cut -d'/' -f1 |rev`
git branch -D test/$TEST
git checkout -b test/$TEST

rsync -avzh --exclude node_modules --exclude .cache --exclude public ../$1/ .


pipenv sync
