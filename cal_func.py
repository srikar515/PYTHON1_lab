#!C:\Program Files\Python37\python
import calendar
def calculate(a,b):
    c=calendar.HTMLCalendar(calendar.SUNDAY)
    str1=c.formatmonth(int(a),int(b))
    print(str1)


import cgi
print("content-type:text/html\n")
print("<html>")
print("<head>")
print("</head>")
print("<body>")
form=cgi.FieldStorage()
a=form.getvalue("operation1")
b=form.getvalue("operation2")
print('<form method="post" action="cal_func.py">')
print('<p>selection operation:</p><select name="operation1"><option>2017</option><option>2018</option><option>2019</option><option>2020</option></select>')
print('<p>selection operation:</p><select name="operation2"><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7</option><option>8</option><option>9</option><option>10</option><option>11</option><option>12</option></select>')
print('<input type="submit" value="submit"/>')
print('<br>')
print('</body>')
print('</html>')
print("\n")

calculate(a,b)
       
