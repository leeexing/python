from flask import Flask, request
from flask_restplus import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app, prefix='/v1', version='2.0', title='Test', description='Test restful api ...')
app.config['ERROR_404_HELP'] = False

users = {
    '1': 'leeing',
    '2': 'nanam'
}

parser = reqparse.RequestParser()
parser.add_argument('userName', type=str, required=True)

@api.route('/hello/<int:user_id>', endpoint='user')
class HelloWorld(Resource):
    def get(self, user_id):
        print('----', user_id)
        return {'hello': 'world'}

    def put(self, user_id):
        args = parser.parse_args(strict=True)
        print(args, '++++')
        return {'userName': 'leeing'}

    def delete(self):
        return 'it has deleted !!!'

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()