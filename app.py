from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database to store orders
orders = []

# Home route to list all orders
@app.route('/')
def index():
    return render_template('index.html', orders=orders)

# Route to add new order
@app.route('/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        product_name = request.form['product_name']
        quantity = request.form['quantity']
        
        # Create an order dictionary
        order = {
            'id': len(orders) + 1,
            'customer_name': customer_name,
            'product_name': product_name,
            'quantity': quantity
        }
        
        # Add order to the orders list
        orders.append(order)
        
        return redirect(url_for('index'))
    
    return render_template('add_order.html')

# Route to edit an order
@app.route('/edit/<int:order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    
    if request.method == 'POST':
        order['customer_name'] = request.form['customer_name']
        order['product_name'] = request.form['product_name']
        order['quantity'] = request.form['quantity']
        
        return redirect(url_for('index'))
    
    return render_template('edit_order.html', order=order)

# Route to delete an order
@app.route('/delete/<int:order_id>')
def delete_order(order_id):
    global orders
    orders = [o for o in orders if o['id'] != order_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
