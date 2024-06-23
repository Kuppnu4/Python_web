FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip

WORKDIR /docker_test

COPY docker_test /docker_test

RUN pip install -r /docker_test/requirements.txt

RUN pip install .

CMD ["python3", "__main__.py"]