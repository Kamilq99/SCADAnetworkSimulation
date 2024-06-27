from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

traffic_light_state = 'RED'

#This function controls, a traffic lights, chaning them every 30 seconds
def change_traffic_light_state():
    global traffic_light_state
    while True:
        if traffic_light_state == 'RED':
            traffic_light_state = 'GREEN'
        elif traffic_light_state == 'GREEN':
            traffic_light_state = 'YELLOW'
        elif traffic_light_state == 'YELLOW':
            traffic_light_state = 'RED'
        time.sleep(30)

#Here is API, wchich giving, a DATA to SCADA controller.
@app.route('/state', methods=['GET'])
def get_state():
    return jsonify({'state': traffic_light_state})

@app.route('/state', methods=['POST'])
def set_state():
    global traffic_light_state
    data = request.json
    if 'state' in data:
        traffic_light_state = data['state']
        return jsonify({'state': traffic_light_state})
    else:
        return jsonify({'error': 'Invalid request'}), 400

if __name__ == "__main__":
    threading.Thread(target=change_traffic_light_state).start()
    app.run(host='0.0.0.0', port=5000)
