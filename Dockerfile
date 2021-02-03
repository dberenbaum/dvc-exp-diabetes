FROM jupyter/base-notebook

# Enable Jupyter Lab
ENV JUPYTER_ENABLE_LAB=yes

# Install git
USER root
RUN apt-get update && apt-get install -yq git

# Update dependencies
ADD environment.yaml /home/${NB_USER}/environment.yaml
USER ${NB_USER}
RUN conda env update -n base -f environment.yaml
