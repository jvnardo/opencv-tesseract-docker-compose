# https://hub.docker.com/_/ubuntu/

FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip
RUN echo "alias python='python3'\nalias pip='pip3'" >> ~/.bashrc
RUN pip3 install -U pip
# ---------------
# | JUPYTER LAB |
# ---------------
RUN pip3 install jupyter jupyterlab>=3.0.10

# ------------------
# | INSTALL FFMPEG |--------------------------
# | https://packages.ubuntu.com/focal/ffmpeg |
# --------------------------------------------
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ffmpeg

# ------------------
# | INSTALL OPENCV |
# ------------------
RUN pip3 install numpy
RUN pip3 install opencv-python

# ---------------------------
# | INSTALL ADDITIONAL APTs |
# ---------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    ca-certificates \
    ssh \
    nano \
    htop \
    unzip \
    wget \
    apt-transport-https \
    ca-certificates \
    tesseract-ocr \
    libtesseract-dev

# ----------------------------
# | INSTALL PYTHON LIBRARIES |
# ----------------------------
# COPY requirements.txt /
RUN pip3 install pytesseract

# -------------------
# | SETUP WORKSPACE |
# -------------------
WORKDIR /workspace

ENV jupyter_base_url=/
ENV jupyter_pass=minh@2021
ENV PYTHONIOENCODING=utf-8

COPY run.sh /
RUN chmod +x /run.sh
CMD "/run.sh"
