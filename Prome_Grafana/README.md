## Monitoring a REST endpoint(s) serviceability using Prometheus and Grafana

### Overview: 
  The approach here is to use Prometheus and Grafana to monitor endpoints exposed by a simple Python app.
 The app also uses Prometheus counter to count the number of calls to a specific endpoint. A successful REST call
will return a value of 200. The demo shows only the measurement of successful calls. It is easy to add other measurements
as needed to Grafana since Prometheus already provides that and many more.

  To see all the metrics provided by Prometheus:

  curl 

  rest_api.py: Python App
  call_apis.py: To generate API calls and traffic
  measurements.py: Provides Prometheus counter and histogram support
  

### Build the images:

```


```

### Start the containers and check status:

```

Venky> docker-compose up -d
WARNING: The Docker Engine you're using is running in swarm mode.

Compose does not use swarm mode to deploy services to multiple nodes in a swarm. All containers will be scheduled on the current node.

To deploy your application across the swarm, use `docker stack deploy`.

Creating prome_grafana_node-exporter_1 ... done
Creating rest_api                      ... done
Creating prometheus                    ... done
Creating grafana                       ... done
Venky> docker-compose ps
            Name                           Command               State           Ports
-----------------------------------------------------------------------------------------------
grafana                         /run.sh                          Up      0.0.0.0:3000->3000/tcp
prome_grafana_node-exporter_1   /bin/node_exporter               Up      9100/tcp
prometheus                      /bin/prometheus --config.f ...   Up      0.0.0.0:9090->9090/tcp
rest_api                        python /app/rest_api.py          Up      0.0.0.0:5000->5000/tcp
Venky>

```

### Check the metrics exposed by the rest_api app

```
Venky> curl 0.0.0.0:5000/metrics
# HELP request_processing_seconds Time spent processing request
# TYPE request_processing_seconds summary
request_processing_seconds_count 0.0
request_processing_seconds_sum 0.0
# TYPE request_processing_seconds_created gauge
request_processing_seconds_created 1.582222915369964e+09
# HELP test_of_counter_total Number of times version called
# TYPE test_of_counter_total counter
test_of_counter_total 0.0                          <== Counts each call to the endpoint(/version)
# TYPE test_of_counter_created gauge
test_of_counter_created 1.58222291537003e+09
# HELP request_count_total App Request Count
# TYPE request_count_total counter
request_count_total{app_name="rest_api",endpoint="/metrics",http_status="200",method="GET"} 67.0
# TYPE request_count_created gauge
request_count_created{app_name="rest_api",endpoint="/metrics",http_status="200",method="GET"} 1.582222922022736e+09
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="2",minor="7",patchlevel="16",version="2.7.16"} 1.0
# HELP request_latency_seconds Request latency
# TYPE request_latency_seconds histogram
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="0.005"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="0.01"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="0.025"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="0.05"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="0.075"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="0.1"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="0.25"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="0.5"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="0.75"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="1.0"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="2.5"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="5.0"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="7.5"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="10.0"} 67.0
request_latency_seconds_bucket{app_name="rest_api",endpoint="/metrics",le="+Inf"} 67.0
request_latency_seconds_count{app_name="rest_api",endpoint="/metrics"} 67.0
request_latency_seconds_sum{app_name="rest_api",endpoint="/metrics"} 0.07958173751831055
# TYPE request_latency_seconds_created gauge
request_latency_seconds_created{app_name="rest_api",endpoint="/metrics"} 1.582222922022645e+09   <== Latency
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 2.3728128e+07
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.0488192e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.58222291429e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.52
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 7.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
Venky>

```

###  Add Prometheus as datasource to Grafana.

   Use: http://localhost:9090/metrics

  Make changes to Grafana interface to on the top left refresh time to 5s and change time-range to last 30 minutes.

###  Generate API calls

  Run: python call_apis.py


### Write PromQL query to monitor.


