
from app.models.shared import db
from app.models.product import Product, product_schema, products_schema

class ProductPostService:

    def __init__(self, data, db_session=None):
        self.data = data
        self.db_session = db_session or db.session

    def post(self):
        new_product = Product(name=self.data['name'], price=self.data['price'])
        self.db_session.add(new_product)
        self.db_session.commit()
        return new_product
