FROM python:3.12-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8082
CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--port=8082"]