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


class MediumPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    tier = db.Column(db.Integer, db.ForeignKey("tier.tier"))
    enhancement = db.Column(db.Integer, db.ForeignKey("enhancement.enh_tier"))
    quality = db.Column(db.Integer, db.ForeignKey("quality.qual_tier"))
    price = db.Column(db.Integer)
    datetime = db.Column(db.Float, nullable=False)
    location = db.Column(db.Integer, db.ForeignKey("location.location"))

    def __init__(self, item_id, tier, enhancement, quality, price, location):
        self.item_id = item_id
        self.tier = tier
        self.enhancement = enhancement
        self.quality = quality
        self.price = price
        self.location = location
        self.datetime = time.time()

    def __repr__(self):
        return '<MediumPrice todo {})>'.format(self.price)
