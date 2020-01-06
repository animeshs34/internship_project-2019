#!C:\Program Files\Python37\Python.exe
print("Content-type:text/html \n")
import cgi


form = cgi.FieldStorage()

name = form.getvalue("data")

print("""
<html><head><title>Sample Page</title>
</head><body>
<h1>Your estimated Car Price is {} lacs</h1>
</body></html>
""".format(name))
