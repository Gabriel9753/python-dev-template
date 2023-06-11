ARG PYTHON_VERSION

#################################################
####### Base Image Configuration Section ########
#################################################
# Alternative base images for different needs:
# - https://hub.docker.com/_/python/ (official Python images)
# - https://hub.docker.com/_/ubuntu/ (official Ubuntu images)
# - mcr.microsoft.com/devcontainers/python:$PYTHON_VERSION for a Python-specific development container.
# - python:3.9-alpine for a slim and simple Python base.
# - ubuntu:latest if you need a full-fledged Ubuntu environment with Python.
# - nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04 for a CUDA-enabled Python environment.

# Uncomment the line matching your requirements
# FROM python:$PYTHON_VERSION-alpine
FROM python:$PYTHON_VERSION
# FROM mcr.microsoft.com/devcontainers/python:$PYTHON_VERSION
# FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04

WORKDIR /workspaces

# Set environment variables. Uncomment these lines to add additional environment variables
# ENV MY_ENV_VAR MY_ENV_VALUE

################################################
####### Additional OS Packages Section #########
################################################
# Uncomment this section to install additional OS packages.
# You might want to add some common debug tools here
# RUN apt-get update \
#     && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends \
        # For networking analysis
        # net-tools \
        # For binary file analysis
        # binutils \
        # For web scraping or testing
        # curl wget \
        # For text processing
        # awk sed grep \
        # For building Python native extensions
        # python3-dev python3-setuptools \
        # For compiling certain Python packages
        # g++ gcc \
        # For database connectivity
        # libpq-dev \
        # For image processing
        # libjpeg-dev zlib1g-dev \
        # For XML and HTML processing
        # libxml2-dev libxslt1-dev \
        # For scientific computing
        # libatlas-base-dev gfortran \
        # For machine learning
        # libhdf5-serial-dev \
        # For cryptography
        # libssl-dev \
    # && apt-get autoremove -y \
    # && apt-get clean -y \
    # && rm -rf /var/lib/apt/lists/*

################################################
########## GPU Support Section #################
################################################
# For GPU support use the following instead of the above:
# RUN apt-get update \
#     && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends python3 python3-pip \
#     && pip install pip==22.3 \
#     && pip --no-cache-dir install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

################################################
####### Application Setup Section ##############
################################################
# Copy the requirements file into the container
COPY requirements.txt .
# Install your application's dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
# Copy your application into the container
# COPY . /workspaces

# Uncomment the following line to run a script at container startup
# CMD ["python", "your_application.py"]

################################################
######### Ports Configuration Section ##########
################################################
# Expose any necessary ports. Uncomment this line to expose ports
# EXPOSE 8080

################################################
####### Entrypoint Configuration Section #######
################################################
# For setting an entrypoint, you can use the following command
# ENTRYPOINT ["python", "your_application.py"]

# In case you need to use a command as well as an entrypoint
# CMD ["--help"]

################################################
####### Volume Configuration Section ############
################################################
# If your application requires persisting data or needs access to specific directories on the host machine,
# use the VOLUME command to enable access from your container to the host.
# VOLUME [ "/data" ]

################################################
####### Healthcheck Configuration Section #######
################################################
# Docker provides a HEALTHCHECK instruction to let you specify a command to run to check the health of your application
# For example, you might want to call a HTTP endpoint, or a database query, or some other command that will return an error
# if your application is not working correctly. This can be very useful in a production environment to detect issues early.
# HEALTHCHECK CMD curl --fail http://localhost:8080/ || exit 1
