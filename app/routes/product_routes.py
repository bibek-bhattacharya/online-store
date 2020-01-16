
from flask import request, jsonify, Blueprint
from app.models.shared import db
from app.models.product import Product, product_schema, products_schema

product_api = Blueprint('product_api', __name__)

# Create a product
@product_api.route('/product', methods=['POST'])
def add_product():
    code = request.json['code']
    name = request.json['name']
    price = request.json['price']


    new_product = Product(code=code, name=name, price=price)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Update a product by code
@product_api.route('/product/<code>', methods=['PUT'])
def update_product(code):
    
    product_to_update = Product.query.get(code)
    product_to_update.name = request.json['name']
    product_to_update.price = request.json['price']

    db.session.commit()

    return product_schema.jsonify(product_to_update)

# Delete a product by code
@product_api.route('/product/<code>', methods=['DELETE'])
def delete_product(id):
    
    product_to_delete = Product.query.get(id)
    db.session.delete(product_to_delete)
    db.session.commit()

    return product_schema.jsonify(product_to_delete)

# Get all products
@product_api.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

#Get single product
@product_api.route('/product/<code>', methods=['GET'])
def get_product(code):
    product = Product.query.get(code)
    return product_schema.jsonify(product)
