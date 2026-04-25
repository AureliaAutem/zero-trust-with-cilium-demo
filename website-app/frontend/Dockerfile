FROM python:3.11-slim

WORKDIR /app

COPY server.py .

RUN apt-get update && apt-get install -y curl
RUN pip install requests

CMD ["python", "server.py"]