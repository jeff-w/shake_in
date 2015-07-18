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

        if loginStatus == "SUCCESS":
            return redirect(url_for('applicantHomepage'))
        else:
            return "Login failed\n"
            # TODO: redirect back here

@app.route('/applicantShake', methods=['GET', 'POST'])
def applicantHomepage():
    if request.method == 'GET':
        return 'Welcome back, applicant!\n'
    if request.method == 'POST':
        jsonObject = request.get_json()


        addShakerResponse1 = addShaker("test1", (1, 2), True)
        addShakerResponse2 = addShaker("test2", (3, 2), False)
        addShakerResponse3 = addShaker("test3", (5, 2), False)
        addShakerResponse4 = addShaker("test5", (2, 2), False)

        nearestShaker = getNearestShakers("test1", 50)


        return "SUCCESS:POSTed!\n"

@app.route('/recruiterShake', methods=['GET', 'POST'])
def recruiterHomepage():
    if request.method == 'GET':
        return 'Welcome back, recruiter!\n'
    if request.method == 'POST':
        return "Error: recruiterHomepage does not support POST yet\n"

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

        if signupStatus == "SUCCESS":
            return redirect(url_for('applicantHomepage'))

        else:
            return "Email address in use"
           


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

        if signupStatus == "SUCCESS":
            return redirect(url_for('recruiterHomepage'))

        else:
            return "Email address in use"


    
if __name__ == '__main__':
    app.run(
    	host=app.config.get("HOST", "0.0.0.0"),
    	port=app.config.get("PORT", 9000))  