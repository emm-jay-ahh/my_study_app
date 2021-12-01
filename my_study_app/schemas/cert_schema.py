from main import ma 
from models.certs import Cert
from marshmallow_sqlalchemy import auto_field

class CertSchema(ma.SQLAlchemyAutoSchema):
    cert_id = auto_field(dump_only=True)
    
    class Meta:
        model = Cert
        load_instance = True
        
cert_schema = CertSchema()
certs_schema = CertSchema(many=True)