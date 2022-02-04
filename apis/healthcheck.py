from flask import Blueprint, jsonify
import requests

healthcheck_blueprint = Blueprint('healthcheck', __name__)


@healthcheck_blueprint.route('/', methods=['GET'])
def healthcheck():

    page = requests.request(
        'GET', 'http://127.0.0.1:5000/equipment/active_equipments?vessel_code=wewwew')

    if page.status_code != 200:
        return jsonify(message='INTERNAL ERROR'), page.status_code

    print(page)

    return jsonify(message='OK'), 200
