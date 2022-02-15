from ast import Delete
from platform import java_ver
from flask import Flask, request, jsonify
from itsdangerous import json

app=Flask(__name__) 

FAKE_DATABASE = []
count = 0


#......................................................................CRUD......................................................................

#CREATE.........................................................................
@app.route("/register", methods=["POST"])
def post():
    u = request.json["username"]
    f = request.json["fname"]
    l = request.json["lname"]
    e = request.json["email"]
    p = request.json["password"]
    global count
    count+=1

    user_object = {
        "id" : count,
        "username": u,
        "fname": f,
        "lname" : l,
        "email" : e,
        "password" : p
    }
    FAKE_DATABASE.append(user_object)
    return jsonify(user_object)


#READ.........................................................................
@app.route("/users",methods=["GET"])
def home2():
    return jsonify(FAKE_DATABASE)

#UPDATE.......................................................................

@app.route("/user/<int:id>", methods=["PATCH"])
def patch_user(id):
    for u in FAKE_DATABASE:
        if u["id"] == id:
            u["username"] = request.json["username"]
        return jsonify(u)

#...............DELETE....................................

@app.route("/user/<int:id>", methods = ["DELETE"])
def delete_user(id):
    for u in FAKE_DATABASE:
        if u["id"] == id:
            FAKE_DATABASE.remove(u)
            return f"user with ID {id} deleted"
   
if __name__ == '__main__':
    app.run(
        debug=True,
        port=3000,
        host="0.0.0.0"
    )
    #.............................................................................................................

    from re import X
from flask import Flask,json, request,jsonify
from datetime import datetime 
t=datetime.now()
mad_Thing={}
hinokami=[]
kagura=0
app=Flask(_name_)


#Profile
@app.route("/profile",methods=["GET"])
def home():

    user_object={}
    user_object['data']=mad_Thing

    return json.dumps(user_object,indent=1)

@app.route("/profile",methods=["POST"])
def profPost():
    
    
    mad_Thing["last_update"]=t
    mad_Thing["username"]=request.json["username"]
    mad_Thing["role"]=request.json["role"]
    mad_Thing["color"]=request.json["color"]
    
    user_object={"data":mad_Thing}
    
    return json.dumps(user_object,indent=1)

@app.route("/profile",methods=["PATCH"])
def profPatch():
    if 'username' in request.json:
        mad_Thing["username"]=request.json["username"]
    
    if 'role' in request.json:
        mad_Thing["role"]=request.json["role"]

    if 'color' in request.json:
        mad_Thing["color"]=request.json["color"]

    user_object={"data":mad_Thing}

    return json.dumps(user_object,indent=1)
    