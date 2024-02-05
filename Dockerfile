FROM python:3.10.5

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src src/
COPY entrypoint.sh .

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
