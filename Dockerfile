FROM python:3.9.7 as base

WORKDIR /api-mineria-py

COPY . ./

RUN apt-get update -y && apt-get install -y

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]