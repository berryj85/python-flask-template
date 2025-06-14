import multiprocessing

from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

from src.collector.server_resource_collector import ServerResourceCollector

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2
server_resource_collector = ServerResourceCollector()


def when_ready(server):
    GunicornPrometheusMetrics.start_http_server_when_ready(8001)


def child_exit(server, worker):
    GunicornPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)
