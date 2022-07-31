#!/usr/bin/python

# Import modules for CGI handling
import cgi
import cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
name = form.getvalue('name')
email = form.getvalue('email')

print("Content-type:text/html\r\n\r\n")
print('''<html>
            <head>
                Registration
            </head>
            <body>
                <h2 align=center style="color:blue;">Registration Form</h2>
                <br>
                <table align=left datasrc="#xmlRegData" border=2>
                    <tr>
                        <td> Name:</td>
                        <td>%s</td>
                    </tr>
                    <tr>
                        <td>E-mail:</td>
                        <td>%s</td>
                    </tr>
                </table>
                <br>
                <h3 align=center style="color:red;">Is this information correct ?</h3>
                <br>
                <form align=center method=GET action="cgi-bin/confirm.py">
                    <input type=radio name='confirm' value='yes'> YES   
                    <input type=radio name='confirm' value='no' checked> NO 
                    <input type=submit value=Submit>     
                    <input type=reset value=Reset>
                </form>
            </body>
        </HTML>'''%(name,email))
