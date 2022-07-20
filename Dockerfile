FROM python:3.7.13

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y build-essential

RUN mkdir /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

ADD pairwisemkl /app/pairwisemkl

# ADD modified /app/modified

WORKDIR /app/pairwisemkl

RUN python setup.py install

# docker build . -t incomplete-kernel-treatment
# docker run -it -v $(pwd):/app incomplete-kernel-treatment /bin/bash