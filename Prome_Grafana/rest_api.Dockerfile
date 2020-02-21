FROM alpine
RUN  mkdir /app & apk update &&  \
     apk upgrade && apk add bash && \
     apk add python && apk add py-pip && \
     pip install flask datetime logger prometheus_flask_exporter prometheus_client werkzeug 
ADD  rest_api.py /app
ADD  measurement.py /app
EXPOSE 5000
WORKDIR /app
ENTRYPOINT ["python", "/app/rest_api.py"]
