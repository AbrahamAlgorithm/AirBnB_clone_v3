#!/usr/bin/python3

from api.v1.views import app_views  # Import the blueprint

@app_views.route('/status')
def index():
    """Returns a JSON response with "status": "OK"."""
    return jsonify({'status': 'OK'})