docker run -it `
  -v ${PWD}/base-notebook:/app `
  -w /app `
  -p 8888:8888 `
  --rm `
  jupyter/base-notebook `
  bash
