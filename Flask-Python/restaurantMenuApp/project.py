from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem 

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

#decorator : takes in a argument and returns a replacement function
@app.route('/restaurant/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
	return render_template('menuItem.html', restaurant=restaurant, items = items)

@app.route('/restaurant/<int:restaurant_id>/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
	if request.method == 'POST':
		newItem = MenuItem(name = request.form['name'], restaurant_id=restaurant_id)
		session.add(newItem)
		session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
	else:
		return render_template('newmenuitem.html', rId = restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
	updateItem = session.query(MenuItem).filter_by(id = menu_id).one()
	if request.method == 'POST':
		if request.form['name']:
			updateItem.name = request.form['name']
			session.add(updateItem)
			session.commit()
			flash("Menu item has been edited")
			return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
	else:
		return render_template('editMenuItem.html', rId = restaurant_id, item=updateItem)

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Menu Item has been deleted")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item=itemToDelete)

#API endpoint for returning menu
@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def returnMenuJson(restaurant_id):
	menuItem = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
	return jsonify(MenuItems=[i.serialize for i in menuItem])

@app.route('/restaurant/<int:restaurant_id>/menu/<menu_id>/JSON')
def returnJson(restaurant_id, menu_id):
	item = session.query(MenuItem).filter_by(id=menu_id, restaurant_id=restaurant_id).one()
	return jsonify(MenuItems=item.serialize)
    
if __name__ == '__main__':
	app.secret_key = 'super_secret_key' 
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)

