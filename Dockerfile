FROM python:3.10.5

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
