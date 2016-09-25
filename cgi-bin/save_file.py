#!/usr/bin/python3
import cgi, cgitb, fileinput, os
path=os.path.dirname(os.path.realpath(__file__))[:-7]+"main/projects/"
form = cgi.FieldStorage()
file_name = form.getvalue('file_name')
file_code = form.getvalue('file_code')
ext = form.getvalue('ext')
s=path+file_name+ext
with open(s,"w") as outfile:
	
	outfile.write(file_code)
