#!/usr/bin/python3

from api.v1.views import app_views  # Import the blueprint
from flask import jsonify
import models

@app_views.route('/status, strict_slashes=False')
def get_status():
    """Returns a JSON response with "status": "OK"."""
    return jsonify({'status': 'OK'})

@app_views.route('/stats')
def status_page():
    """return the status of each model"""
    model = models.storage
    ret = {'amenities': model.count("Amenity"),
           'cities': model.count("City"),
           'places': model.count("Place"),
           'reviews': model.count("Review"),
           'states': model.count("State"),
           'users': model.count("User")}
    return jsonify(ret)