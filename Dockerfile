FROM python:3.7.13

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y build-essential

RUN mkdir /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

ADD pairwisemkl /app/pairwisemkl

WORKDIR /app/pairwisemkl

RUN python setup.py install

CMD [ "python", "main_modified.py" ]

# docker build . -t incomplete-kernel-treatment
# docker run -it -v $(pwd):/app incomplete-kernel-treatment /bin/bash
# docker run -v $(pwd):/app -d incomplete-kernel-treatment

# IP: 192.168.0.151 Senha: workshop