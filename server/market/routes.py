from flask import Blueprint, request, jsonify

from server.models import Product
from server import db

market = Blueprint('market', __name__)

@market.route('/api/product/add', methods=['POST'])
def add_product():
    try:
        name = request.json.get('name')
        description = request.json.get('description')
        price = request.json.get('price')
        db.session.add(Product(name=name, desc=description, price=price))
        db.session.commit()
    except: 
            return jsonify(result={
                'message': 'Produkt nie został dodany do bazy, spróbuj później.',
                'category': 'danger'
            })
    return jsonify(result={
        'message': 'Produkt został pomyślnie dodany.',
        'catrgory': 'success'
    })
    
@market.route('/api/product/del/<product_id>')
def remove_product(product_id):
    product = Product.query.filter_by(id=product_id).first_or_404()
    return jsonify(result={
        'message': 'Produkt został usunięty',
        'category': 'info'
    })

@market.route('/api/product/update/<product_id>', methods=['POST'])
def update_product(product_id):
    allowed_fields = ('name', 'desc', 'price')
    product = Product.query.filter_by(id=product_id).first_or_404()

    for field in allowed_fields:
        fieldValue = request.json.get(field)

        if fieldValue is not None:
            setattr(product, field, fieldValue)
            db.session.commit()

    return jsonify(result={
        'message': 'Produkt został zaaktualizowany',
        'info': 'success'
    })

@market.route('/api/products', methods=['GET'])
def products():
    products = Product.query.all()
    data = []
    for product in products:
        data.append(dict(product={
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.desc,
            'add_date': product.add_date.strftime("%Y/%m/%d, %H:%M:%S"),
         }))
    return jsonify(result=data)

