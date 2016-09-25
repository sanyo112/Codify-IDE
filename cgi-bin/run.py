#! /usr/bin/python3
import cgi, cgitb, fileinput, subprocess, time, sys ,os ,platform
cgitb.enable()
print("Content-Type: text/html")
print("Access-Control-Allow-Origin: *")
print() 
path=os.path.dirname(os.path.realpath(__file__))[:-7]+"main/projects"
form = cgi.FieldStorage()
file_name = form.getvalue('file_name')
ext = form.getvalue('ext')

if platform.system()=="Windows":
    
    bat_exe=path+"/program.bat"
    with open(bat_exe,"w") as outfile:
        outfile.write("@echo off \n")
        outfile.write("cd /"+"\n")
        outfile.write("cd "+path+"\n")
        if ext == ".py":
                    outfile.write("python "+file_name+".py"+"\n")
        elif ext == ".java":
                        outfile.write("javac "+file_name+".java"+"\n")
                        outfile.write("java "+file_name+"\n")    
        elif ext == ".cpp":
                    outfile.write("g++ "+file_name+".cpp -o "+file_name+"\n")
                    outfile.write(file_name+".exe"+"\n")
                    outfile.write("pause")

    p= subprocess.Popen(bat_exe,stdout=subprocess.PIPE)
    output = p.communicate()[0]
    print(output.decode('ascii'))
      
else :
    
    shell_exe=path+"/program.sh"
    with open(shell_exe,"w") as outfile:
        
        outfile.write("cd "+path+"\n")
        if ext == ".py":
                    outfile.write("python3 "+file_name+".py "+"\n")
        elif ext == ".java":
                        outfile.write("javac "+file_name+".java"+"\n")
                        outfile.write("java "+file_name+"\n")    
        elif ext == ".cpp":
                    outfile.write("g++ "+file_name+".cpp -o "+file_name+"\n")
                    outfile.write(file_name+".exe"+"\n")
                    outfile.write("pause")

    p= subprocess.Popen(['sh',shell_exe],stdout=subprocess.PIPE)
    output = p.communicate()[0]
    print(output.decode('ascii')) 
    
