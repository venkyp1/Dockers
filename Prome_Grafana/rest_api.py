from flask import Response, Flask, request
from measurement import setup_metrics
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import random, time

# Create my app
app = Flask(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
_INF = float("inf")

setup_metrics(app)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

graphs = {}
graphs['c'] =  Counter('test_of_counter', 'Number of times version called')

@app.route("/version", methods=["GET"])
def update_count():
    graphs['c'].inc()
    return get_metrics()

#@app.route('/metrics', methods=["GET"])
@app.route('/metrics')
def get_metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
