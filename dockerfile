FROM ubuntu:24.04

RUN apt update && \
    apt install -y python3 python3-pip curl docker.io

WORKDIR /app

COPY . /app

RUN pip3 install flask requests docker

CMD ["python3", "app.py"]
