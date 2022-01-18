FROM python:3.9

ADD . /app/
WORKDIR /app

RUN pip install bs4
RUN pip install requests
RUN pip install lxml

CMD python crous.py