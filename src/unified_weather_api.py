from flask import Flask, jsonify, request
from kafka import KafkaProducer
import json
from json import dumps
from fetch_data import fetch_open_weather_data, fetch_weatherapi_data

def service_unified_weather_api():
    app = Flask("app")
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        api_version=(0, 11, 5),
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )
    topic = "views_api"

    @app.route("/current_weather/<location>", methods=['GET'])
    def get_current_weather(location):
        try:
            open_weather_data = fetch_open_weather_data(location)
            weatherapi_data = fetch_weatherapi_data(location)

            unified_data = {
                "open_weather": open_weather_data,
                "weatherapi": weatherapi_data
            }

            producer.send(topic, value=unified_data)
            
            return jsonify(unified_data)

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app

if __name__ == "__main__":
    app = service_unified_weather_api()
    app.run(debug=True, port=5000)
