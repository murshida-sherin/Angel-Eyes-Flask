import functools
import os
from flask import *
from werkzeug.utils import secure_filename

from src.dbconnection import *
app=Flask(__name__)
from flask import session
app.secret_key='aaa'

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return '''<script>alert("please login");window.location="/"</script>'''
        return func()

    return secure_function
@app.route("/",methods=["POST","GET"])
def main():
    return render_template("LOGIN.html")
@app.route("/login",methods=["POST","GET"])
def login():
    uname=request.form['Username']
    keyword=request.form['password']
    query="SELECT * FROM `login` WHERE `user_name`=%s AND `password`=%s"
    val=(uname,keyword)
    res=select1(query,val)
    if res is None:
        return '''<script>alert("Invalid");window.location="/"</script>'''
    elif res[3]=='admin':
        session['lid']=res[0]
        return '''<script>alert("W E L C O M E");window.location="/adminhome"</script>'''
    elif res[3]=='caretaker':
        session['lid']=res[0]
        return '''<script>alert("W E L C O M E");window.location="/caretakerhome"</script>'''
    else :
        return '''<script>alert("Invalid");window.location="/"</script>'''






@app.route("/caretakerregistration",methods=["POST","GET"])
def caretakerregistration():
    return render_template("CARETAKERREGISTRATION.html")
@app.route("/caretakerreg",methods=["POST","GET"])
def caretakerreg():
    try:
        fname =request.form['textfield']
        lname =request.form['textfield2']
        gender=request.form['radiobutton']
        dob=request.form['textfield10']
        place=request.form['textfield3']
        post=request.form['textfield4']
        pin=request.form['textfield5']
        phone=request.form['textfield6']
        email=request.form['textfield7']
        uname=request.form['textfield8']
        password=request.form['textfield9']
        query1="INSERT INTO `login` VALUES(NULL,%s,%s,'pending')"
        val1=(uname,password)
        id=iud(query1,val1)
        query2="INSERT INTO `care_taker` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'pending')"
        val2=(str(id),fname,lname,gender,dob,place,post,pin,phone,email)
        iud(query2,val2)
        return '''<script>alert("CARETAKER REGISTRATION SUCCESSFUL");window.location="/"</script>'''
    except:
        return '''<script>alert("USER NAME ALREADY EXIST");window.location="/"</script>'''











@app.route("/adminhome",methods=["POST","GET"])
@login_required
def adminhome():
    return render_template("ADMINHOME.html")

@app.route("/viewandapprovecaretakers",methods=["POST","GET"])
@login_required

def viewandapprovecaretakers():
    query="SELECT `care_taker`.* FROM `care_taker` JOIN `login` ON `login`.`id`=`care_taker`.`Login_id` WHERE `login`.`type`='pending'"
    res=selectalla(query)
    return render_template("VIEWANDAPPROVECARETAKERS.html",val=res)

@app.route("/approve",methods=["POST","GET"])
@login_required

def approve():
    care_id=request.args.get('cid')
    query="UPDATE `login` SET `type`='caretaker' WHERE id=%s"
    iud(query,care_id)

    return'''<script>alert('Approved');window.location='/viewandapprovecaretakers'</script>'''

@app.route("/reject",methods=["POST","GET"])
@login_required

def reject():
    care_id = request.args.get('cid')
    query = "UPDATE `login` SET `type`='rejected' WHERE id=%s"
    iud(query, care_id)

    return '''<script>alert('Rejected');window.location='/viewandapprovecaretakers'</script>'''





@app.route("/viewcaretakers",methods=["POST","GET"])
@login_required

def viewcaretakers():
    query = "SELECT `care_taker`.* FROM `care_taker` JOIN `login` ON `login`.`id`=`care_taker`.`Login_id` WHERE `login`.`type`='caretaker'"
    res = selectalla(query)



    return render_template("VIEWCARETAKERS.html",val=res)




@app.route("/blindperson",methods=["POST","GET"])
@login_required

def blindperson():
    id=request.args.get('id')
    query="SELECT * FROM `blind_person` WHERE `care_id`=%s"
    res=selectall(query,str(id))


    return render_template("BLINDPERSON.html",val=res)

@app.route("/viewcomplaints",methods=["POST","GET"])
@login_required
def viewcomplaints():
    qry="SELECT `complaints`.*,`care_taker`.`First_Name`,`Last_Name` FROM `care_taker` JOIN `complaints` ON `complaints`.`User_id`=`care_taker`.`Login_id` WHERE `complaints`.`Replay`='pending'"
    res=selectalla(qry)
    return render_template("VIEWCOMPLAINTS.html",val=res)
@app.route("/sendreply",methods=["POST","GET"])
@login_required

def sendreply():
    id=request.args.get('id')
    session['cid']=id
    return render_template("SENDREPLY.html")

@app.route("/sendreplynew",methods=["POST","GET"])
@login_required

def sendreplynew():
    comid=session['cid']
    reply=request.form['textfield']
    qry="UPDATE `complaints` SET `Replay`=%s WHERE `Complaint_id`=%s"
    val=(reply,str(comid))
    iud(qry,val)
    return '''<script>alert('REPLY SENDED SUCCESSFULLY');window.location='/viewcomplaints'</script>'''


@app.route("/caretakerhome",methods=["POST","GET"])
@login_required

def caretakerhome():
    return render_template("CARETAKERHOME.html")
@app.route("/caretakerprofile",methods=["POST","GET"])
@login_required

def caretakerprofile():


    id=session['lid']
    qry="SELECT * FROM`care_taker` WHERE `Login_id`=%s"
    res=select1(qry,str(id))

    return render_template("CARETAKERPROFILE.html",val=res)

@app.route("/updatecaretaker",methods=["POST","GET"])
@login_required

def updatecaretaker():
    lid=session['lid']
    fname = request.form['textfield8']
    lname = request.form['textfield7']
    gender = request.form['radiobutton']
    dob = request.form['textfield6']
    place = request.form['textfield5']
    post = request.form['textfield4']
    pin = request.form['textfield3']
    phone = request.form['textfield2']
    email = request.form['textfield']
    qry="UPDATE `care_taker` SET `First_Name`=%s,`Last_Name`=%s,`Gender`=%s,`DOB`=%s,`Place`=%s,`Post`=%s,`Pin`=%s,`Phone`=%s,`Email`=%s WHERE `Login_id`=%s"
    val=(fname,lname,gender,dob,place,post,pin,phone,email,str(lid))
    iud(qry,val)
    return '''<script>alert('UPDATED SUCCESSFULLY');window.location='/caretakerhome'</script>'''



@app.route("/blindpersonmanagement",methods=["POST","GET"])
@login_required

def blindpersonmanagement():
    lid=session['lid']
    qry="SELECT * FROM `blind_person` WHERE care_id=%s"
    res=selectall(qry,str(lid))


    return render_template("BLINDPERSONMANAGEMENT.html",val=res)
@app.route("/delete",methods=["POST","GET"])
@login_required

def delete():
    id=request.args.get('id')
    qry="DELETE  FROM `blind_person` WHERE `V_id`=%s"
    iud(qry,str(id))
    return '''<script>alert('DELETED SUCCESSFULLY');window.location='/caretakerhome'</script>'''

@app.route("/edit",methods=["POST","GET"])
@login_required

def edit():
    id = request.args.get('id')
    session['bid']=id

    qry="SELECT * FROM `blind_person` WHERE `V_id`=%s"
    res=select1(qry,str(id))
    return render_template("EDITBLIND.html",val=res)

@app.route("/update",methods=["POST","GET"])
@login_required

def update():
    id=session['bid']

    fname = request.form['textfield8']
    lname = request.form['textfield7']
    gender = request.form['radiobutton']
    dob = request.form['textfield6']
    place = request.form['textfield5']
    post = request.form['textfield4']
    pin = request.form['textfield3']
    phone = request.form['textfield2']
    imeino = request.form['textfield']
    qry="UPDATE `blind_person` SET `First_Name`=%s,`Last_Name`=%s,`Gender`=%s,`DOB`=%s,`Place`=%s,`Post`=%s,`Pin`=%s,`Phone`=%s,`IMEI_NO`=%s WHERE `V_id`=%s"
    val=(fname,lname,gender,dob,place,post,pin,phone,imeino,str(id))
    iud(qry,val)

    return '''<script>alert('EDITED SUCCESSFULLY');window.location='/caretakerhome'</script>'''





@app.route("/addblind",methods=["POST","GET"])
@login_required

def addblind():
    return render_template("ADDBLIND.html")

@app.route("/add",methods=["POST","GET"])
@login_required

def add():
    fname = request.form['textfield8']
    lname = request.form['textfield7']
    gender = request.form['radiobutton']
    dob = request.form['textfield6']
    place = request.form['textfield5']
    post = request.form['textfield4']
    pin = request.form['textfield3']
    phone = request.form['textfield2']
    imeino= request.form['textfield']
    query="INSERT INTO `blind_person` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(fname,lname,gender,dob,place,post,pin,phone,imeino,session['lid'])
    iud(query,val)
    return '''<script>alert('BLIND PERSON ADDED');window.location='/blindpersonmanagement'</script>'''









@app.route("/familiarpersonmanagement",methods=["POST","GET"])
@login_required

def familiarpersonmanagement():
    qry="SELECT `blind_person`.`First_Name`,`blind_person`.`Last_Name`,`familiar_person`.* FROM `familiar_person` JOIN `blind_person` ON `blind_person`.`V_id`=`familiar_person`.`blind_id`"

    res=selectalla(qry)


    return render_template("FAMILIARPERSONMANAGEMENT.html",val=res)

@app.route("/deletefamiliarperson",methods=["POST","GET"])
@login_required

def deletefamiliarperson():
    id = request.args.get('id')
    qry="DELETE FROM `familiar_person` WHERE f_id=%s"
    iud(qry,str(id))


    return '''<script>alert('DELETED SUCCESSFULLY');window.location='/familiarpersonmanagement'</script>'''

@app.route("/editfamiliarperson",methods=["POST","GET"])
@login_required

def editfamiliarperson():
    id=request.args.get('id')
    session['fid']=id
    qry="SELECT * FROM `familiar_person` WHERE `f_id`=%s"
    res=select1(qry,str(id))
    qry1="SELECT * FROM `blind_person`"
    res1=selectalla(qry1)

    return render_template("EDITFAMILIARPERSON.html",val=res,val1=res1)

@app.route("/updatefamiliarperson",methods=["POST","GET"])
@login_required

def updatefamiliarperson():
    try:
        fid=session['fid']
        blind = request.form['select']
        name = request.form['textfield']
        relation = request.form['textfield2']
        image = request.files['file']
        file = secure_filename(image.filename)
        image.save(os.path.join("static/familiarperson", file))
        qry="UPDATE `familiar_person` SET `blind_id`=%s,`name`=%s,`image`=%s,`relation`=%s WHERE `f_id`=%s"
        val=(blind,name,file,relation,str(fid))
        iud(qry,val)
        return '''<script>alert('UPDATED SUCCESSFULLY');window.location='/familiarpersonmanagement'</script>'''
    except Exception as e:
        blind = request.form['select']
        name = request.form['textfield']
        relation = request.form['textfield2']
        qry = "UPDATE `familiar_person` SET `blind_id`=%s,`name`=%s,`relation`=%s WHERE `f_id`=%s"
        val = (blind, name,relation,str(fid))
        iud(qry, val)
        return '''<script>alert('UPDATED SUCCESSFULLY');window.location='/familiarpersonmanagement'</script>'''






@app.route("/addfamiliarperson",methods=["POST","GET"])
@login_required

def addfamiliarperson():
    lid=session['lid']

    qry="SELECT * FROM `blind_person` WHERE care_id=%s"
    res=selectall(qry,str(lid))

    return render_template("ADDFAMILIARPERSON.html",val=res)


@app.route("/submitfamiliarperson",methods=["POST","GET"])
@login_required

def submitfamiliarperson():

    blind=request.form['select']
    name=request.form['textfield']
    relation=request.form['textfield2']
    image=request.files['file']
    file=secure_filename(image.filename)
    image.save(os.path.join("static/familiarperson",file))
    qry="INSERT INTO `familiar_person` VALUES(NULL,%s,%s,%s,%s)"
    val=(blind,name,file,relation)
    iud(qry,val)

    return '''<script>alert('FAMILIAR PERSON ADDED');window.location='/familiarpersonmanagement'</script>'''


@app.route("/viewemergencyhelp",methods=["POST","GET"])
@login_required

def viewemergencyhelp():
    qry="SELECT `blind_person`.`First_Name`,`blind_person`.`Last_Name`,`help`.* FROM `blind_person` JOIN `help` ON `blind_person`.`IMEI_NO`=`help`.`imei`"
    res=selectalla(qry)



    return render_template("VIEWEMERGENCYHELP.html",val=res)

@app.route("/logout")
@login_required

def logout():
    session.clear()
    return render_template("LOGIN.html")

@app.route("/sendcomplaints",methods=["POST","GET"])
@login_required

def sendcomplaints():
    return render_template("SENDCOMPLAINTS.html")
@app.route("/complaints",methods=["POST","GET"])
@login_required

def complaints():
    complaints = request.form['textfield']
    query="INSERT INTO `complaints` VALUES (NULL,%s,curdate(),%s,'pending')"
    val=(session['lid'],complaints)
    iud(query,val)
    return '''<script>alert('COMPLAINTS SENDED SUCCESSFULLY');window.location='/caretakerhome'</script>'''


@app.route("/viewcomplaintsreply",methods=["POST","GET"])
@login_required

def viewcomplaintsreply():
    qry="SELECT  * FROM`complaints`"
    res=selectalla(qry)



    return render_template("VIEWCOMPLAINTSREPLY.html",val=res)



@app.route("/tracklocation",methods=["POST","GET"])
@login_required

def tracklocation():
    qry="SELECT `blind_person`.*,`location`.`latitude`,`location`.`longitude` FROM `blind_person` JOIN `location` ON `blind_person`.`V_id`=`location`.`blind_id` WHERE `blind_person`.`care_id`=%s"
    val=( session['lid'])
    res=selectall(qry,val)
    print(res)

    return render_template("TRACKLOCATION.html",val=res)
app.run(debug=True)