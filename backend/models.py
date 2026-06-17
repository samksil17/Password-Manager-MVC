from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Credential(db.Model):
    __tablename__ = 'credentials'

    id        = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sitio     = db.Column(db.String(100), nullable=False)
    usuario   = db.Column(db.String(100), nullable=False)
    password  = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            'id':        self.id,
            'sitio':     self.sitio,
            'usuario':   self.usuario,
            'password':  self.password,
            'categoria': self.categoria or ''
        }
