
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


# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('confirm'):
    confirm = form.getvalue('confirm')
else:
    confirm = "Not set"
print(confirm)
if(confirm == "yes"):
    correctConfirm()
elif(confirm == "no"):
    incorrectConfirm()
else:
    print("You get Error,Please redo it.")