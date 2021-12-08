from flask import Blueprint, jsonify, request, render_template
from main import db
from models.certs import Cert
from schemas.cert_schema import certs_schema, cert_schema

certs = Blueprint('certs', __name__)

# @app.route('/', methods=["GET"])
#     def home():
#         return "Welcome to 'My Study App'"


@certs.route("/certs/", methods=["GET"])
def get_certs():
    data = {
    "page_title": "Certs",
    "certs": certs_schema.dump(Cert.query.all())
    }
    return render_template("cert_index.html", page_data = data)


@certs.route("/certs/", methods=["POST"])
def create_cert():
    new_cert=cert_schema.load(request.form)
    db.session.add(new_cert)
    db.session.commit()
    return jsonify(cert_schema.dump(new_cert))


@certs.route("/certs/<int:id>/", methods = ["GET"])
def get_cert(id):
    cert = Cert.query.get_or_404(id)
    return jsonify(cert_schema.dump(cert))


@certs.route("/certs/<int:id>/", methods=["PUT", "PATCH"])
def update_cert(id):
    cert = Cert.query.filter_by(cert_id=id)
    updated_fields = cert_schema.dump(request.json)
    if updated_fields:
        cert.update(updated_fields)
        db.session.commit()
    return jsonify(cert_schema.dump(cert.first()))


@certs.route("/certs/<int:id>/", methods = ["DELETE"])
def delete_cert(id):
    cert = Cert.query.get_or_404(id)
    db.session.delete(cert)
    db.session.commit()
    return jsonify(cert_schema.dump(cert))