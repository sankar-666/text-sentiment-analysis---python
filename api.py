from flask import *
from database import *

api=Blueprint('api',__name__)



@api.route("/reg",methods=['get','post'])
def reg():
    if 'btn' in request.form:
        email=request.form['email']
        passw=request.form['passw']
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        dob=request.form['dob']
        housename=request.form['housename']
        city=request.form['city']
        district=request.form['district']
        pincode=request.form['pincode']

        q="select * from login where username='%s'"%(email)
        res=select(q)
        if res:
            flash("This email already exist!, try register with new one.")
        else:
            q="insert into login values('%s','%s','customer','active')"%(email,passw)
            insert(q)
            q="insert into customer values (NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','active')"%(email,fname,lname,phone,dob,housename,city,district,pincode,passw)
            # print(q)
            insert(q)
            flash("Registration successfull")
            return redirect(url_for("public.login"))
    return render_template("reg.html")
