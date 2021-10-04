FROM ubuntu:20.04

RUN apt-get update && apt-get install -y
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip

COPY ./docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["bash","/app/docker-entrypoint.sh"]