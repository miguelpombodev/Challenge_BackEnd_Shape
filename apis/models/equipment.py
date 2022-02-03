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

    def __init__(self, data):
        self.vessel_id = data['vessel_id'],
        self.name = str(data['name']).upper(),
        self.code = str(data['code']).upper(),
        self.location = str(data['location']).capitalize(),
        self.active = True

    def saveEquipment(self):
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

    
    def getEquipmentVessel(self, vessel_id):
        vessel_id = self.query.filter_by(vessel_id=vessel_id).first()
        if vessel_id:
            return vessel_id
        return None

    
    def getEquipmentByCode(self, code):
        equip = self.query.filter_by(code=code).first()
        if equip:
            return equip
        return None
