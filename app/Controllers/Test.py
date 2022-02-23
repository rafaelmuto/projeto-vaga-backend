from app import app, api, Resource


@app.route("/test/<string:param>", methods=['GET'])
def parameter(param: str):
    return {
        'parameter': param
    }, 201

@api.route("/api/test/<string:id>")
@api.doc(params={'id': 'GET YOUR ID!'})
class testApi(Resource):

    @api.response(200, 'Okey dokey!')
    @api.response(500, 'no go... =(')
    def get(self, id=None):
        return {
            'test': 'test',
            'id': id
            }, 200

    

@api.route("/api/test")
class testApiNoId(Resource):
    def get(self):
        return {
            'test': 'no id'
            }, 200

    def post(self):
        return