FROM python:3.7
RUN mkdir -p /opt/service_metrics/src
COPY ./requirements.txt /opt/service_metrics/
COPY ./src/app.py /opt/service_metrics/src/
RUN pip install -r /opt/service_metrics/requirements.txt
WORKDIR /opt/service_metrics/
ENV PYTHONPATH '/opt/service_metrics/'
CMD ["python" , "/opt/service_metrics/src/app.py"]