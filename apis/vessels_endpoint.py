from flask import Blueprint, request, jsonify
from sqlalchemy import func, extract, and_

from apis.models.vessel import Vessel


vessels_blueprint = Blueprint('vessels', __name__)


@vessels_blueprint.route('/insert_vessel', methods=['POST'])
def insert_vessel():
    """Insert a new vessel
        ---
        tags:
          - Vessels
        parameters:
            - name: code
              in: body
              type: string
              required: true
        responses:
          201:
            description: returns OK if the vessel was correctly inserted
          400:
            description: returns MISSING_PARAMETER if the vessel code is not sent
          400:
            description: returns WRONG_FORMAT if any parameter are sent in the wrong format
          409:
            description: returns FAIL if the vessel code is already in the system
    """

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
