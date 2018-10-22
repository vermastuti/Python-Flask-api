# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:12:50 2018

@author: stuti.verma
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse

app=Flask(__name__)
api=Api(app)
    
class CreateUser(Resource):
    def post(self):
        try:
            #Parse the arguments
            parser=reqparse.RequestParser()
            parser.add_argument('email', type=str, help='email address to create user')
            parser.add_argument('password', type=str, help='password to create user')
            args=parser.parse_args()
            
            _userEmail=args['email']
            _userPassword=args['password']
            
            return {'email': args['email'],  'password':args['password'] }
            
        except Exception as e:
            return {'error': str(e)}
        #return{'status':'success'}
        
api.add_resource(CreateUser,'/CreateUser')

if __name__=='__main__':
    app.run(debug=True)
    
    
