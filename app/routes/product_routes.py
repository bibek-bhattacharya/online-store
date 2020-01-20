
from flask import request, abort, jsonify, Blueprint
from app.models.shared import db
from app.models.product import Product, product_schema, products_schema
from app.service.product_post_service import ProductPostService
from app.service.product_put_service import ProductPutService
from app.service.product_delete_service import ProductDeleteService

product_api = Blueprint('product_api', __name__)

# Create a product
@product_api.route('/product', methods=['POST'])
def add_product():

    req_data = request.get_json()
    name = req_data.get('name', '')
    price = req_data.get('price', '')

    if not name:
        abort(400, description="Missing name")
    
    if not price:    
        abort(400, description="Missing price")

    postService = ProductPostService(req_data, db.session)
    return product_schema.jsonify(postService.post())

# Update a product by id
@product_api.route('/product/<id>', methods=['PUT'])
def update_product(id):
    
    product_to_update = Product.query.get(id)

    if product_to_update is None:
        abort(404, description="Resource not found")
    
    req_data = request.get_json()
    name = req_data.get('name', '')
    price = req_data.get('price', '')

    if not name and not price:
        abort(400, description="Missing name or price to update")

    putService = ProductPutService(req_data, product_to_update, db.session)
    return product_schema.jsonify(putService.put())

# Delete a product by id
@product_api.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    
    product_to_delete = Product.query.get(id)
    
    if product_to_delete is None:
        abort(404, description="Resource not found")

    deleteService = ProductDeleteService(product_to_delete, db.session)
    return product_schema.jsonify(deleteService.delete())

#Get single product
@product_api.route('/product/<id>', methods=['GET'])
def get_product(id):
    
    product = Product.query.get(id)
    
    if product is None:
        abort(404, description="Resource not found")
    
    return product_schema.jsonify(product)

# Get all products
@product_api.route('/products', methods=['GET'])
def get_products():

    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    
    return products_schema.jsonify(result)


