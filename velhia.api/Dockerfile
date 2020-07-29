FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /Velh-IA
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /Velh-IA/velhia