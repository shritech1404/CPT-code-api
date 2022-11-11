from flask import Flask,request
import sqlite3
from flask_restful import Api, Resource, reqparse
from fuzzywuzzy import fuzz


app = Flask(__name__)
app.secret_key = 'shri'
api = Api(app) ## make api using flask_restful
#jwt = JWT(app, authenticate, identity)  ## /auth (endpoint)

def response(success, status_code, data, message=None):
    #data.sort(key=lambda e: e['data']['score'], reverse=True)
    return ({
            "success": success,
            "status_code": status_code,
            "data": data,
            "message": message
        })


class Code(Resource):
    #@jwt_required()
    def get(self, des):
        item = Code.find_by_desription(des)
        if item:
            return item
        return {"message":"given named Porcedure dosen't match any procedure!"}, 400

    @classmethod
    def find_by_desription(cls, des):
        
        connection = sqlite3.connect('cpt.db')
        cursor = connection.cursor()
        desc = f"%{des}%"
        query = "SELECT * FROM cprcode WHERE cate_proc2 LIKE ?"
        result1 = cursor.execute(query, (desc,))
        result = result1.fetchall()
        connection.close()
        #print(result)
        res = result.copy()
        data = []
        for rows in res:
            score=fuzz.WRatio(des, rows[4])
            data.append({"CategaryCode":rows[1], "CategoryName":rows[2], "CPTCode":rows[3], "matchedDescription":rows[4], "score":float(score)})
        #data= {"result":results}
        #data.sort(key=lambda e: e['key']['subkey'], reverse=True)
        if data != []:
            return response(True, 200, data)
        return response(False, 404, None, "given named Porcedure dosen't match any procedure!"), 404



## add endpoints
api.add_resource(Code, '/code/<string:des>') 


if __name__=='__main__':
    app.run(port=8000, debug=True)