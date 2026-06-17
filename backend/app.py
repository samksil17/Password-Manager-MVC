from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Credential
import os

app = Flask(__name__)
CORS(app)

# configuracion de base de datos 
# en Render usa DATABASE_URL; localmente usa SQLite
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///passwords.db')
# Render usa postgres://, SQLAlchemy necesita postgresql://
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


#  RUTAS / ENDPOINTS
@app.route('/credentials', methods=['GET'])
def get_credentials():
    credentials = Credential.query.all()
    return jsonify([c.to_dict() for c in credentials]), 200


@app.route('/credentials', methods=['POST'])
def create_credential():
    data = request.get_json()

    if not data or not data.get('sitio') or not data.get('usuario') or not data.get('password'):
        return jsonify({'error': 'Los campos sitio, usuario y password son obligatorios'}), 400

    new_cred = Credential(
        sitio=data['sitio'],
        usuario=data['usuario'],
        password=data['password'],
        categoria=data.get('categoria', '')
    )
    db.session.add(new_cred)
    db.session.commit()
    return jsonify(new_cred.to_dict()), 201


@app.route('/credentials/<int:id>', methods=['GET'])
def get_credential(id):
    cred = Credential.query.get_or_404(id)
    return jsonify(cred.to_dict()), 200


@app.route('/credentials/<int:id>', methods=['PUT'])
def update_credential(id):
    cred = Credential.query.get_or_404(id)
    data = request.get_json()

    cred.sitio     = data.get('sitio',     cred.sitio)
    cred.usuario   = data.get('usuario',   cred.usuario)
    cred.password  = data.get('password',  cred.password)
    cred.categoria = data.get('categoria', cred.categoria)

    db.session.commit()
    return jsonify(cred.to_dict()), 200


@app.route('/credentials/<int:id>', methods=['DELETE'])
def delete_credential(id):
    cred = Credential.query.get_or_404(id)
    db.session.delete(cred)
    db.session.commit()
    return jsonify({'message': f'Credencial {id} eliminada'}), 200


#  INICIO 
if __name__ == '__main__':
    app.run(debug=True)
