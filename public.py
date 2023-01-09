from flask import *
from database import *

public=Blueprint('public',__name__)


@public.route('/')
def home():
    return render_template('index.html')

@public.route('/login',methods=['post','get'])
def login():

    if 'submit' in request.form:
        username=request.form['username']
        pasw =request.form['password']

        q="select * from login where username='%s' and password='%s'"%(username,pasw)
        print(q)
        res=select(q)
        
        if res:
            session['lid']=res[0]["login_id"]
            utype=res[0]["usertype"]
            if utype == "admin":
                    flash("Login Succeessfully")
                    return redirect(url_for("admin.adminhome")) 
        else:
            flash("invalid Email or Password!")
            return redirect(url_for("public.login"))

    return render_template("login.html")


