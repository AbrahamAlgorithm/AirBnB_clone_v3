from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route('/stats', methods=['GET'])
def stats():
    """Retrieves the number of objects by class"""
    classes = {
        'Amenity': 'amenities',
        'City': 'cities',
        'Place': 'places',
        'Review': 'reviews',
        'State': 'states',
        'User': 'users'
    }
    stats = {}
    for cls_name, class_key in classes.items():
        cls = storage.count(cls_name)
        stats[class_key] = cls
    return jsonify(stats)