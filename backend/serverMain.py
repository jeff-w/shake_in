from flask import Flask
from flask import request
from pymongo import MongoClient

app = Flask(__name__)

dbClient = MongoClient('mongodb://Shake_In:password1@ds047652.mongolab.com:47652/shake_in')
db = dbClient.shake_in
users = db.users


print "got past that"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    	return 'You submitted a post request'
    else:
    	return 'You tried 2 GET'


@app.route('/resume')
def resume():
    try:
        users.insert({ 'username' : 'thomas', 'password' : 'nossl', 'email' : 'test@test.com' })
    except(e):
        print e
    return "Resume Page!!"










if __name__ == '__main__':
    app.run(
    	host=app.config.get("HOST", "0.0.0.0"),
    	port=app.config.get("PORT", 9000))  