
from app.models.shared import db
from app.models.product import Product, product_schema

class ProductPutService:

    def __init__(self, data, product, db_session=None):
        self.data = data
        self.product = product
        self.db_session = db_session or db.session

    def put(self):

        name = self.data.get('name', '')
        price = self.data.get('price', '')
        if name:
            self.product.name = name
    
        if price:    
            self.product.price = price

        self.db_session.commit()

        return self.product
