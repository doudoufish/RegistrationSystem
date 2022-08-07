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
            <body>
                <h2 align=center style="color:blue;">Registration Form</h2>
                <br>
                <table align=center datasrc="#xmlRegData" border=2>
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
                <form align=center method=GET action="confirm.py">
                    <input type=radio name='confirm' value='yes'> YES
                    <input type=hidden name='name' value='%s'>
                    <input type=hidden name='email' value='%s'>
                    <input type=radio name='confirm' value='no' checked> NO 
                    <input type=submit value=Submit>     
                    <input type=reset value=Reset>
                </form>
            </body>
        </HTML>'''%(name,email,name,email))
