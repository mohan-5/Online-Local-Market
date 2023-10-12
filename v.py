#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql
mydb=pymysql.Connect(host="localhost",user="root",password="mohan",database="second_project")
cur=mydb.cursor()

data=cgi.FieldStorage()
vendor_shop=data.getvalue("shop")

if vendor_shop=="mhn_supermarket":

    print('''
        <style>
        body{
                background-image:url('last.jpg');
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
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Webpage Design</title>
        <link rel="stylesheet" href="style.css">
        </head>
        <body>
        <div class="navbar">
		    <div class="icon">
			    <br><h1 class="logo">ONLINE MARKET</h1>
		    </div>
		    <div class="menu">
			    <ul>
				    <li><a href="#">HOME</a></li>
				    <li><a href="#">ABOUT</a></li>
				    <li><a href="#">SERVICE</a></li>
				    <li><a href="#">COURSE</a></li>
				    <li><a href="#">CONTACT</a></li>
			    </ul>
		    </div>			
    	</div>
	<br><br><br><br><hr>
	</body>
	</html>
	''')
    
    cur.execute("select * from customer_details")
    var=cur.fetchall()
    for i in var:
        customer_name=i[0]
        customer_mobile=i[1]
        customer_address=i[2]
        customer_area=i[3]
    
    cur.execute("select * from mhn_supermarket_order")
    var=cur.fetchall()

    for i in var:
        mhn_customer_order=i[0]
    
    print('''

        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Webpage Design</title>
        <link rel="stylesheet" href="style.css">
        <style>
        th,td{
	    border:1px solid black;
	    border-collapse:collapse;
	    background-color:pink;
	    border-radius:10px;
	    border-style:ridge;
	    border-color:blue;
	    padding:15px;
	    border-spacing:40px;
        }
        tr:nth-child(even){
	    background-color:blue;
        }
        </style>
        </head>
        <body>
        <table style="width:100%">
	    <caption style="font-size:40px;color:blue"><center><ins><b>Customer Order Detail</b></ins></center></caption><br>
	    <tr style="height:50px">
		    <th style="width:10%;height:50%">Customer Name</th>
		    <th style="width:10%">Customer Mobile Number</th>
		    <th style="width:15%">Customer Address</th>
		    <th style="width:15%">Customer Area</th>
		    <th style="width:15%">Customer Order</th>
		</tr>
	    <tr>''')
    print("<td><center>",customer_name,"</center></td>")
    print("<td><center>",customer_mobile,"</center></td>")
    print("<td><center>",customer_address,"</center></td>")
    print("<td><center>",customer_area,"</center></td>")
    print("<td><center>",mhn_customer_order,"</center></td>")
    print('''
        </tr>
        </table>
        
	    <br><br><br><br><br><br><br><br><br><center><a href='index.html'<button class="submit-btn"><center><h2><ins>Logout</ins></h2></center></button></center></a>
        </body>
        </html>
        ''')
elif vendor_shop=="krty_sweets":

    print('''
        <style>
        body{
                background-image:url('last.jpg');
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
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Webpage Design</title>
        <link rel="stylesheet" href="style.css">
        </head>
        <body>
        <div class="navbar">
		    <div class="icon">
			    <br><h1 class="logo">ONLINE MARKET</h1>
		    </div>
		    <div class="menu">
			    <ul>
				    <li><a href="#">HOME</a></li>
				    <li><a href="#">ABOUT</a></li>
				    <li><a href="#">SERVICE</a></li>
				    <li><a href="#">COURSE</a></li>
				    <li><a href="#">CONTACT</a></li>
			    </ul>
		    </div>			
    	</div>
	<br><br><br><br><hr>
	</body>
	</html>
	''')
    
    cur.execute("select * from customer_details")
    var=cur.fetchall()
    for i in var:
        customer_name=i[0]
        customer_mobile=i[1]
        customer_address=i[2]
        customer_area=i[3]
    
    cur.execute("select * from krty_sweets_order")
    var=cur.fetchall()

    for i in var:
        krty_customer_order=i[0]
    
    print('''

        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Webpage Design</title>
        <link rel="stylesheet" href="style.css">
        <style>
        th,td{
	    border:1px solid black;
	    border-collapse:collapse;
	    background-color:pink;
	    border-radius:10px;
	    border-style:ridge;
	    border-color:blue;
	    padding:15px;
	    border-spacing:40px;
        }
        tr:nth-child(even){
	    background-color:blue;
        }
        </style>
        </head>
        <body>
        <table style="width:100%">
	    <caption style="font-size:40px;color:blue"><center><ins><b>Customer Order Detail</b></ins></center></caption><br>
	    <tr style="height:50px">
		    <th style="width:10%;height:50%">Customer Name</th>
		    <th style="width:10%">Customer Mobile Number</th>
		    <th style="width:15%">Customer Address</th>
		    <th style="width:15%">Customer Area</th>
		    <th style="width:15%">Customer Order</th>
		</tr>
	    <tr>''')
    print("<td><center>",customer_name,"</center></td>")
    print("<td><center>",customer_mobile,"</center></td>")
    print("<td><center>",customer_address,"</center></td>")
    print("<td><center>",customer_area,"</center></td>")
    print("<td><center>",krty_customer_order,"</center></td>")
    print('''
        </tr>
        </table>
        
	    <br><br><br><br><br><br><br><br><br><center><a href='index.html'<button class="submit-btn"><center><h2><ins>Logout</ins></h2></center></button></center></a>
        </body>
        </html>
        ''')

elif vendor_shop=="sla_books":

    print('''
        <style>
        body{
                background-image:url('last.jpg');
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
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Webpage Design</title>
        <link rel="stylesheet" href="style.css">
        </head>
        <body>
        <div class="navbar">
		    <div class="icon">
			    <br><h1 class="logo">ONLINE MARKET</h1>
		    </div>
		    <div class="menu">
			    <ul>
				    <li><a href="#">HOME</a></li>
				    <li><a href="#">ABOUT</a></li>
				    <li><a href="#">SERVICE</a></li>
				    <li><a href="#">COURSE</a></li>
				    <li><a href="#">CONTACT</a></li>
			    </ul>
		    </div>			
    	</div>
	<br><br><br><br><hr>
	</body>
	</html>
	''')
    
    cur.execute("select * from customer_details")
    var=cur.fetchall()
    for i in var:
        customer_name=i[0]
        customer_mobile=i[1]
        customer_address=i[2]
        customer_area=i[3]
    
    cur.execute("select * from sla_books_order")
    var=cur.fetchall()

    for i in var:
        sla_customer_order=i[0]
    
    print('''

        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Webpage Design</title>
        <link rel="stylesheet" href="style.css">
        <style>
        th,td{
	    border:1px solid black;
	    border-collapse:collapse;
	    background-color:pink;
	    border-radius:10px;
	    border-style:ridge;
	    border-color:blue;
	    padding:15px;
	    border-spacing:40px;
        }
        tr:nth-child(even){
	    background-color:blue;
        }
        </style>
        </head>
        <body>
        <table style="width:100%">
	    <caption style="font-size:40px;color:blue"><center><ins><b>Customer Order Detail</b></ins></center></caption><br>
	    <tr style="height:50px">
		    <th style="width:10%;height:50%">Customer Name</th>
		    <th style="width:10%">Customer Mobile Number</th>
		    <th style="width:15%">Customer Address</th>
		    <th style="width:15%">Customer Area</th>
		    <th style="width:15%">Customer Order</th>
		</tr>
	    <tr>''')
    print("<td><center>",customer_name,"</center></td>")
    print("<td><center>",customer_mobile,"</center></td>")
    print("<td><center>",customer_address,"</center></td>")
    print("<td><center>",customer_area,"</center></td>")
    print("<td><center>",sla_customer_order,"</center></td>")
    print('''
        </tr>
        </table>
        
	    <br><br><br><br><br><br><br><br><br><center><a href='index.html'<button class="submit-btn"><center><h2><ins>Logout</ins></h2></center></button></center></a>
        </body>
        </html>
        ''')

elif vendor_shop=="ss_sports":

    print('''
        <style>
        body{
                background-image:url('last.jpg');
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
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Webpage Design</title>
        <link rel="stylesheet" href="style.css">
        </head>
        <body>
        <div class="navbar">
		    <div class="icon">
			    <br><h1 class="logo">ONLINE MARKET</h1>
		    </div>
		    <div class="menu">
			    <ul>
				    <li><a href="#">HOME</a></li>
				    <li><a href="#">ABOUT</a></li>
				    <li><a href="#">SERVICE</a></li>
				    <li><a href="#">COURSE</a></li>
				    <li><a href="#">CONTACT</a></li>
			    </ul>
		    </div>			
    	</div>
	<br><br><br><br><hr>
	</body>
	</html>
	''')
    
    cur.execute("select * from customer_details")
    var=cur.fetchall()
    for i in var:
        customer_name=i[0]
        customer_mobile=i[1]
        customer_address=i[2]
        customer_area=i[3]
    
    cur.execute("select * from ss_sports_order")
    var=cur.fetchall()

    for i in var:
        ss_customer_order=i[0]
    
    print('''

        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Webpage Design</title>
        <link rel="stylesheet" href="style.css">
        <style>
        th,td{
	    border:1px solid black;
	    border-collapse:collapse;
	    background-color:pink;
	    border-radius:10px;
	    border-style:ridge;
	    border-color:blue;
	    padding:15px;
	    border-spacing:40px;
        }
        tr:nth-child(even){
	    background-color:blue;
        }
        </style>
        </head>
        <body>
        <table style="width:100%">
	    <caption style="font-size:40px;color:blue"><center><ins><b>Customer Order Detail</b></ins></center></caption><br>
	    <tr style="height:50px">
		    <th style="width:10%;height:50%">Customer Name</th>
		    <th style="width:10%">Customer Mobile Number</th>
		    <th style="width:15%">Customer Address</th>
		    <th style="width:15%">Customer Area</th>
		    <th style="width:15%">Customer Order</th>
		</tr>
	    <tr>''')
    print("<td><center>",customer_name,"</center></td>")
    print("<td><center>",customer_mobile,"</center></td>")
    print("<td><center>",customer_address,"</center></td>")
    print("<td><center>",customer_area,"</center></td>")
    print("<td><center>",ss_customer_order,"</center></td>")
    print('''
        </tr>
        </table>
        
	    <br><br><br><br><br><br><br><br><br><center><a href='index.html'<button class="submit-btn"><center><h2><ins>Logout</ins></h2></center></button></center></a>
        </body>
        </html>
        ''')

    