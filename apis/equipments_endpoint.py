from flask import Blueprint, request, jsonify
from sqlalchemy import func, extract, and_

from apis.models.vessel import Vessel
from apis.models.equipment import Equipment
from apis.models.model import db


equipments_blueprint = Blueprint('equipments', __name__)


@equipments_blueprint.route('/insert_equipment', methods=['POST'])
def insert_equipment():
    try:
        data = dict(request.json)

        if Vessel.getVesselByID(data['vessel_id']) is None:
            return jsonify(message='There is not a vessel for such id'), 409

        if Equipment.getEquipmentByCode(data['code']) is not None:
            return jsonify(message='Equipment {} already exits'.format(data['code'])), 409

        equipment = Equipment(data)

        result = equipment.saveEquipment()

        return result, 201
    except KeyError:
        return jsonify(message="No valid argument passed"), 400


@equipments_blueprint.route('/update_equipment_status', methods=['PUT'])
def update_equipment_status():
    try:

        data = dict(request.json)

        equipmentsNormalize = [str(equip).upper()
                               for equip in data['code']]
        result = []

        for equip in equipmentsNormalize:
            equipmentResult = Equipment.getEquipmentByCode(equip)

            if equipmentResult is None:
                return jsonify(message="There is not an equipment for such id {}".format(equip)), 409

            equipmentResult.setInactiveEquipment()
            equipmentResult.saveEquipment()
            result.append(equip)

        return jsonify(list=result), 201
    except KeyError:
        return jsonify(message="No valid argument passed"), 400


@equipments_blueprint.route('/active_equipments', methods=['GET'])
def active_equipment():

    return {'message': 'OK'}, 200
