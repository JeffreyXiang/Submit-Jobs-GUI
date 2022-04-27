#!/bin/bash
conda create -n submit_jobs python=3.8 && \
source activate submit_jobs && \
pip install PyQt5 && \
pip install --upgrade --disable-pip-version-check --extra-index-url https://azuremlsdktestpypi.azureedge.net/K8s-Compute/D58E86006C65 azureml_contrib_k8s && \
pip install azureml-contrib-aisc && \
pip install azureml-sdk==1.32.0