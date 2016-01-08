FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /project
WORKDIR /project

ADD requirements.txt /project/
RUN pip install -r requirements.txt

EXPOSE 8000

ADD . /project/


