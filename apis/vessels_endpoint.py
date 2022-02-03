from flask import Blueprint, request, jsonify
from sqlalchemy import func, extract, and_

from apis.models.vessel import Vessel
from apis.models.model import db


vessels_blueprint = Blueprint('vessels', __name__)


@vessels_blueprint.route('/insert_vessel', methods=['POST'])
def insert_vessel():

    data = dict(request.json)

    if data.get('code') is None:
        return jsonify(message="No valid argument passed"), 400

    vessel_code = data['code']

    vessel = Vessel(vessel_code)

    if vessel.findVessel(vessel_code):
        return jsonify(message="Vessel code {} already exists.".format(vessel_code)), 409

    vessel.saveVessel()
    return jsonify(data), 201
