FROM python:3.11

WORKDIR /app

ADD main.py .

CMD ["python", "./main.py"]