from apis.models.model import db


class Vessel(db.Model):
    __tablename__ = 'vessels'

    id = db.Column(db.BigInteger, primary_key=True)
    code = db.Column(db.String(8), unique=True)

    def __init__(self, vessel_code):
        self.code = vessel_code

    def saveVessel(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findVessel(cls, vessel_code):
        vessel = cls.query.filter_by(code=vessel_code).first()
        if vessel:
            return vessel
        return None
