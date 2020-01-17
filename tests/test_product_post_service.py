import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from app.service.product_post_service import ProductPostService 
from unittest.mock import MagicMock

def test_ProductPostService_can_init():
    session = MagicMock()
    json_data={'name': 'Lavender heart', 'price': '9.25'}
    service = ProductPostService(data=json_data, db_session=session)
    assert service.db_session is session
    assert service.data is json_data

def test_ProductPostService_can_post():
    session = MagicMock()
    service = ProductPostService(data={'name': 'Lavender heart', 'price': '9.25'}, db_session=session)
    product = service.post()
    assert product.name == 'Lavender heart'
    assert product.price == '9.25'
