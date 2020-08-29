from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib
import numpy as np
import sys

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Breast Cancer Cell Classifier", 
		  description = "Classify whether a breast tumor is cancerous ")

name_space = app.namespace('diagnosis', description='Diagnosis APIs')

model = app.model('Diagnosis params', 
				  {'radius': fields.Float(required = True, 
				  							   description="Cell Radius", 
    					  				 	   help="Cell Radius cannot be blank")})