FROM python:3.9-slim

WORKDIR /app

COPY roteador.py .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
