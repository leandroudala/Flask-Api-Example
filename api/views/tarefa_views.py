from flask_jwt_extended import jwt_required
from flask_restful import Resource
from api import api
from ..schemas import tarefa_schema
from flask import request, make_response, jsonify
from ..entidades import tarefa
from ..services import tarefa_service, projeto_service
from ..pagination import paginate
from ..models.tarefa_model import Tarefa

class TarefaList(Resource):
    @jwt_required
    def get(self):
        """
        Listagem de todas as tarefas
        ---
        parameters:
         - in: header
           name: Authorization
           type: string
           required: true
        responses:
          200: 
            description: Lista de todas as tarefas.
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
        ts = tarefa_schema.TarefaSchema(many=True)
        return make_response(paginate(Tarefa, ts), 200)

    def post(self):
        """
        Esta rota é responsável por cadastrar uma nova tarefa.
        ---
        parameters: 
         - in: body
           name: Tarefa
           description: Criar nova tarefa
           schema: 
            type: object
            required: 
              - titulo
              - descricao
              - data_expiracao
              - projeto
            properties:
              titulo: 
                type: string
              descricao:
                type: string
              data_expiracao:
                type: string
              projeto:
                type: string
        responses:
          201: 
            description: Tarefa criada com sucesso.
            schema: 
              id: Tarefa
              properties: 
                titulo: 
                  type: string
                descricao:
                  type: string
                data_expiracao:
                  type: string
                projeto:
                  type: string
          
        """
        ts = tarefa_schema.TarefaSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            descricao = request.json['descricao']
            data_expiracao = request.json['data_expiracao']
            projeto = request.json['projeto']
            projeto_tarefa = projeto_service.listar_projeto_id(projeto)

            if projeto_tarefa is None:
                return make_response(jsonify('Projeto não encontrado'), 404)

            tarefa_nova = tarefa.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, projeto=projeto_tarefa)
            result = tarefa_service.cadastrar_tarefa(tarefa_nova)
            return make_response(ts.jsonify(result), 201)

class TarefaDetail(Resource):
    @jwt_required
    def get(self, id):
        """
        Retorna a tarefa que possui o ID como parâmetro
        ---
        parameters:
         - in: header
           name: Authorization
           type: string
           required: true
         - in: path
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
        tarefa = tarefa_service.listar_tarefa_id(id)
        if tarefa is None:
            return make_response(jsonify("Tarefa não encontrada"), 404)

        ts = tarefa_schema.TarefaSchema()
        return make_response(ts.jsonify(tarefa), 200)
    
    def put(self, id):
        tarefa_bd = tarefa_service.listar_tarefa_id(id)
        # verificando se tabela existe
        if tarefa_bd is None:
            return make_response(jsonify("Tarefa não encontrada"), 404)
        
        ts = tarefa_schema.TarefaSchema()
        validate = ts.validate(request.json)
        # verificando se dados da tarefa são válidos
        if validate:
            return make_response(jsonify(validate), 400)
        # capturando parametros
        titulo = request.json['titulo']
        descricao = request.json['descricao']
        data_expiracao = request.json['data_expiracao']
        projeto = request.json['projeto']
        projeto_bd = projeto_service.listar_projeto_id(projeto)
        if projeto_bd is None:
            return make_response(jsonify('Projeto não encontrado'), 404)

        # criando objeto com parametros
        tarefa_nova = tarefa.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, projeto=projeto_bd)
        tarefa_service.editar_tarefa(tarefa_bd, tarefa_nova)
        tarefa_atualizada = tarefa_service.listar_tarefa_id(id)
        # retornando 
        return make_response(ts.jsonify(tarefa_atualizada), 200)

    
    def delete(self, id):
        tarefa_bd = tarefa_service.listar_tarefa_id(id)
        if tarefa_bd is None:
            return make_response(jsonify('Tarefa não encontrada'), 404)
        tarefa_service.remover_tabela(tarefa_bd)
        return make_response('', 204)


api.add_resource(TarefaList, '/tarefas')
api.add_resource(TarefaDetail, '/tarefas/<int:id>')