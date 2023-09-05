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
    amount = 0
    silver_spend = 0
    for history in json["MarketHistories"][1:]:  # Первое значение за неполный отрезок, не нужно
        if i % 4 == 0:  # Сутки за 4 отрезка
            price = silver_spend / amount / 10000
            date = datetime.now().date() - timedelta(days=i // 4)
            sales_by_day = models.SalesByDay(item.item_type_id, quality_level, location_id, price, amount, date.strftime('%d.%m.%Y'))
            db.session.add(sales_by_day)
            if i > 13:
                break
        else:
            amount += history["ItemAmount"]
            silver_spend += history["SilverAmount"]
        i += 1

    db.session.commit()
