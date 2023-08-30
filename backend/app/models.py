from . import db
import time


class Tier(db.Model):
    tier = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Tier {})>'.format(self.tier)


class Enhancement(db.Model):
    enh_tier = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Enhancement {})>'.format(self.enh_tier)


class Quality(db.Model):
    qual_tier = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    def __repr__(self):
        return '<Quality {})>'.format(self.text)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    def __repr__(self):
        return '<Location{})>'.format(self.text)


class ItemType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    def __repr__(self):
        return '<ItemType{})>'.format(self.text)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_type_id = db.Column(db.Integer, db.ForeignKey("item_type.id"))
    text = db.Column(db.String)

    def __repr__(self):
        return '<Item{})>'.format(self.text)


class SalesByDay(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    tier = db.Column(db.Integer, db.ForeignKey("tier.tier"))
    enhancement = db.Column(db.Integer, db.ForeignKey("enhancement.enh_tier"))
    quality = db.Column(db.Integer, db.ForeignKey("quality.qual_tier"))
    location = db.Column(db.Integer, db.ForeignKey("location.location"))
    price = db.Column(db.Integer)
    sold = db.Column(db.Integer)
    sold_date = db.Column(db.Float, nullable=False)
    update_date = db.Column(db.Float, nullable=False)

    def __init__(self, item_id, tier, enhancement, quality, location, price, sold, sold_date):
        self.item_id = item_id
        self.tier = tier
        self.enhancement = enhancement
        self.quality = quality
        self.location = location
        self.price = price
        self.sold = sold
        self.sold_date = sold_date
        self.update_date = time.time()  # todo date

    def __repr__(self):
        return f'<SalesByDay {self.id})>'
