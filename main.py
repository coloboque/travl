from json import dumps, loads
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('map.html')


@app.route("/api")
def api():
    callback_function = request.args.get('callback')
    coordinates = request.args.get('bbox')
    x_min, y_min, x_max, y_max = coordinates.split(',')
    x_min, y_min, x_max, y_max = float(x_min), float(y_min), float(x_max), float(y_max)
    with open('data.json', 'r') as fp:
        raw_data = loads(fp.read())
    data = {
        "type": "FeatureCollection",
        "features": []
    }
    for item in raw_data['features']:
        if x_min < item["geometry"]["coordinates"][0] < x_max:
            if y_min < item["geometry"]["coordinates"][1] < y_max:
                data['features'].append(item)
    print('points:', len(data['features']))
    json_data = dumps(data)
    response = f'{callback_function}({json_data})'
    return response
