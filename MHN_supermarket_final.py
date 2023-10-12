#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

mydb=pymysql.Connect(host="localhost",user="root",password="mohan",database="second_project")
cur=mydb.cursor()

data=cgi.FieldStorage()
customer_order=data.getvalue("cusorderMHN")

query="insert into mhn_supermarket_order values(%s)"
values=[customer_order]
cur.execute(query,values)
mydb.commit()

print('''

<!DOCTYPE html>
            <html lang="en">
            <head>
            <style>
        body{
                background-image:url('11.jpg');
                background-repeat:no-repeat;
                background-size:cover;
                    
        }
        .submit-btn{
	        width: 90px;
	        padding: 10px 30px;
	        cursor: pointer;
	        display: block;
	        margin: auto;
	        background: linear-gradient(to right, #ff105f,#ffad06);
	        border: 0;
	        outline: none;
	        border-radius: 30px;
        }
    </style>
            <title>Webpage Design</title>
            <link rel="stylesheet" href="python_student_final.css">
            </head>
            <body>
            <div class="content">
			<br><br><h1 style="color:red;font-size:50px"><center>Thankyou for purchasing...</center></h1><br>
            <br><br><h1 style="color:blue;font-size:40px"><center>your order will reach you soon..</center></h1><br>
	    </div>
	    <br><br><center><a href='index.html'<button class="submit-btn"><center><h2><ins>Logout</ins></h2></center></button></center></a>
            </body>
            </html>
''')