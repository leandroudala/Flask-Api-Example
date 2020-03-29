from api import db
from sqlalchemy.dialects.mysql import INTEGER

class Funcionario(db.Model):
    __tablename__ = 'funcionario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(INTEGER(unsigned=True), nullable=False)

    projetos = db.relationship('Projeto', secondary="funcionario_projeto", back_populates="funcionarios")