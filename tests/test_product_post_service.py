import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from app.service.product_post_service import ProductPostService 
from app.service.product_put_service import ProductPutService
from app.models.product import Product, product_schema
from unittest.mock import MagicMock

def test_ProductPostService_can_post():
    session = MagicMock()
    service = ProductPostService(data={'name': 'Lavender heart', 'price': '9.25'}, db_session=session)
    product = service.post()
    assert product.name == 'Lavender heart'
    assert product.price == '9.25'

def test_ProductPutService_can_put_price():
    session = MagicMock()
    service = ProductPutService(data={'name': 'Lavender heart', 'price': '10.25'}, product=Product(name='Lavender heart', price='9.25'), db_session=session)
    product = service.put()
    assert product.name == 'Lavender heart'
    assert product.price == '10.25'

def test_ProductPutService_can_put_name():
    session = MagicMock()
    service = ProductPutService(data={'name': 'White trainer', 'price': '55.00'}, product=Product(name='Black trainer', price='55.00'), db_session=session)
    product = service.put()
    assert product.name == 'White trainer'
    assert product.price == '55.00'

def test_ProductPutService_can_put_name_and_price():
    session = MagicMock()
    service = ProductPutService(data={'name': 'White trainer', 'price': '50.00'}, product=Product(name='Black trainer', price='55.00'), db_session=session)
    product = service.put()
    assert product.name == 'White trainer'
    assert product.price == '50.00'

