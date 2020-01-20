from app.models.shared import db, ma

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(10), nullable=False)

def __init__(self, name, price):
    self.name = name
    self.price = price


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price')

# Initialise schema for single object
product_schema = ProductSchema()
# Initialise schema for collections
products_schema = ProductSchema(many=True)