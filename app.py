from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from flask_cors import CORS
from mecab import MeCab
import os

mecab = MeCab()

app = Flask(__name__)
CORS(app)
api = Api(app)

sentence_args = reqparse.RequestParser()
sentence_args.add_argument('sentence', type=str, required=True, help="Must provide sentence to be parsed")

parseFields = {
    'status':fields.Integer,
    'results':fields.String,
    'message':fields.String,
}

class ParseSentence(Resource):
    @marshal_with(parseFields)
    def post(self):
        args = sentence_args.parse_args()
        parseReq = args['sentence']
        if len(parseReq) == 0:
            abort(400, message="Must provide sentence to be parsed")
        parsed =  mecab.parse(parseReq)
        formatted = []
        for morpheme in parsed:
            morphemeDic = {
                "start": morpheme.span.start,
                "end": morpheme.span.end,
                "text": morpheme.surface,
                "POS": morpheme.feature.pos
            }
            formatted.append(morphemeDic)
        jsonResponse = {"status": 200, "results": str(formatted), "message": "success"}
        return jsonResponse, 200

api.add_resource(ParseSentence, '/parse')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=8080))