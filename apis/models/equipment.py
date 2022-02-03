from apis.models.equipment import Equipment
from typing import Union
from apis.models.model import db
from flask import jsonify


class Equipment(db.Model):
    __tablename__ = 'equipments'

    id = db.Column(db.BigInteger, primary_key=True)
    vessel_id = db.Column(db.BigInteger, db.ForeignKey('vessels.id'))
    name = db.Column(db.String(256))
    code = db.Column(db.String(8), unique=True)
    location = db.Column(db.String(256))
    active = db.Column(db.Boolean)

    def __init__(self, data: dict):
        self.vessel_id = data['vessel_id'],
        self.name = str(data['name']).upper(),
        self.code = str(data['code']).upper(),
        self.location = str(data['location']).capitalize(),
        self.active = True

    def saveEquipment(self) -> Equipment:
        '''
          Method saves the created instance of Equipment in database
        '''
        try:
            db.session.add(self)
            db.session.commit()
            return jsonify(
                id=self.id,
                vessel_id=self.vessel_id,
                name=self.name,
                code=self.code,
                location=self.location,
                active=self.active
            )
        except:
            return jsonify(message='Internal error ocurred trying to save equipment')

    # @classmethod
    # def getEquipmentVessel(cls, vessel_id: int) -> Union[Equipment, None]:
    #     '''
    #       Method searches for a vessel which CODE is registered in database

    #       If there is not such code, it returns None

    #       PARAMETERS:
    #         - vessel_code: string
    #     '''
    #     vessel_id = cls.query.filter_by(vessel_id=vessel_id).first()
    #     if vessel_id:
    #         return vessel_id
    #     return None

    @classmethod
    def getEquipmentByCode(cls, code: int) -> Union[Equipment, None]:
        '''
          Method searches for a equipement code that is already registered in database

          If there is not such equipement code, it returns None

          PARAMETERS:
            - vessel_code: string
        '''
        equip = cls.query.filter_by(code=code).first()
        if equip:
            return equip
        return None
