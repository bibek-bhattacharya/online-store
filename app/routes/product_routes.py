
from flask import request, abort, jsonify, Blueprint
from app.models.shared import db
from app.models.product import Product, product_schema, products_schema
from app.service.product_post_service import ProductPostService 

product_api = Blueprint('product_api', __name__)

# Create a product
@product_api.route('/product', methods=['POST'])
def add_product():

    data = request.get_json()
    name = data.get('name', '')
    price = data.get('price', '')

    if not name:
        abort(400, description="Missing name")
    
    if not price:    
        abort(400, description="Missing price")

    service = ProductPostService(data, db.session)
    return product_schema.jsonify(service.post())

# Update a product by id
@product_api.route('/product/<id>', methods=['PUT'])
def update_product(id):
    
    product_to_update = Product.query.get(id)
    if product_to_update is None:
        abort(404, description="Resource not found")
    
    data = request.get_json()
    name = data.get('name', '')
    price = data.get('price', '')

    if not name and not price:
        abort(400, description="Missing name or price to update")
        
    if name:
        product_to_update.name = name
    
    if price:    
        product_to_update.price = price

    db.session.commit()

    return product_schema.jsonify(product_to_update)

# Delete a product by id
@product_api.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    
    product_to_delete = Product.query.get(id)
    if product_to_delete is None:
        abort(404, description="Resource not found")

    db.session.delete(product_to_delete)
    db.session.commit()

    return product_schema.jsonify(product_to_delete)

# Get all products
@product_api.route('/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

#Get single product
@product_api.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    
    if product is None:
        abort(404, description="Resource not found")
    return product_schema.jsonify(product)
