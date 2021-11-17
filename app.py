import requests
from flask import Flask, request, jsonify

app = Flask(__name__)#Cria a aplicação Flask

produtos = [{"id":"0","nome":"Lapis","preço":10}]#Dados locais

@app.route('/produtos_resgistrados', methods=['GET'])#Mostra todas as produtos registrados
def get():
    return jsonify({"produtos registradas":produtos})

@app.route('/produtos/<string:name>', methods=['GET'])#Mostra um produto especifico atraves do seu ID
def get1(name):
    produto = [produto for produto in produtos if produto['id'] == name]
    return jsonify({"produtos registradas":produto[0]})

@app.route('/produtos', methods=['POST'])#Adiciona um novo produto passando seu ID, nome e preço
def post():
    nova_produto = {'id':request.json['id'],'nome':request.json['nome'],'preço':request.json['preço']}
    produtos.append(nova_produto)
    return jsonify({'produtos registradas': produtos})

@app.route('/produtos/<string:name>',methods=['DELETE'])#Deleta uma produto passando seu ID
def delete(name):
    produto_deletado = [produto for produto in produtos if produto['id'] == name]
    produtos.remove(produto_deletado[0])
    return jsonify({'produtos registradas': produtos})

if __name__ == "__main__":
    app.run(debug=True)