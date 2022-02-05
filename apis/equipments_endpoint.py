from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequestKeyError

from apis.models.vessel import Vessel
from apis.models.equipment import Equipment


equipments_blueprint = Blueprint('equipments', __name__)


@equipments_blueprint.route('/insert_equipment', methods=['POST'])
def insert_equipment():
    try:
        data = dict(request.json)

        if Vessel.getVesselByID(data['vessel_id']) is None:
            return jsonify(message='NO_VESSEL'), 409

        if Equipment.getEquipmentByCode(data['code']) is not None:
            return jsonify(message='REPEATED_CODE'), 409

        equipment = Equipment(data)

        equipment.saveEquipment()

        return jsonify(message="OK"), 201
    except KeyError:
        return jsonify(message="MISSING_PARAMETER"), 400


@equipments_blueprint.route('/update_equipment_status', methods=['PUT'])
def update_equipment_status():
    try:

        data = dict(request.json)

        equipmentsNormalize = [str(equip).upper()
                               for equip in data['code']]

        for equip in equipmentsNormalize:
            equipmentResult = Equipment.getEquipmentByCode(equip)

            if equipmentResult is None:
                return jsonify(message="NO_CODE"), 409

            equipmentResult.setInactiveEquipment()
            equipmentResult.saveEquipment()

        return jsonify(message="OK"), 201
    except KeyError:
        return jsonify(message="MISSING_PARAMETER"), 400


@equipments_blueprint.route('/active_equipments', methods=['GET'])
def active_equipment():

    try:

        data = request.args['vessel_code']

        vessel = Vessel.getVesselByCode(data)

        if vessel is None:
            return jsonify(message='NO_VESSEL'), 409

        equipmentsActive = Equipment.getActiveEquipments(vessel.code)

        equipmentsArray = []

        for equip in equipmentsActive:
            equipSet = {
                "id": equip.id,
                "vessel_id": equip.vessel_id,
                "name": equip.name,
                "code": equip.code,
                "location": equip.location,
                "active": equip.active
            }
            equipmentsArray.append(equipSet)

        result = {
            vessel.code: equipmentsArray
        }

        return jsonify(result), 200
    except BadRequestKeyError:
        return jsonify(message="MISSING_PARAMETER"), 400
