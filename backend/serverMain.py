import json
from flask import Flask
from flask import request
from flask import abort, redirect, url_for
from pymongo import MongoClient
from util import *

app = Flask(__name__)

dbClient = MongoClient('mongodb://Shake_In:password1@ds047652.mongolab.com:47652/shake_in')
db = dbClient.shake_in
users = db.users
recruiters = db.recruiters


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    	return 'You submitted a post request'
    else:
    	return 'You tried 2 GET'


@app.route('/resume')
def resume():
    #res = addUser(users, recruiters, "tom", "manzini", "goodPassword", "goodEmail", "12345678901", "RPI", "BS", "1.0", "coding n shit")
    
    return redirect(url_for('applicantHomepage'))

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

        if loginStatus == "SUCCESS":
            return redirect(url_for('applicantHomepage'))
        else:
            return "Login failed\n"
            # TODO: redirect back here

@app.route('/applicantHomepage', methods=['GET', 'POST'])
def applicantHomepage():
    if request.method == 'GET':
        return 'Welcome back, applicant!\n'
    if request.method == 'POST':
        return "Error: applicantHomepage does not support POST yet\n"

@app.route('/recruiterHomepage', methods=['GET', 'POST'])
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
        requestEmail = jsonObject['emailAddress']
        requestPassword = jsonObject['password']
        requestFirstName = jsonObject['firstName']
        requestLastName = jsonObject['lastName']
        requestPhoneNumber = jsonObject['phoneNumber']
        requestSchool = jsonObject['school']
        requestEduLevel = jsonObject['eduLevel']
        requestGpa = jsonObject['GPA']
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
        requestEmail = jsonObject['emailAddress']
        requestPassword = jsonObject['password']
        requestFirstName = jsonObject['firstName']
        requestLastName = jsonObject['lastName']
        requestPhoneNumber = jsonObject['phoneNumber']
        requestSchool = jsonObject['school']
        requestEduLevel = jsonObject['eduLevel']
        requestGpa = jsonObject['GPA']
        requestSkills = jsonObject['skills']


        addRecruiterResponse = addRecruiter(users,
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
        signupStatus = addRecruiterResponse['result']

        if signupStatus == "SUCCESS":
            return redirect(url_for('applicantHomepage'))

        else:
            return "Email address in use"


    
if __name__ == '__main__':
    app.run(
    	host=app.config.get("HOST", "0.0.0.0"),
    	port=app.config.get("PORT", 9000))  