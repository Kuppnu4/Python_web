FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip

COPY helper-app /app

RUN pip install -r helper-app/requirements.txt

CMD ["python3", "/app"]