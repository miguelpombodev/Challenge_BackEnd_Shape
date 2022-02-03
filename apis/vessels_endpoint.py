from flask import Blueprint, request, jsonify
from sqlalchemy import func, extract, and_

from apis.models.vessel import Vessel
from apis.models.model import db


vessels_blueprint = Blueprint('vessels', __name__)


@vessels_blueprint.route('/insert_vessel', methods=['POST'])
def insert_vessel():

    try:
        data = dict(request.json)

        vessel_code = data['code']

        vessel = Vessel(vessel_code)

        if vessel.findVessel(vessel_code):
            return jsonify(message="Vessel code {} already exists.".format(vessel_code)), 409

        result = vessel.saveVessel()
        return result, 201
    except KeyError:
        return jsonify(message="No valid argument passed"), 400
