FROM jupyter/base-notebook

# Install git
USER root
RUN apt-get update && apt-get install -yq git

# Clone repo and update dependencies
USER jovyan
RUN git clone https://github.com/dberenbaum/dvc-exp-diabetes.git
WORKDIR dvc-exp-diabetes
RUN conda env update -n base -f environment.yaml
