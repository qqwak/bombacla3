from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello world!'

    

class Market(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(25), nullable=False)
    
class Trading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    shop = db.Column(db.String(20), nullable=False, unique=True)
    art = db.Column(db.Integer, nullable=False)
    operation = db.Column(db.String(20), nullable=False)
    n = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
    
class Product(db.Model):
    art = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    provider = db.Column(db.String(20), nullable=False)
    
@app.route("/market_list")
def market_list():
    s = []
    for market in Market.query.all():
        print(market.id, market.area)
        s.append([market.id, market.area])
    return str(s)

@app.route("/trading_list")
def trading_list():
    s = []
    for trading in Trading.query.all():
        print(trading.id, trading.date, trading.shop, trading.art, trading.operation, trading.n, trading.price)
        s.append([trading.id, trading.date, trading.shop, trading.art, trading.operation, trading.n, trading.price])
    return str(s)

@app.route("/product_list")
def product_list():
    s = []
    for product in Product.query.all():
        print(product.art, product.department, product.name, product.unit, product.count, product.provider)
        s.append([product.art, product.department, product.name, product.unit, product.count, product.provider])
    return str(s)


if __name__ == '__main__':
    app.run()
    