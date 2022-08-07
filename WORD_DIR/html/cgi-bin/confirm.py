
#!/usr/bin/python

# Import modules for CGI handling
import cgi
import cgitb
import pymysql


def correctConfirm():
    print('''
          <HTML><TABLE ALIGN=center BORDER=1 CELLSPACING=1 CELLPADDING=1 >
                <TR VALIGN=TOP>
                    <TD>
<pre>   
    Registration Successful     
    Thanks
    Please check your emial.

</pre>
                    </TD>
                </TR>

            </TABLE></HTML>''')
    
def incorrectConfirm():
    print('''
          <HTML>
          <body>
          <TABLE ALIGN=center BORDER=1 CELLSPACING=1 CELLPADDING=1 >
                <TR VALIGN=TOP>
                    <TD>
                        <h1>So, The Information Is Incorrect.
                        <pre>
                            <h2><a href="/cgi-bin/regist.py">Please Registration Again</a>
                            <h3><a href="../regist.html">Back To Top</a>
                        </pre>
                    </TD>
                </TR>
            </TABLE></body></HTML>''')

def insertUser():
    db = pymysql.connect(host='localhost',user='test',password='password',db='db1')
    


    cursor = db.cursor()
    data=cgi.FieldStorage()
    name=data.getvalue('name')
    email=data.getvalue('email')
    sql = "INSERT INTO customers VALUES('%s','%s')" %(name, email)
    try:
   # Execute the SQL command
        cursor.execute(sql)
   # Commit your changes in the database
        db.commit()
    except:
   # Rollback in case there is any error
        db.rollback()

# disconnect from server
    db.close()

# Create instance of FieldStorage
form = cgi.FieldStorage()
name = form.getvalue('name')

# Get data from fields
if form.getvalue('confirm'):
    confirm = form.getvalue('confirm')
else:
    confirm = "Not set"
if(confirm == "yes"):
    insertUser()
    correctConfirm()
elif(confirm == "no"):
    incorrectConfirm()
else:
    print("You get Error,Please redo it.")