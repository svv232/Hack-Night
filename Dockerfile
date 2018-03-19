FROM ubuntu:16.04
MAINTAINER Sai

RUN apt-get update && apt-get install -y \
    apt-utils \
    build-essential \
    vim \
    git \
    python-pip 

RUN git clone https://github.com/trailofbits/manticore.git && \
    pip install --upgrade pip && \
    python -m pip install manticore && \
    python -m pip install pwntools

ADD examples /home/examples/

WORKDIR /home/

CMD /bin/bash
