#!C:\Program Files\Python37\python
def calculate(a,b,c):
    if c=='+':
       print("after addition:",(int(a)+int(b)))
    elif c=='-':
       print("afetr substration:",(int(a)-int(b)))
    elif c=='*':
       print("multiplication:",(int(a)*int(b)))
    elif c=='/':
       print("division:",(int(a)/int(b)))
    elif c=='%':
       print("modulo:",(int(a)%int(b)))
import cgi
print("content-type:text/html\n")
print("<html>")
print("<head>")
print("</head>")
print("<body>")
form=cgi.FieldStorage()
a=form.getvalue("first")
b=form.getvalue("second")
op=form.getvalue("operation")
print('<form method="post" action="arthmetic.py">')
print('<p>Enter first number:<input type="text" name="first"/></p>')
print('<p>Enter second number:<input type="text" name="second"/></p>')
print('<p>selection operation:</p><select name="operation"><option>+</option><option>-</option><option>/</option><option>%</option></select>')
print('<input type="submit" value="submit"/>')
print('<br>')
print('</body>')
print('</html>')
print("\n")

calculate(a,b,op)
       
