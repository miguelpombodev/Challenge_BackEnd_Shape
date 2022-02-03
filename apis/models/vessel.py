from apis.models.vessel import Vessel
from apis.models.model import db
from typing import Union
from flask import jsonify


class Vessel(db.Model):
    __tablename__ = 'vessels'

    id = db.Column(db.BigInteger, primary_key=True)
    code = db.Column(db.String(8), unique=True)

    def __init__(self, vessel_code: str):
        self.code = vessel_code

    def saveVessel(self) -> Vessel:
        '''
          Method saves the created instance of Vessel in database
        '''

        try:
            db.session.add(self)
            db.session.commit()
            return jsonify(id=self.id, code=self.code)
        except:
            return jsonify(message='Internal error ocurred trying to save vessel')

    @classmethod
    def getVesselByCode(cls, vessel_code: str) -> Union[Vessel, None]:
        '''
          Method searches for a vessel which CODE is registered in database

          If there is not such code, it returns None

          PARAMETERS:
            - vessel_code: string
        '''

        vessel = cls.query.filter_by(code=vessel_code).first()
        if vessel:
            return vessel
        return None

    @classmethod
    def getVesselByID(cls, vessel_id: int) -> Union[Vessel, None]:
        '''
          Method searches for a vessel which ID is registered in database

          If there is not such ID, it returns None

          PARAMETERS:
            - vessel_id: int
        '''

        vessel = cls.query.filter_by(id=vessel_id).first()
        if vessel:
            return vessel
        return None
