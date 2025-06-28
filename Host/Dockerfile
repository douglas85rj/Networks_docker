FROM python:3

RUN apt-get update -y && apt-get install -y python3-pip  python3-dev

WORKDIR /app

RUN pip install Flask requests flask_mysqldb


COPY . .

EXPOSE 5001

CMD ["python", "app.py"]


