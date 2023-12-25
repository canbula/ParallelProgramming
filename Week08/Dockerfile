FROM python:3.8

RUN apt-get update && apt-get install -y \
    python3-pip \
    htop \
    && pip3 install --upgrade pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt

COPY . /usr/src/app/

CMD python3 hi.py && tail -f /dev/null