docker run -it `
  -v ${PWD}:/app `
  -w /app `
  -p 8888:8888 `
  --rm `
  jupyter/tensorflow-notebook `
  bash
