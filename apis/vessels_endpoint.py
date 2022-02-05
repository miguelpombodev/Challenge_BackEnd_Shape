from flask import Blueprint, request, jsonify
from sqlalchemy import func, extract, and_

from apis.models.vessel import Vessel


vessels_blueprint = Blueprint('vessels', __name__)


@vessels_blueprint.route('/insert_vessel', methods=['POST'])
def insert_vessel():

    try:
        data = dict(request.json)

        vessel_code = data['code']

        vessel = Vessel(vessel_code)

        if vessel.getVesselByCode(vessel_code):
            return jsonify(message="FAIL"), 409

        vessel.saveVessel()

        return jsonify(message="OK"), 201
    except KeyError:
        return jsonify(message="MISSING_PARAMETER"), 400
