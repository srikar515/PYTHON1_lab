#!C:\Program Files\Python37\python
def sort_func(a):
    l=a.split(" ")
    l.sort()
    a=" ".join(l)
    print(a)
    
import cgi
print("content-type:text/html\n")
print("<html>")
print("<head>")
print("</head>")
print("<body>")
form=cgi.FieldStorage()
a=form.getvalue("first")
print('<form method="post" action="sort_func.py">')
print('<p>Enter string:<input type="text" name="first"/></p>')
print('<input type="submit" value="submit"/>')
print('<br>')
print('</body>')
print('</html>')
print("\n")

sort_func(a)
       
