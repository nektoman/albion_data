from . import models, app, db


def post_sold_daily_data(json):
    app.logger.info(f'recieved {json}')  # todo

