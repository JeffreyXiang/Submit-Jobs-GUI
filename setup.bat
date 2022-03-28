@echo off
call conda create -n submit_jobs python=3.8
call conda activate submit_jobs
call pip install PyQt5
call pip install --upgrade --disable-pip-version-check --extra-index-url https://azuremlsdktestpypi.azureedge.net/K8s-Compute/D58E86006C65 azureml_contrib_k8s
call pip install azureml-contrib-aisc
call pip install azureml-sdk==1.32.0
