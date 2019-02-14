from json import dumps, loads
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('map.html')


@app.route("/api")
def api():
    callback_function = request.args.get('callback')
    data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": 0,
                "geometry": {
                    "type": "Point",
                    "coordinates": [55.831903, 37.411961]
                },
                "properties": {
                    "balloonContent": "Содержимое балуна",
                    "clusterCaption": "Метка 1",
                    "hintContent": "Текст подсказки 1"
                }
            },
            {
                "type": "Feature",
                "id": 1,
                "geometry": {
                    "type": "Point",
                    "coordinates": [55.763338, 37.565466]
                },
                "properties": {
                    "balloonContent": "Содержимое балуна",
                    "clusterCaption": "Метка 2",
                    "hintContent": "Текст подсказки 2"
                }
            },
            {
                "type": "Feature",
                "id": 2,
                "geometry": {
                    "type": "Point",
                    "coordinates": [56.000000, 37.311961]
                },
                "properties": {
                    "balloonContent": "Содержимое балуна",
                    "clusterCaption": "Метка 0",
                    "hintContent": "Текст подсказки 0"
                }
            }

        ]
    }
    json_data = dumps(data)
    response = f'{callback_function}({json_data})'
    return response
