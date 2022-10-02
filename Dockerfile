FROM python:3.6-slim

RUN pip install flask

WORKDIR /app
COPY . /app

CMD  python3 app.py

