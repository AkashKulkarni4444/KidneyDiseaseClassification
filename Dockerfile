FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

ENV MLFLOW_TRACKING_URI=https://dagshub.com/AkashKulkarni4444/KidneyDiseaseClassification.mlflow
ENV MLFLOW_TRACKING_USERNAME=AkashKulkarni4444
ENV MLFLOW_TRACKING_PASSWORD=a5822a71ae059c7a235dcb34190305eb72d1b62e
EXPOSE 8080
CMD ["python3", "app.py"]