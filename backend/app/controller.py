from . import models, app, db
from datetime import datetime, timedelta


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

    i = 1
    sold = 0
    silver_spend = 0
    app.logger.info(f'work with {json["MarketHistories"][1:]}')
    for history in json["MarketHistories"][1:]:  # Первое значение за неполный отрезок, не нужно
        if i % 4 == 0:  # Сутки за 4 отрезка
            price = silver_spend / sold / 10000
            date = datetime.now().date() - timedelta(days=i // 4)
            sales_by_day = models.SalesByDay.query.filter(models.SalesByDay.item_type_id == item.item_type_id,
                                                          models.SalesByDay.quality_level == quality_level,
                                                          models.SalesByDay.location_id == location_id,
                                                          models.SalesByDay.sold_date == date).first()
            if sales_by_day is not None:
                app.logger.info(f'found sales_by_day: {sales_by_day}')
                sales_by_day.price = price
                sales_by_day.sold = sold
                sales_by_day.update_date = datetime.now().date()
                db.session.commit()
            else:
                app.logger.info(f'create new sales_by_day')
                sales_by_day = models.SalesByDay(item.item_type_id, quality_level, location_id, price, sold, date)
                db.session.add(sales_by_day)
                db.session.commit()
            sold = 0
            silver_spend = 0
        else:
            sold += history["ItemAmount"]
            silver_spend += history["SilverAmount"]
        if i > 13:
            break
        i += 1


