FROM python:3.11-slim

WORKDIR /app

RUN pip install flask requests

COPY api.py .

CMD ["python", "api.py"]