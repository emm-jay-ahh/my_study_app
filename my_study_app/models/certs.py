from main import db


class Cert(db.Model):
    __tablename__ = "certs"
    cert_id = db.Column(db.Integer, primary_key=True)
    cert_name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, cert_name):
        self.cert_name = cert_name