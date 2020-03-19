import pymongo
from flask import *
from pymongo import MongoClient

client = MongoClient()
myclient =pymongo.MongoClient("mongodb://localhost:27017/")
app = Flask(__name__,template_folder='html01')
db = client.login
col = db.data
print(myclient.list_database_names())

@app.route('/')
def host():
    return render_template('index.html')


@app.route('/',methods=['POST'])
def submit():
    name = request.form['name']
    surename = request.form['surename']
    email = request.form['email']
    contact = request.form['contact']
    gender = request.form['gender']
    user = request.form['user']
    password = request.form['pass']
    col.insert_one({'name': name,'surenane':surename,'email':email,'contact':contact,
                    'gender':gender,'password':password,'username':user})
    return render_template('login.html')

@app.route('/back',methods=['POST'])
def back():
    return render_template('index.html')


@app.route('/login/',methods=['POST'])
def login():
    return render_template('login.html')

@app.route('/back2',methods=['POST'])
def back2():
    return render_template('login.html')

@app.route('/login/display',methods=['POST'])
def display():
    return render_template('display.html')




if __name__ == "__main__":
    app.run(debug=True,port=50)