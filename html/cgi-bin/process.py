#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getvalue('confirm'):
   confirm = form.getvalue('confirm')
else:
   confirm = "Not set"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Registration</title>")
print ("</head>")
print ("<body>")
print ("<h2> Is this information correct?  %s</h2>" % confirm)
print ("</body>")
print ("</html>")