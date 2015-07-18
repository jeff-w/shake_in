from flask import Flask
from flask import request
from pymongo import MongoClient
from util import *

app = Flask(__name__)

dbClient = MongoClient('mongodb://Shake_In:password1@ds047652.mongolab.com:47652/shake_in')
db = dbClient.shake_in
users = db.users
recruiters = db.recruiters


print "got past that"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    	return 'You submitted a post request'
    else:
    	return 'You tried 2 GET'


@app.route('/resume')
def resume():
    res = None
    try:
        res = addUser(users, recruiters, "tom", "manzini", "123", "1234@1234.com", "12345678901", "RPI", "BS", "1.0", "coding n shit")
    except(e):
        print e
    return str(res))
    
if __name__ == '__main__':
    app.run(
    	host=app.config.get("HOST", "0.0.0.0"),
    	port=app.config.get("PORT", 9000))  