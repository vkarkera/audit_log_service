from flask import Flask, request, jsonify
import threading
import uuid
from datetime import datetime

app = Flask(__name__)

# In-memory storage for events
events = []
lock = threading.Lock()

@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + 'Z',
        "service": data.get('service'),
        "event_type": data.get('event_type'),
        "event_data": data.get('event_data', {})
    }

    with lock:
        events.append(event)

    return jsonify(event), 201

@app.route('/events', methods=['GET'])
def get_events():
    # Optional: Add filtering based on query parameters
    return jsonify(events), 200

if __name__ == '__main__':
    app.run(debug=True)
