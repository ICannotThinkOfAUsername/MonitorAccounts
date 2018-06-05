from database import app, db, Account
from config import pa_username

from flask import render_template

import time

@app.route('/')
def dashboard():
    time_file = open('/home/'+pa_username+'/mysite/time.txt', 'r')

    try:
        last_updated = int(time_file.read())
    except:
        return('Error getting integer from time_file')

    if (last_updated < (int(time.time()) - 60)):
        return('Monitoring script is not running!')

    accs = Account.query.order_by(-Account.time).all()

    if (len(accs) < 1):
        return('No accounts found')

    actives = []
    inactives = []
    for acc in accs:
        if (acc.active):
            actives.append((acc.id, acc.name, acc.time))
        else:
            inactives.append((acc.id, acc.name, acc.time))

    return render_template('accounts.html', inactives=inactives, actives=actives)

@app.route('/get/<string:id>')
def get(id):
	query_result = Account.query.get(id)

	if (not query_result):
	    return('ID not in database')

	return('name: <b><u>' + query_result.name + '</u></b> | id: <b><u>' + str(query_result.id) + '</u></b> | latest time: <b><u>' + str(query_result.time) + '</u></b> | is active:  <b><u>' + str(query_result.active) + '</u></b>')

@app.route('/create/<string:name>')
def create(name):
	db.session.add(Account(name=name, time=0, active=False))
	db.session.commit()

	query_result = Account.query.filter_by(name=name).order_by(-Account.id.desc()).first() #gets most recent entry via: filtering by name, reversing order and then calling .first()

	return('CREATED id: <b>' + str(query_result.id) + '</b> | name: <b>' + query_result.name + '</b> | latest time: <b>' + str(query_result.time) + '</b> | is active:  <b><u>' + str(query_result.active) + '</u></b>')

@app.route('/alive/<string:id>')
def alive(id):
	query_result = Account.query.get(id)

	if (not query_result):
	    return('ID not in database')

	query_result.time = int(time.time())
	if not query_result.active:
	    query_result.active = True
	db.session.commit()

	return('latest time has been updated to ' + str(query_result.time) + ' for ' + query_result.name)

@app.route('/delete/<string:id>')
def delete(id):
    acc = Account.query.get(id)

    if (not acc):
        return('ID not in database')
    else:
        name = acc.name
        db.session.delete(acc)
        db.session.commit()
        return('Successfully deleted: ' + name)