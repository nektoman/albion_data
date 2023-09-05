from . import db
from datetime import datetime


class Enchantment(db.Model):
    enchantment_level = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Enchantment {})>'.format(self.enchantment_level)


class Quality(db.Model):
    quality_level = db.Column(db.Integer, primary_key=True)

    def __init__(self, quality_level):
        self.quality_level = quality_level

    def __repr__(self):
        return '<Quality {})>'.format(self.text)


class Location(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    def __repr__(self):
        return '<Location{})>'.format(self.text)


class Item(db.Model):
    item_type_id = db.Column(db.String, primary_key=True)
    albion_id = db.Column(db.Integer)
    enchantment_level = db.Column(db.Integer, db.ForeignKey("enchantment.enchantment_level"))
    tier = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Item{})>'.format(self.item_type_id)


class SalesByDay(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_type_id = db.Column(db.String, db.ForeignKey("item.item_type_id"))
    quality_level = db.Column(db.Integer, db.ForeignKey("quality.quality_level"))
    location_id = db.Column(db.Integer, db.ForeignKey("location.location_id"))
    price = db.Column(db.Integer)
    sold = db.Column(db.Integer)
    sold_date = db.Column(db.Date, nullable=False)
    update_date = db.Column(db.Date, nullable=False)

    def __init__(self, item_type_id, quality_level, location_id, price, sold, sold_date):
        self.item_type_id = item_type_id
        self.quality_level = quality_level
        self.location_id = location_id
        self.price = price
        self.sold = sold
        self.sold_date = sold_date
        self.update_date = datetime.now().date()


    def __repr__(self):
        return f'<SalesByDay {self.id})>'
