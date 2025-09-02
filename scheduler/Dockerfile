FROM python:3.12-slim
WORKDIR /scheduler
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "-u", "scheduler.py"]