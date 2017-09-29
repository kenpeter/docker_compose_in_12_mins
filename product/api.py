# We use flask
from flask import Flask

# Use restful from flask and api
from flask_restful import Resource, Api

# __name__ is this app
app = Flask(__name__)

# Now the app becomes api
api = Api(app)

class Product(Resource):
	def get(self):
		return {
			'products': [
				'Bla', 
				'Ice cream', 
				'Chocolate',
				'Fruit'
			]
		}

api.add_resource(Product, '/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
