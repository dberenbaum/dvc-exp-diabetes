# dvc-exp-diabetes

This project shows how to use `dvc experiments`, using `scikit-learn` on the
[diabetes](https://sklearn.org/datasets/index.html#diabetes-dataset) dataset to
predict disease progression one year after the baseline.

### Get started

To get started, clone this repository and navigate to it.

The only other prerequisite is [docker](https://www.docker.com/). Once docker is installed, build a
docker image from the existing Dockerfile and run it:

```bash
docker build -t dvc-exp-diabetes .
docker run -v $(pwd):/home/jovyan/dvc-exp-diabetes -p 8888:8888 $(docker images -q dvc-exp-diabetes)
```

To run the notebook, navigate to the link provided in the output that starts with http://127.0.0.1:8888/.
