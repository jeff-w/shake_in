import json
from flask import Flask
from flask import request
from flask import abort, redirect, url_for
from pymongo import MongoClient
from util import *
from shakeUtil import *

app = Flask(__name__)

dbClient = MongoClient('mongodb://Shake_In:password1@ds047652.mongolab.com:47652/shake_in')
db = dbClient.shake_in
users = db.users
recruiters = db.recruiters


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Welcome to the Shake\'in backend, dont screw up here.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'login page\n'
    if request.method == 'POST':
        jsonObject = request.get_json()
    
        if 'emailAddress' not in jsonObject or 'password' not in jsonObject:
            return "Malformed request fields\n"
        else:
            requestEmail = jsonObject['emailAddress']
            requestPassword = jsonObject['password']

        loginValidation = validateLogin(users,
                                        recruiters,
                                        requestEmail,
                                        requestPassword)
        loginStatus = loginValidation['result']

        print json.dumps(jsonObject)

        return json.dumps(loginValidation)

@app.route('/applicantShake', methods=['GET', 'POST'])
def applicantShake():
    if request.method == 'GET':
        return 'Welcome back, applicant!\n'
    if request.method == 'POST':
        jsonObject = request.get_json()
        lat = jsonObject['latitude']
        lon = jsonObject['longitude']


        applicantShaker1 = addShaker("applicant1", (float(lat), float(lon)), False)


        return "SUCCESS:POSTed!\n"

@app.route('/recruiterShake', methods=['GET', 'POST'])
def recruiterShake():
    if request.method == 'GET':
        return 'Welcome back, recruiter!\n'
    if request.method == 'POST':
        jsonObject = request.get_json()
        lat = jsonObject['latitude']
        lon = jsonObject['longitude']


        applicantShaker = addShaker("recruiter1", (float(lat), float(lon)), True)
        nearestShakers = getNearestShakers("recruiter1", 50000)

        return json.dumps(nearestShakers['userID'])

@app.route('/applicantSignup', methods=['GET', 'POST'])
def applicantSignup():
    if request.method == 'GET':
        return 'Sign in, applicant!\n'
    if request.method == 'POST':
        jsonObject = request.get_json()
        print json.dumps(jsonObject)

        requestEmailAddress = jsonObject['emailAddress']
        requestPassword = jsonObject['password']
        requestFirstName = jsonObject['firstName']
        requestLastName = jsonObject['lastName']
        requestPhoneNumber = jsonObject['phoneNumber']
        requestSchool = jsonObject['school']
        requestEduLevel = jsonObject['eduLevel']
        requestGPA = jsonObject['GPA']
        requestSkills = jsonObject['skills']

        addUserResponse = addUser(  users,
                                    recruiters,
                                    requestFirstName,
                                    requestLastName, 
                                    requestPassword,
                                    requestEmailAddress,
                                    requestPhoneNumber,
                                    requestSchool,
                                    requestEduLevel,
                                    requestGPA,
                                    requestSkills)

        signupStatus = addUserResponse['result']

        return json.dumps(addUserResponse)
           


@app.route('/recruiterSignup', methods=['GET', 'POST'])
def recruiterSignup():
    if request.method == 'GET':
        return 'Sign in, recruiter!\n'
    if request.method == 'POST':
        jsonObject = request.get_json()
        requestEmailAddress = jsonObject['emailAddress']
        requestPassword = jsonObject['password']
        requestFirstName = jsonObject['firstName']
        requestLastName = jsonObject['lastName']
        requestPhoneNumber = jsonObject['phoneNumber']
        requestCompany = jsonObject['company']
        

        addRecruiterResponse = addRecruiter(users,
                                            recruiters,
                                            requestFirstName,
                                            requestLastName,
                                            requestPassword, 
                                            requestEmailAddress,
                                            requestPhoneNumber,
                                            requestCompany)

        signupStatus = addRecruiterResponse['result']

        return json.dumps(addRecruiterResponse)

    
if __name__ == '__main__':
    app.run(debug=True,
    	host=app.config.get("HOST", "0.0.0.0"),
    	port=app.config.get("PORT", 9000))  