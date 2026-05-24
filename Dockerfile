FROM ubuntu:24.04

RUN apt update && apt install -y python3 python3-pip

WORKDIR /app

COPY . /app

RUN pip3 install flask

CMD ["python3", "app.py"]
