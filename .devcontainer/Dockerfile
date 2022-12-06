FROM mcr.microsoft.com/devcontainers/python:3.11
# For GPU support use the following instead of the above:
# FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive

COPY ../requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code