from app.models.shared import db, ma

class Product(db.Model):
    __tablename__ = 'products'
    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

def __init__(self, code, name, price):
    self.name = name
    self.price = price
    self.qty = qty

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('code', 'name', 'price')

# Initialise schema for single objects
product_schema = ProductSchema()
# Initialise schema for collections
products_schema = ProductSchema(many=True)