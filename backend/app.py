import os
from datetime import datetime
from pymongo import MongoClient
from models import db, Credential
from flask_cors import CORS
from flask import Flask, request, jsonify
cat > /mnt/user-data/outputs/app.py << 'EOF'

app = Flask(__name__)
CORS(app)

#  BASE DE DATOS RELACIONAL (PostgreSQL / SQLite) via SQLAlchemy
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///passwords.db')
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

#  BASE DE DATOS NO RELACIONAL (MongoDB Atlas) via PyMongo
MONGO_URL = os.environ.get('MONGO_URL', 'mongodb://localhost:27017/')
mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client['password_manager']
logs = mongo_db['logs']   # colección de auditoría


def registrar_log(accion, datos):
    """Registra cada operación CRUD en MongoDB como auditoría."""
    logs.insert_one({
        'accion':    accion,          # 'CREAR', 'ACTUALIZAR', 'ELIMINAR'
        'datos':     datos,           # qué se modificó
        'timestamp': datetime.utcnow()
    })


#  ENDPOINTS

# GET /credentials → listar todas las credenciales
@app.route('/credentials', methods=['GET'])
def get_credentials():
    credentials = Credential.query.all()
    return jsonify([c.to_dict() for c in credentials]), 200


# POST /credentials → crear nueva credencial
@app.route('/credentials', methods=['POST'])
def create_credential():
    data = request.get_json()

    if not data or not data.get('sitio') or not data.get('usuario') or not data.get('password'):
        return jsonify({'error': 'Los campos sitio, usuario y password son obligatorios'}), 400

    nueva = Credential(
        sitio=data['sitio'],
        usuario=data['usuario'],
        password=data['password'],
        categoria=data.get('categoria', '')
    )
    db.session.add(nueva)
    db.session.commit()

    # Registro en MongoDB
    registrar_log('CREAR', {
        'id':       nueva.id,
        'sitio':    nueva.sitio,
        'usuario':  nueva.usuario,
        'categoria': nueva.categoria
    })

    return jsonify(nueva.to_dict()), 201


# GET /credentials/<id> → obtener una credencial
@app.route('/credentials/<int:id>', methods=['GET'])
def get_credential(id):
    cred = Credential.query.get_or_404(id)
    return jsonify(cred.to_dict()), 200


# PUT /credentials/<id> → actualizar credencial
@app.route('/credentials/<int:id>', methods=['PUT'])
def update_credential(id):
    cred = Credential.query.get_or_404(id)
    data = request.get_json()

    cred.sitio = data.get('sitio',     cred.sitio)
    cred.usuario = data.get('usuario',   cred.usuario)
    cred.password = data.get('password',  cred.password)
    cred.categoria = data.get('categoria', cred.categoria)

    db.session.commit()

    # Registro en MongoDB
    registrar_log('ACTUALIZAR', {
        'id':       cred.id,
        'sitio':    cred.sitio,
        'usuario':  cred.usuario,
        'categoria': cred.categoria
    })

    return jsonify(cred.to_dict()), 200


# DELETE /credentials/<id> → eliminar credencial
@app.route('/credentials/<int:id>', methods=['DELETE'])
def delete_credential(id):
    cred = Credential.query.get_or_404(id)

    # Registro en MongoDB antes de eliminar
    registrar_log('ELIMINAR', {
        'id':      cred.id,
        'sitio':   cred.sitio,
        'usuario': cred.usuario
    })

    db.session.delete(cred)
    db.session.commit()
    return jsonify({'message': f'Credencial {id} eliminada'}), 200


# GET /logs → ver historial de auditoría desde MongoDB
@app.route('/logs', methods=['GET'])
def get_logs():
    historial = list(logs.find({}, {'_id': 0}).sort('timestamp', -1).limit(50))
    for log in historial:
        log['timestamp'] = log['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
    return jsonify(historial), 200


# ─── INICIO ───────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)
EOF
echo "OK"
