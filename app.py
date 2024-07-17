from flask import Flask, request, jsonify
import datetime
import uuid

app = Flask(__name__)

events = []

@app.route('/events', methods=['POST'])
def add_event():
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.datetime.now().isoformat(),
        "service": request.json['service'],
        "event_type": request.json['event_type'],
        "event_data": request.json['event_data']
    }
    events.append(event)
    return jsonify(event), 201

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
