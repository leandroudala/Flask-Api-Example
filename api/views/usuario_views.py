from flask_jwt_extended import jwt_required
from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service
from ..models.usuario_model import Usuario

class UsuarioList(Resource):
    @jwt_required
    def post(self):
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify('Usuário não encontrado'), 404)
        
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        
        usuario_novo = usuario.Usuario(nome=nome, email=email, senha=senha)
        result = usuario_service.cadastrar_usuario(usuario_novo)
        return make_response(us.jsonify(result), 201)

api.add_resource(UsuarioList, '/usuarios')
