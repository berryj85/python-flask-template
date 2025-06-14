import prometheus_flask_exporter
from flask import Flask
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

from src.controller import service_information

metrics = GunicornPrometheusMetrics.for_app_factory(defaults_prefix = prometheus_flask_exporter.NO_PREFIX)
def create_app():
    app = Flask(__name__)
    app.config.from_envvar("CONFIGURATION_FILE", silent=True)
    app.register_blueprint(service_information.blueprint)
    metrics.init_app(app)
    return app
