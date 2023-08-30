from . import app
from .controller import post_sold_daily_data
from flask import Response, jsonify, request
import traceback
from .CONST import ResponseStatus as rs


@app.route('/')
def index():
    return "<p>Hello!</p>"


@app.route('/sold_daily', methods=['POST'])
def create_payment():
    try:
        post_sold_daily_data(request.get_json())
        return Response('', rs.OK_200)
    except Exception as err:
        print(str(err) + '\n' + traceback.format_exc())
        return Response(str(err), status=rs.INTERNAL_SERVER_ERROR_500)
