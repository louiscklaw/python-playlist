#!/usr/bin/env bash

nodemon -e'json' -w src/result_jsons/ --exec "rsync -avzh src/result_jsons/*.json public/json"