from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Otavio',
        'habilidades':['Python','Flask']
    },
    {
        'id':'1',
        'nome': 'Bitencourt',
        'habilidades': ['Python', 'Flask']
     }
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor (id):
    if request.method == 'GET':
        desenvolvedor = desenvolvedores[id]
        print(desenvolvedor)
        return jsonify(desenvolvedor)
    elif requets.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif requets.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluido'})

#Lista todos os desenvolvedores e inclui um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores(posicao))
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)