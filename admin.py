from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')



@admin.route('/adminviewuser')
def adminviewuser():
    data={}
    q='select * from user'
    data['res']=select(q)
    return render_template('adminviewuser.html',data=data)

@admin.route('/adminviewpost')
def adminviewpost():
    data={}
    q='select * from post inner join user using (user_id)'
    data['res']=select(q)
    return render_template('adminviewpost.html',data=data)


@admin.route('/adminviewcomments')
def adminviewcomments():
    data={}
    pid=request.args['pid']
    q="select * from comment where post_id='%s'"%(pid)
    data['res']=select(q)
    return render_template('adminviewcomments.html',data=data)


@admin.route('/adminviewcomplaint',methods=['get','post'])
def adminviewcomplaint():
    data={}
    q="select * from user inner join complaint using (user_id)"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None

    if action == "reply":
        data['replysec']=True

        if 'submit' in request.form:
            reply=request.form['reply']

            q="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
            update(q)
            return redirect(url_for("admin.adminviewcomplaint"))
    return render_template('adminviewcomplaint.html',data=data)

