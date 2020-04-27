#import library for web app
from flask import *

#import library  for password
import bcrypt

#import library for mongo database
import pymongo
from pymongo import MongoClient

#connect to MongoDB
client = MongoClient()
myclient =pymongo.MongoClient("mongodb://localhost:27017/")
app = Flask(__name__,template_folder='html01')
db = client.login #db for acces datanase name login
col = db.data    #col for access column name data
print(myclient.list_database_names())


#first page
@app.route('/')
def host():
    if 'username' in session :
        return 'You are logged in as ' + session['username']

    return render_template('index.html')


@app.route('/register',methods=['POST','GET'])
def submit():

    #store data from form in variable
    if request.method == 'POST' :
        name = request.form['name']
        surename = request.form['surename']
        email = request.form['email']
        contact = request.form['contact']
        gender = request.form['gender']
        user = request.form['user']
        password = request.form['pass']
        existing_user = col.find_one({'username' : user})

        #check if user already exist
        if existing_user is None:
            hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) #hash the password

            #insert data in database
            col.insert_one({'name' : name, 'surenane' : surename, 'email' : email, 'contact' : contact,
                    'gender' : gender, 'password' : hashpass, 'username':user})

            session['username'] = name
            return redirect(url_for('host'))

        return 'That username already exist'
    return render_template('index.html')



#login page
@app.route('/login/',methods=['POST','GET'])
def login():
    if request.method == 'POST' :
            login_user = col.find_one({'username' : request.form['user']})
            if login_user:

                #check the password
                if bcrypt.hashpw(request.form['pass'].encode('utf-8'),  login_user['password']) ==  login_user['password']:
                    session['username'] = login_user['name']
                    return redirect(url_for('host'))

            return 'Invalid username or password'
    return render_template('login.html')


#display page
@app.route('/login/display',methods=['POST'])
def display():
    return render_template('display.html')


if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(debug=True,port=80)