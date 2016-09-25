
#!/usr/local/bin/python3
import cgi, cgitb, fileinput,os

path=os.path.dirname(os.path.realpath(__file__))[:-7]+"main/src-noconflict/snippets/"
form = cgi.FieldStorage()
snippet_name = form.getvalue('snippet_name')
snippet_code = form.getvalue('snippet_code')
mode = form.getvalue('snippet_code')
lines=[]
lines=snippet_code.split('\n')
s=''
with open("java.js") as infile:
    for line in infile:
		if line.strip("\n")== "##\\n\\":
			s+=line
			line3 = next(infile)
			s+=line3
			if line3.strip("\n")== "## Myadditions\\n\\":
				s+="snippet "+snippet_name+"\\n\\"+"\n"
				for line2 in lines:
					s+=line2+"\\n\\"+"\n"
		else:
			s+=line
			
with open("java.js","w") as outfile:
	outfile.write(s)
