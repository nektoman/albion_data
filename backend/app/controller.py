from . import models, app, db

def post_sold_daily_data(json):
    print(f'recieved {json}') # todo