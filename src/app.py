import prometheus_client
import requests
from flask import Flask, Response
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client.exposition import CONTENT_TYPE_LATEST

# All the urls which we want to monitor
endpoints = ['https://httpstat.us/200','https://httpstat.us/503']

app = Flask(__name__)

class CustomCollector(object):
    def __init__(self):
        pass

# This is giving the status code of the url and response time using elapse time
    def urlAudit(self,url):
        response = requests.get(url)
        status_code = response.status_code
        time_ms = (response.elapsed.seconds)  / 1000
        if status_code == 200:
            return 1, time_ms
        elif status_code == 503:
            return 0, time_ms

# For sending the metrics  -- Prometheus

    def collect(self):
        for url in endpoints:
            status_code, time_ms = self.urlAudit(url)
            urlStat = GaugeMetricFamily("sample_external_url_up", 'status Code', labels=['url'])
            urlStat.add_metric([url], status_code)
            yield urlStat

            rTime = GaugeMetricFamily("sample_external_url_response_ms", 'URl Response in ms', labels=['url'])
            rTime.add_metric([url], time_ms)
            yield rTime

@app.route("/")
@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    REGISTRY.register(CustomCollector())
    app.run(host='0.0.0.0')