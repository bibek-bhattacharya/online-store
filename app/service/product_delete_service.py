
from app.models.shared import db
from app.models.product import Product, product_schema

class ProductDeleteService:

    def __init__(self, product, db_session=None):
        self.product = product
        self.db_session = db_session or db.session

    def delete(self):

        self.db_session.delete(self.product)
        self.db_session.commit()

        return self.product
