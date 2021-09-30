FROM python:3.7.5
WORKDIR /server
ADD . /server
RUN pip install -r requirements.txt

CMD ["uwsgi","uwsgi.ini"]