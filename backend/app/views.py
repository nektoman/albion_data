from . import app
from .controller import post_sold_daily_data
from flask import Response, jsonify, request
import traceback
from .CONST import ResponseStatus as rs


@app.route('/')
def index():
    return "<p>Hello!</p>"



@app.route('/sold_daily/marketorders.ingest', methods=['POST'])
def sold_daily_marketorders():
    try:
        app.logger.info('marketorders')
        app.logger.info(f'recieved {request.get_json()}')  # todo
        return Response('', rs.OK_200)
    except Exception as err:
        app.logger.info(str(err) + '\n' + traceback.format_exc())
        return Response(str(err), status=rs.INTERNAL_SERVER_ERROR_500)


@app.route('/sold_daily/markethistories.ingest', methods=['POST'])
def sold_daily_markethistories():
    try:
        app.logger.info('markethistories')
        post_sold_daily_data(request.get_json())
        return Response('', rs.OK_200)
    except Exception as err:
        app.logger.info(str(err) + '\n' + traceback.format_exc())
        return Response(str(err), status=rs.INTERNAL_SERVER_ERROR_500)