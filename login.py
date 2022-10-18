from urllib import response
from flask import Flask,Response,request
app = Flask(__name__)
import json
import sqlite3
from db.dal import DAL,User, USERS
# import uuid

@app.route('/login', methods=['POST'])
def login():
    username=request.json["username"]
    password=request.json["password"]
    user=User(username,password)
    user.authenticate()
    id=user.id
    r=Response(json.dumps({'id':id}))
    r.headers["Content-type"]="application/json"
    return r

@app.route('/add', methods=['POST'])
def add():
    username=request.json["username"]
    password=request.json["password"]
    adminPassword=request.json["ap"]
    id=User(username,password,"","").authenticate()
    print('enter:',id)
    if id=='null':
        id=User(username,password,"",adminPassword).save()
        print('in: ',id)
    r=Response(json.dumps({'id':id})) #if return null=not admin
    r.headers["Content-Type"]="application/json"
    return r

@app.route('/remove', methods=['POST'])
def remove(): #ניתן לעשות בדיקה אם קיים
    # username=request.json["username"]
    id1=request.json["id"]
    # adminPassword=request.json["ap"]
    user=User("","",id1,"")
    status=user.remove()
    # status=User(username,'none',id1,adminPassword)
    r=Response(json.dumps({'status':status}))
    r.headers["Content-Type"]="application/json"
    return r

@app.route('/update', methods=['POST'])
def update():
    id=request.json["id"]
    oldPassword=request.json["oldPassword"]
    newUsername=request.json["newUsername"]
    newPassword=request.json["newPassword"]
    user=User("",oldPassword,id,"")
    user.authenticatePasswordAndId()
    id=user.id
    if id != 'null':
        if newUsername=="null":
            username=user.username
            status=user.update(id,username,newPassword)
        elif newPassword=="null":
            status=user.update(id,newUsername,oldPassword)
        else:
            status=user.update(id,newUsername,newPassword)
    r=Response(json.dumps({'status':status}))
    r.headers["Content-Type"]="application/json"
    return r
    
@app.route('/')
def homePage():
    return 'Home Page!'

@app.route('/retuenJson',methods=['POST','GET'])
def retuenJson():
    r=Response(json.dumps({'hello world':111}))
    r.headers["Content-Type"]="application/json"
    return r

@app.route('/list',methods=['POST','GET'])
def retuenJson1():
    rows=User().list1()
    print(rows)
    r=Response(json.dumps({'usernames':rows}))
    r.headers["Content-Type"]="application/json"
    return r

@app.route('/listAll',methods=['POST','GET'])
def retuenJson2():
    adminPassword=request.json["ap"]
    user=User("","","",adminPassword)
    rows=user.listAll()
    print(rows)
    r=Response(json.dumps(rows))
    r.headers["Content-Type"]="application/json"
    return r

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, host='(my IPv4 Address:) 10.103.50.80', port='(my port:) 506')