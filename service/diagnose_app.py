from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
import joblib
import numpy as np
import sys

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Breast Cancer Cell Classifier", 
		  description = "Classify whether a breast tumor cell is cancerous ")

name_space = app.namespace('diagnosis', description='Diagnosis APIs')

model = app.model('Diagnosis params', 
				  {'radius': fields.Float(required = True, 
				  							   description="Cell Radius", 
    					  				 	   help="Cell Radius cannot be blank"),
				   'texture': fields.Float(required = True, 
				  							   description="Cell Texture", 
    					  				 	   help="Cell Texture cannot be blank"),					  
				   'perimeter': fields.Float(required = True, 
				  							   description="Cell Perimeter", 
    					  				 	   help="Cell Perimeter cannot be blank"),
				   'area': fields.Float(required = True, 
				  							   description="Cell Area", 
    					  				 	   help="Cell Area cannot be blank"),	
				   'smoothness': fields.Float(required = True, 
				  							   description="Cell Smoothness", 
    					  				 	   help="Cell Smoothness cannot be blank"),
				   'compactness': fields.Float(required = True, 
				  							   description="Cell Compactness", 
    					  				 	   help="Cell Compactness cannot be blank"),								  
				   'concavity': fields.Float(required = True, 
				  							   description="Cell Concavity", 
    					  				 	   help="Cell Concavity cannot be blank"),
				   'concavepoints': fields.Float(required = True, 
				  							   description="Cell Concave Points", 
    					  				 	   help="Cell Concave Points cannot be blank"),					  
				   'symmetry': fields.Float(required = True, 
				  							   description="Cell Symmetry", 
    					  				 	   help="Cell Radius cannot be blank"),
				   'fractaldimensions': fields.Float(required = True, 
				  							   description="Cell Fractal Dimensions", 
    					  				 	   help="Cell Fractal Dimensions cannot be blank")})

classifier = joblib.load('classifier.joblib')

@name_space.route("/")
class MainClass(Resource):

	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	@app.expect(model)		
	def post(self):
		try: 
			formData = request.json
			for k in formData:
				if (formData[k] == ''):
					response = jsonify({
						"statusCode": 200,
						"status": "Could not make diagnosiss",
						"result": "All input values must be filled in",
						"error": "All input values are not filled in"
					})
					response.headers.add('Access-Control-Allow-Origin', '*')
					return response
				try:
					float(formData[k])
				except Exception as error:
					response = jsonify({
						"statusCode": 200,
						"status": "Could not make diagnosis",
						"result": "All input values must be numbers",
						"error": str(error)
					})
					response.headers.add('Access-Control-Allow-Origin', '*')
					return response
			data = [val for val in formData.values()]
			diagnosis = classifier.predict(np.array(data).reshape(1, -1))
			types = { 0: "Benign", 1: "Malignant"}
			response = jsonify({
				"statusCode": 200,
				"status": "Diagnosis made",
				"result": "Diagnosis: " + types[diagnosis[0]]
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			return response
		except Exception as error:
			return jsonify({
				"statusCode": 500,
				"status": "Could not make diagnosis",
				"error": str(error)
			})