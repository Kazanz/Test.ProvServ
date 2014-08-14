from app import db


class ProvServer(db.Model):
    __tablename__ =  'provisioning_provserver'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    device_id = db.Column(db.Integer, nullable=False)
    ips = db.Column(db.String(25), nullable=False)
    in_use = db.Column(db.Boolean, nullable=False)
    test_passed = db.Column(db.Boolean)
    date_of_test = db.Column(db.String(50))
    client_id = db.Column(db.Integer)

    def __repr__(self):
        return "<ProvServer {}>".format(self.device_id)
