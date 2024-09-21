from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS
from mecab import MeCab
import os

mecab = MeCab()

app = Flask(__name__)
CORS(app)
api = Api(app)

sentence_args = reqparse.RequestParser()
sentence_args.add_argument('sentence', type=str, required=True, help="Must provide sentence to be parsed")

class ParseSentence(Resource):
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
                "POS": morpheme.feature.pos,
                "expression": morpheme.feature.expression
            }
            formatted.append(morphemeDic)
        jsonResponse = jsonify({"status": 200, "results": formatted, "message": "success"})
        jsonResponse.status_code = 200
        return jsonResponse

api.add_resource(ParseSentence, '/parse')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)