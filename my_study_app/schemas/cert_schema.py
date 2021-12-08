from main import ma 
from models.certs import Cert
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length


class CertSchema(ma.SQLAlchemyAutoSchema):
    cert_id = auto_field(dump_only=True)
    cert_name = auto_field(required=True, validate=Length(min=1))
    
    class Meta:
        model = Cert
        load_instance = True
        
cert_schema = CertSchema()
certs_schema = CertSchema(many=True)