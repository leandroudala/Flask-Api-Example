from api import api
from flask_restful import Resource
from ..schemas.login_schema import LoginSchema
from flask import request, make_response, jsonify
from ..services import usuario_service
from flask_jwt_extended import create_access_token
from datetime import timedelta

class LoginList(Resource):
    def post(self):
        """
        Gera token de acesso
        ---
        parameters:
         - in: body
           name: id
           type: integer
           required: true
        responses:
          200: 
            description: Tarefa que possui o ID enviado
            schema: 
              id: Tarefa
              properties:
                tarefa_id:
                  type: integer
                titulo: 
                  type: string
                descricao:
                  type: string
                data_expiracao:
                  type: string
                projeto:
                  type: string
          
        """
        ls = LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        
        email = request.json['email']
        senha = request.json['senha']
        usuario_bd = usuario_service.listar_usuario(email)
        if usuario_bd and usuario_bd.ver_senha(senha):
            access_token = create_access_token(
                identity=usuario_bd.id,
                expires_delta=timedelta(seconds=60)
            )
            return make_response(jsonify({
                'access_token': access_token, 
                'message': 'Login realizado com sucesso!'
            }), 200)
        else:
            return make_response(jsonify({
                'message': 'Crendenciais inválidas'
            }), 401)

api.add_resource(LoginList, '/login')