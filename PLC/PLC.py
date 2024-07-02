from flask import Flask, request, jsonify

app = Flask(__name__)

light_state = "red"

@app.route('/update', methods=['POST'])
def update_light():
    global light_state
    data = request.get_json()
    if data["command"] == "change_light":
        if light_state == "red":
            light_state = "green"
        elif light_state == "green":
            light_state = "yellow"
        elif light_state == "yellow":
            light_state = "red"
        return jsonify({"status": "light changed", "current_light": light_state}), 200
    return jsonify({"status": "invalid command"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)