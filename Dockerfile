FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /Arbitria
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /Arbitria/velhia