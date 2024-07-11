
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

snacks = [
    {'name': 'Samosa', 'price': 2.50, 'description': 'A crispy pastry filled with spiced potatoes and peas.'},
    {'name': 'Pakora', 'price': 3.00, 'description': 'A fried vegetable fritter.'},
    {'name': 'Bhel Puri', 'price': 2.00, 'description': 'A puffed rice salad with vegetables and spices.'},
    {'name': 'Chana Masala', 'price': 3.50, 'description': 'A spicy chickpea curry.'},
    {'name': 'Butter Chicken', 'price': 4.00, 'description': 'A creamy tomato-based chicken dish.'}
]

cart = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/snacks')
def snacks():
    return render_template('snacks.html', snacks=snacks)

@app.route('/cart')
def cart():
    return render_template('cart.html', cart=cart)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html', cart=cart)

@app.route('/place-order', methods=['POST'])
def place_order():
    shipping_address = request.form.get('shipping_address')
    payment_info = request.form.get('payment_info')

    # Here we would normally process the order and save it to a database.
    # However, since we don't have a database connection, we'll just simulate the process.

    order_number = '1234567890'

    return render_template('order_confirmation.html', order_number=order_number)

if __name__ == "__main__":
    app.run(debug=True)
