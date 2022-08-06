#!/usr/bin/python



print("Content-type:text/html\r\n\r\n")
print('''<HTML>
<HEAD>
<TITLE>Registration Form</TITLE>
</HEAD>
  Registration Form
  <form action="process.py" method=GET>
  Name: <input type=text name=name value="" size=23>
  <br>
  Email: <input type=text name=email value="" size=23>
    <br>
    <input type=submit value=Submit name=B1>        
    <input type=reset value=Reset name=B2>
  </form>
</BODY>
</HTML>''')
