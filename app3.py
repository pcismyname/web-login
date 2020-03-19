# เขียนโค้ดพยายาม comment ด้วยนะจะได้รู้ว่าแต่ละ def ทำอะไร?
# ทำให้สามารถแบ่งโค้ดเป็นส่วนๆได้ด้วย จะง่ายต่อการพัฒนานะครับ
# พี่จะยกตัวอย่างส่วนแรกให้นะ ตัวอย่างคือ comment ที่เป็นภาษาอังกฤษล้วนนะ
# ถ้าสังเกตุจะเห็นว่าพี่จัดหมดหมู่เอานะครับ

# import library for web app
from flask import *

# import library python connect to mongoDB
import pymongo
from pymongo import MongoClient

# running and setting about web app
app = Flask(__name__,template_folder='html01')
# คำอธิบายเพิ่มเติมคือ ส่วนของ template_folder ค่า default คือ template_folder='templates'
# ไม่ต้องตั้งค่าก็ได้ อันนี้บอกไว้เฉยๆ

# connect to mongoDB
client = MongoClient()
myclient =pymongo.MongoClient("mongodb://localhost:27017/")
db = client.login
col = db.data

print(myclient.list_database_names())

@app.route('/')
def host():
    return render_template('index.html')


# ทำไมเป็น  / เฉยๆครับ พี่อยากได้ /register นาาาาา
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

# ถ้าไม่ต้อง render_template ใหม่ทุกครั้งสามารถทำได้ไหม 
# แบบเป็นการ redirection แทนอะไรงี้ ได้ไม่ได้ก็บอกนะ
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
    # พี่อยากได้ port 80 ครับ
    