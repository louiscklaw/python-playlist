#!/usr/bin/env bash

set -ex

# pip install playwright &
# pip install nest_asyncio &
# pip install jupyter &

# wait

# playwright install-deps
# playwright install

# pip install python-dotenv

# wait 


jupyter notebook \
  --allow-root \
  --notebook-dir=notebook \
  --ip='*' \
  --NotebookApp.token='' \
  --NotebookApp.password=''
  