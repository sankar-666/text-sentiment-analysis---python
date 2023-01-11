from flask import *
from database import *
import uuid

api=Blueprint('api',__name__)



@api.route("/login")
def login():
	data={}

	uname=request.args['username']
	pwd=request.args['password']


	print(uname,pwd)
	q="select * from login where username='%s' and password='%s'"%(uname,pwd)
	res=select(q)
	if res:
		
		data['status']='success'
		data['data']=res
	else:
		data['status']='failed'
	return str(data)

@api.route("/userreg")
def userreg():
	data={}

	fname=request.args['fname']
	lname=request.args['lname']
	
	phone=request.args['phone']
	email=request.args['email']
	
	place=request.args['place']
	
	uname=request.args['username']
	pwd=request.args['password']

	q="insert into login values(null,'%s','%s','user')"%(uname,pwd)
	id=insert(q)

	q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
	insert(q)
	data['status']='success'
	return str(data)

@api.route('/viewallposts')
def viewallposts():
    data={}
    q='select * from post inner join user using (user_id)'
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="viewallposts"
    return str(data)


@api.route('/viewamyposts')
def viewamyposts():
    data={}
    lid=request.args['lid']
    q='select * from post inner join user using (user_id) where user_id=(select user_id from user where login_id="%s")'%(lid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="viewamyposts"
    return str(data)


@api.route('/addpost',methods=['get','post'])
def addpost():
    data={}
    post=request.form['post']
    lid=request.form['lid']
    img=request.files['image']
    uuids=str(uuid.uuid4())
    path="D:/Projects/College Projects/Viswajyothi Btech/Text Sentiment Analysis/web/static/uploads/"+uuids+img.filename
    img.save(path)
    paths="/static/uploads/"+uuids+img.filename
    
    q="insert into post values (null,(select user_id from user where login_id='%s'),'%s','%s',curdate(),'pending')"%(lid,post,paths)
    insert(q)
    data['status']="success"
    data['method']="addpost"
    return str(data)


@api.route('/viewcommenperpost')
def viewcommenperpost():
    data={}
    pid=request.args['pid']
    q="select * from comment where post_id='%s'"%(pid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="viewcommenperpost"
    return str(data)


@api.route('/addcommentperpost',methods=['get','post']) 
def addcommentperpost():
    data={}
    pid=request.args['pid']
    comment=request.args['comment']

    q="insert into comment values(null,'%s','%s','pending')"%(pid,comment)
    insert(q)
    data['status']="success"
    data['method']="addcommentperpost"
    return str(data)


@api.route('/mypostcomment')
def mypostcomment():
    data={}
    pid=request.args['pid']
    q="select * from comment where post_id='%s'"%(pid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="mypostcomment"
    return str(data)


@api.route('/deletemypost')
def deletemypost():
    data={}
    pid=request.args['pid']
    q="delete from post where post_id='%s'"%(pid)
    delete(q)
    
    data['status']="success"
    
    data['method']="deletemypost"
    return str(data)


@api.route('/editpost')
def editpost():
    data={}
    pid=request.args['post_id']
    post=request.args['post']
    q="update post set post='%s' where post_id='%s'"%(post,pid)
    update(q)
    
    data['status']="success"
    return str(data)


@api.route('/viewusers')
def viewusers():
    data={}
    lid=request.args['log_id']
    q="select * from user where user_id <> (select user_id from user where login_id='%s' )"%(lid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="viewusers"
    return str(data)




@api.route("/chatdetail")
def chatdetail():
	sid=request.args['sender_id']
	rid=request.args['receiver_id']
	
	data={}
	q="select * from chat where (sender_id='%s' and receiver_id='%s') or (sender_id='%s' and receiver_id='%s') group by chat_id "%(sid,rid,rid,sid)
	
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		
		data['status']="failed"
	data['method']='chatdetail'
	
	return str(data)

@api.route("/chat")
def chat():
	data={}
	sid=request.args['sender_id']
	rid=request.args['receiver_id']
	det=request.args['details']
	
	
	q="insert into chat values(null,'%s','%s','%s',curdate(),'pending')"%(sid,rid,det)
	insert(q)
	data['status']='success'
	data['method']='chat'
	return str(data)


@api.route('/viewcomp')
def viewcomp():
    data={}
    lid=request.args['log_id']
    q="select * from complaint where user_id= (select user_id from user where login_id='%s' )"%(lid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="viewcomp"
    return str(data)


@api.route('/User_Complaint')
def User_Complaint():
    data={}
    lid=request.args['log_id']
    complaints=request.args['complaints']
    q="insert into complaint values (null,(select user_id from user where login_id='%s' ),'%s','pending',curdate() )"%(lid,complaints)
    insert(q)

    data['status']="success"
    
    data['method']="User_Complaint"
    return str(data)