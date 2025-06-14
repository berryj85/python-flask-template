from flask import Blueprint, jsonify, current_app

blueprint = Blueprint("service_information", __name__)


@blueprint.get("/health")
def health():
    return jsonify({"status": "UP"})


@blueprint.get("/info")
def info():
    response = {
        "name": current_app.config.get("APP_NAME"),
        "version": current_app.config.get("APP_VERSION")
    }
    return jsonify(response)
