FROM python:3.8-alpine

RUN apk update && apk add build-base
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
CMD ["python", "main.py"]