FROM python:3.10-slim

WORKDIR /

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY app/* ./app/

EXPOSE 80

CMD ["python", "/app/server.py"]
