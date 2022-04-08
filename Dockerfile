FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y build-essential

RUN mkdir /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

ADD original /app/original

ADD modified /app/modified

# RUN cd original

# RUN python setup.py install

# CMD [ "echo", "TESTE" ]

# docker build . -t incomplete-kernel-treatment
# docker run incomplete-kernel-treatment