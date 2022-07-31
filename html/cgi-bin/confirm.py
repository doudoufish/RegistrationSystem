
#!/usr/bin/python

# Import modules for CGI handling
import cgi
import cgitb


def correctConfirm():
    print('''<TABLE ALIGN=center BORDER=1 CELLSPACING=1 CELLPADDING=1 >
                <TR VALIGN=TOP>
                    <TD>
                        <pre>
                            Registration Successful

                            Thanks
                        </pre>
                    </TD>
                </TR>

            </TABLE>''')
    
def incorrectConfirm():
    print('''<TABLE ALIGN=center BORDER=1 CELLSPACING=1 CELLPADDING=1 >
                <TR VALIGN=TOP>
                    <TD>
                        <pre>
                        So, The Information Is Incorrect.

                        <a href="/cgi-bin/regist.py">Please Registration Again</a>

                        <a href="regist.html">Back To Top</a>
                        </pre>
                    </TD>
                </TR>

            </TABLE>''')


# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('confirm'):
    confirm = form.getvalue('confirm')
else:
    confirm = "Not set"

if(confirm == "YES"):
    correctConfirm()
elif(confirm == "No"):
    incorrectConfirm()
else:
    print("You get Error,Please redo it.")