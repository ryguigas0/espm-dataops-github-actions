from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(app, title='Calculadora', version='1.0', description='API de calculadora', doc='/swagger')

operator_ns = api.namespace('/', description='Operadores disponiveis para calcular')

operator_model = operator_ns.model('BinaryOperator', {
    'a': fields.Fixed(decimals=3),
    'b': fields.Fixed(decimals=3)
})

# curl -X POST -H 'Content-Type: application/json' --data '{"a": 3, "b": 4}' http://localhost:3000/soma
@operator_ns.route('/soma')
class Soma(Resource):
    @operator_ns.marshal_with(operator_model, code=200)
    def post(self):
        a = api.payload['a']
        b = api.payload['b']
        return {'message': a + b}

# curl -X POST -H 'Content-Type: application/json' --data '{"a": 3, "b": 4}' http://localhost:3000/multiplicacao
@operator_ns.route('/multiplicacao')
class Multiplicacao(Resource):
    @operator_ns.marshal_with(operator_model, code=200)
    def post(self):
        a = api.payload['a']
        b = api.payload['b']
        return {'message': a * b}

if __name__ == '__main__':
    app.run(debug=True, port=3000)
