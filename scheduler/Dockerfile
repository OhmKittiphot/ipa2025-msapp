FROM python
RUN pip install pymongo
RUN pip install pika
WORKDIR /scheduler
COPY . .
CMD python3 scheduler