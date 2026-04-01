from flask import Flask, jsonify, request

app = Flask(__name__)

accounts = []

@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.json
    accounts.append(data)
    return jsonify(data), 201

@app.route('/accounts', methods=['GET'])
def list_accounts():
    return jsonify(accounts), 200

@app.route('/accounts/<int:index>', methods=['GET'])
def read_account(index):
    return jsonify(accounts[index]), 200

@app.route('/accounts/<int:index>', methods=['PUT'])
def update_account(index):
    accounts[index] = request.json
    return jsonify(accounts[index]), 200

@app.route('/accounts/<int:index>', methods=['DELETE'])
def delete_account(index):
    accounts.pop(index)
    return '', 204