from flask import *
from database import *
from emotionOfSentences import *
from test import *
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
    path="static/uploads/"+uuids+img.filename
    img.save(path)
    paths="static/uploads/"+uuids+img.filename
    
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
    # print(type(comment))
    out=predictValueFromText(comment)
    bert_out=preddictEmotion(comment)
    print(f"ssssssssssssssssssssssssssssssss{bert_out}")
    if out == "":
        q="insert into comment values(null,'%s','%s','No output','%s')"%(pid,comment,bert_out)
        insert(q)
    else:
        q="insert into comment values(null,'%s','%s','%s','%s')"%(pid,comment,out,bert_out)
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
    out=predictValueFromText(det)
    if out == "":
        q="insert into chat values(null,'%s','%s','%s',curdate(),'No output',curtime())"%(sid,rid,det)
        insert(q)
    else:  
        q="insert into chat values(null,'%s','%s','%s',curdate(),'%s',curtime())"%(sid,rid,det,out) 
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



@api.route('/mycommentgraph')
def mycommentgraph():
    data={}
    pid=request.args['pid']
    joy='joy'+'%'
    sadness='sadness'+'%'
    shame='shame'+'%'
    noout='No output'+'%'
    q="SELECT COUNT(`emotion`) AS cout FROM `comment` WHERE post_id='%s' AND `emotion` LIKE '%s' "%(pid,joy)
    print(q)
    joycount=select(q)[0]['cout']
    q="SELECT COUNT(`emotion`) AS cout FROM `comment` WHERE post_id='%s' AND `emotion` LIKE '%s' "%(pid,sadness)
    print(q)
    sadcount=select(q)[0]['cout']
    q="SELECT COUNT(`emotion`) AS cout FROM `comment` WHERE post_id='%s' AND `emotion` LIKE '%s' "%(pid,shame)
    print(q)
    shamecount=select(q)[0]['cout']
    q="SELECT COUNT(`emotion`) AS cout FROM `comment` WHERE post_id='%s' AND `emotion` LIKE '%s' "%(pid,noout)
    print(q)
    nocount=select(q)[0]['cout']

    if joycount == 0:
        joyPercentage = 0
    else:
        joyPercentage = (joycount / (joycount+sadcount+shamecount+nocount) ) * 100
    
    if sadcount == 0:
        sadPercentage = 0
    else:
        sadPercentage = (sadcount / (joycount+sadcount+shamecount+nocount) ) * 100
        
    if shamecount == 0:
        shamePercentage = 0
    else:
        shamePercentage = (shamecount / (joycount+sadcount+shamecount+nocount) ) * 100
    
    if nocount == 0:
        novaluePercentage = 0
    else:
        novaluePercentage = (nocount / (joycount+sadcount+shamecount+nocount) ) * 100
    
     
    print(joycount,sadcount,shamecount,nocount) 
    
    q="select * from comment where post_id='%s'"%(pid)
    res=select(q)
    
    if res:
        data['data']=res
        data['status']="success"
        data['joyPercentage']=joycount
        data['sadPercentage']=sadcount
        data['shamePercentage']=shamecount
        data['novaluePercentage']=nocount
        print("no count,...",nocount) 
    else:
        data['status']="failed"
    data['method']="mycommentgraph"
    return str(data)


from datetime import datetime, timedelta


@api.route('/chatemotion')
def chatemotion():
    data={}
    sid=request.args['sid']
    rid=request.args['rid']
    joy='joy'+'%'
    sadness='sadness'+'%'
    shame='shame'+'%'
    noout='No output'+'%'

    
    # Get the current date and time
    now = datetime.now()

    # Subtract 24 hours from the current time
    last_24_hours = datetime.now() - timedelta(hours=24)
    print(last_24_hours)
    print("now...........................",str(datetime.now())[0:19])
    destructuretime = str(last_24_hours)[0:19]
    print("24 before time..........",destructuretime)
    q="select curtime()"  
    curDate = select(q)
    print("date ........................",curDate) 

    q="select * from chat where (sender_id='%s' and receiver_id='%s') and   date  between '%s' and '%s' "%(sid,rid,destructuretime,str(datetime.now())[0:19])
    print(q) 
    thwentyFourTime = select(q)
    print(thwentyFourTime) 

    if thwentyFourTime:
        q="select count(emotion) as count from chat where (sender_id='%s' and receiver_id='%s')  and `emotion` LIKE '%s' and date  between '%s' and '%s'  "%(sid,rid,joy,destructuretime,str(datetime.now())[0:19])
        print(q)
        out=select(q)[0]['count'] 
        joycount = out
        q="select count(emotion) as count from chat where (sender_id='%s' and receiver_id='%s')  and `emotion` LIKE '%s' and date  between '%s' and '%s'  "%(sid,rid,sadness,destructuretime,str(datetime.now())[0:19])
        sadcount = select(q)[0]['count']
        q="select count(emotion) as count from chat where (sender_id='%s' and receiver_id='%s')  and `emotion` LIKE '%s' and date  between '%s' and '%s'  "%(sid,rid,shame,destructuretime,str(datetime.now())[0:19])
        shamecount = select(q)[0]['count']
        q="select count(emotion) as count from chat where (sender_id='%s' and receiver_id='%s')  and `emotion` LIKE '%s' and date  between '%s' and '%s'  "%(sid,rid,noout,destructuretime,str(datetime.now())[0:19])
        novalcount = select(q)[0]['count']
    
    
        q="select count(emotion) as count from chat where (sender_id='%s' and receiver_id='%s')  and `emotion` LIKE '%s' and date  between '%s' and '%s'  "%(rid,sid,joy,destructuretime,str(datetime.now())[0:19])
        herjoycount = select(q)[0]['count']
        q="select count(emotion) as count from chat where (sender_id='%s' and receiver_id='%s')  and `emotion` LIKE '%s' and date  between '%s' and '%s'  "%(rid,sid,sadness,destructuretime,str(datetime.now())[0:19])
        hersadcount = select(q)[0]['count']
        q="select count(emotion) as count from chat where (sender_id='%s' and receiver_id='%s')  and `emotion` LIKE '%s' and date  between '%s' and '%s'  "%(rid,sid,shame,destructuretime,str(datetime.now())[0:19])
        hershamecount = select(q)[0]['count']
        q="select count(emotion) as count from chat where (sender_id='%s' and receiver_id='%s')  and `emotion` LIKE '%s' and date  between '%s' and '%s'  "%(rid,sid,noout,destructuretime,str(datetime.now())[0:19])
        hernovalcount = select(q)[0]['count'] 

        


        print(joycount,sadcount,shamecount,novalcount)
        print(herjoycount,hersadcount,hershamecount,hernovalcount)

        mycount = max(joycount,sadcount,shamecount,novalcount)
        print("My count: ",mycount)

        if mycount == joycount:
            data['myemotion'] = "Happy"
        elif mycount == sadcount:
            data['myemotion'] = "Sad"
        elif mycount == shamecount: 
            data['myemotion'] = " Shame"
        elif mycount == novalcount:
            data['myemotion'] = "No Specific Emotion"

        print(data['myemotion'])
        
        
        hercount = max(herjoycount,hersadcount,hershamecount,hernovalcount)
        print("her count: ",hercount)

        if hercount == herjoycount:
            data['heremotion'] = "Happy" 
        elif hercount == hersadcount:
            data['heremotion'] = "Sad"
        elif hercount == hershamecount: 
            data['heremotion'] = "Shame"
        elif hercount == hernovalcount:
            data['heremotion'] = "No Specific Emotion"

        print(data['heremotion'])

        data['status']="success"
    else:
        data['status']="failed"
    
    data['method']="chatemotion" 
    return str(data) 