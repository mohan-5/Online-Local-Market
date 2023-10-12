#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

mydb=pymysql.Connect(host="localhost",user="root",password="mohan",database="second_project")
cur=mydb.cursor()

data=cgi.FieldStorage()
customer_name=data.getvalue("name")
customer_mbl=data.getvalue("mobile")
customer_addr=data.getvalue("address")
customer_area=data.getvalue("area")

query="insert into customer_details values(%s,%s,%s,%s)"
values=[customer_name,customer_mbl,customer_addr,customer_area]
cur.execute(query,values)
mydb.commit()

if customer_area=="kk nagar":
    print('''
    <html>
    <head>
    <style>
        body{
                background-image:url('last.jpg');
                background-repeat:no-repeat;
                background-size:cover;
                    
        }
    </style>
    </head>
    <br><br><center><h1 style="color:yellow;font-size:40px"><ins>Below are our registered shops on your area</ins></h1></center><br><br><br>
    <center><h2 style="color:blue;font-size:30px">MHN Super Market</h2></center>
    <center><a href=MHN_supermarket.html>
    <img src="supermarket.jpeg" width="450px" height="300px" alt="clickable"><br><br>
    </a></center>
    <center><h2 style="color:blue;font-size:30px">KRTY Sweets</h2></center>
     <br><center><a href=KRTY_sweets.html>
    <img src="sweet.jpg" width="450px" height="300px" alt="clickable"><br><br>
    </a></center>
    </html>
    ''')

elif customer_area=="porur":
    print('''
    <html>
    <head>
    <style>
        body{
                background-image:url('last.jpg');
                background-repeat:no-repeat;
                background-size:cover;
                    
        }
    </style>
    </head>
    <br><br><center><h1 style="color:yellow;font-size:40px"><ins>Below are our registered shops on your area</ins></h1></center><br><br><br>
    <center><h2 style="color:blue;font-size:30px">SLA Books Shop</h2></center>
    <center><a href=SLA_bookshop.html>
    <img src="books.jpg" width="450px" height="300px" alt="clickable"><br><br>
    </a></center><br>
    <center><h2 style="color:blue;font-size:30px">SS Sports Shop</h2></center>
     <center><a href=SS_sports.html>
    <img src="sports.jpeg" width="450px" height="300px" alt="clickable"><br><br>
    </a></center>
    </html>
    ''')
