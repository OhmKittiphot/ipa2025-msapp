FROM python
RUN pip install flask
RUN pip install pymongo
WORKDIR /app
COPY . .
EXPOSE 8080
CMD python3 /app/app.py