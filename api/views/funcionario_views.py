from flask_jwt_extended import jwt_required
from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from ..schemas import funcionario_schema
from ..entidades import funcionario
from ..services import funcionario_service
from ..pagination import paginate
from ..models.funcionario_model import Funcionario

class FuncionarioList(Resource):
    @jwt_required
    def get(self):
        fs = funcionario_schema.FuncionarioSchema(many=True)
        return make_response(paginate(Funcionario, fs), 200)
    
    def post(self):
        fs = funcionario_schema.FuncionarioSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        
        nome = request.json['nome']
        idade = request.json['idade']
        funcionario_novo = funcionario.Funcionario(nome=nome, idade=idade)
        result = funcionario_service.cadastrar_funcionario(funcionario_novo)
        return make_response(fs.jsonify(result), 200)

class FuncionarioDetail(Resource):
    @jwt_required
    def get(self, id):
        funcionario = funcionario_service.listar_funcionario_id(id)
        if funcionario is None:
            return make_response(jsonify('Funcionário não encontrado'), 404)
        
        fs = funcionario_schema.FuncionarioSchema()
        return make_response(fs.jsonify(funcionario), 200)
    
    def put(self, id):
        funcionario_bd = funcionario_service.listar_funcionario_id(id)
        if funcionario_bd is None:
            return make_response(jsonify('Funcionário não encontrado'), 404)
        
        nome = request.json['nome']
        idade = request.json['idade']
        funcionario_novo = funcionario.Funcionario(nome=nome, idade=idade)
        funcionario_service.editar_funcionario(funcionario_bd, funcionario_novo)
        funcionario_atualizado = funcionario_service.listar_funcionario_id(id)
        fs = funcionario_schema.FuncionarioSchema()
        return make_response(fs.jsonify(funcionario_atualizado), 200)
    
    def delete(self, id):
        funcionario_bd = funcionario_service.listar_funcionario_id(id)
        if funcionario_bd is None:
            return make_response(jsonify('Funcionário não encontrado'), 404)
        
        funcionario_service.remover_funcionario(funcionario_bd)
        return make_response('', 204)

api.add_resource(FuncionarioList, '/funcionarios')
api.add_resource(FuncionarioDetail, '/funcionarios/<int:id>')

