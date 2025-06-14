import psutil
from prometheus_client import Gauge, REGISTRY


class ServerResourceCollector:
    def __init__(self):
        self.cpu_usage_gauge = Gauge('cpu_usage_percent', 'CPU Usage Percentage', registry=REGISTRY)
        self.memory_usage_gauge = Gauge('memory_usage_bytes', 'Memory Usage in Bytes', registry=REGISTRY)

    def collect(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        self.cpu_usage_gauge.set(cpu_usage)

        memory_info = psutil.virtual_memory()
        self.memory_usage_gauge.set(memory_info.used)
