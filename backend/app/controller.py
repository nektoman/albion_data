from . import models, app, db
from datetime import datetime, timedelta


def _modify_sales_by_day(item_type_id, quality_level, location_id, date, price, sold):
    sales_by_day = models.SalesByDay.query.filter(models.SalesByDay.item_type_id == item_type_id,
                                                  models.SalesByDay.quality_level == quality_level,
                                                  models.SalesByDay.location_id == location_id,
                                                  models.SalesByDay.sold_date == date).first()
    if sales_by_day is not None:
        #  Если такой уже есть - обновить
        app.logger.info(f'found sales_by_day: {sales_by_day}')
        sales_by_day.price = price
        sales_by_day.sold = sold
        sales_by_day.update_date = datetime.now().date()
        db.session.commit()
    else:
        #  Если такого нет - создать
        app.logger.info(f'create new sales_by_day')
        sales_by_day = models.SalesByDay(item_type_id, quality_level, location_id, price, sold, date)
        db.session.add(sales_by_day)
        db.session.commit()
    pass


def _timestamp_to_seconds(timestamp):
    return int(timestamp / 10000000)


def post_sold_daily_data(json):
    app.logger.info(f'recieved {json}')
    item = models.Item.query.filter(models.Item.albion_id == int(json["AlbionId"])).first()
    if item is None:
        return

    quality_level = json.get("QualityLevel")
    location_id = json.get("LocationId")

    if json["Timescale"] == 0:
        return
    elif json["Timescale"] == 1:
        pass
    else:  # json["Timescale"] == 2
        return

    day = 0
    sold = 0
    silver_spend = 0
    histories = json.get("MarketHistories")
    if len(histories) == 0:
        return
    start_timestamp = _timestamp_to_seconds(histories[0].get("Timestamp"))

    app.logger.info(f'work with {histories[1:]}')

    for history in histories[1:]:  # Первое значение за неполный отрезок, не нужно
        app.logger.info(f'stamp: {_timestamp_to_seconds(history["Timestamp"]) - start_timestamp}')
        if _timestamp_to_seconds(history["Timestamp"]) - start_timestamp < -86400:  # На сутки назад
            _modify_sales_by_day(item.item_type_id,
                                 quality_level,
                                 location_id,
                                 datetime.now().date() - timedelta(days=day),
                                 silver_spend / sold / 10000,
                                 sold)
            start_timestamp = _timestamp_to_seconds(history["Timestamp"])
            day += 1
            sold = 0
            silver_spend = 0
            if day >= 3:  # Только последние 3 дня
                break
        else:
            sold += history["ItemAmount"]
            silver_spend += history["SilverAmount"]
