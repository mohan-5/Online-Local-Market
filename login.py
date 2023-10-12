#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

mydb=pymysql.Connect(host="localhost",user="root",password="mohan",database="second_project")
cur=mydb.cursor()

data=cgi.FieldStorage()
logmail=data.getvalue("loginmail")
logpass=data.getvalue("loginpswd")

cur.execute("select * from member_details")
var=cur.fetchall()

for i in var:    
    if i[1]==logmail and i[2]==logpass:
            print('''
            <style>
            body{
                    background-image:url('multichoice2.jpg');
                    background-repeat:no-repeat;
                    background-size:cover;
            }
            </style>
            <!DOCTYPE html>
            <html>
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
            .navbar{
                    width: 1200px;
                    height:50px;
                    margin: auto;
            }

            .icon{
                    width: 200px;
                    float: left;
                    height: 40px;
            }

            .logo{
                    color: #ff7200;
                    font-size: 55px;
                    font-family: Arial;
                    padding-left: 20px;
                    float: left;
                    padding-top: -20px;
            }
            .menu{
                    width: 400px;
                    float: left;
                    height: 50px;
            }

            ul{
                    float: left;
                    display: flex;
                    justify-content: center;
                    align-items: center;
            }

            ul li{
                    list-style: none;
                    margin-left: 55px;
                    margin-top: 30px;
                    font-size: 25px;
            }

            ul li a{
                    text-decoration: none;
                    color: #fff;
                    font-family: Arial;
                    font-weight: bold;
                    transition: 0.4s ease-in-out;
            }

            ul li a:hover{
                    color: #ff7200;
            }
            
            .block{
                position: relative;
                width: 500px;
                height: 200px;
                top: -30px;
                background: transparent;
                border: 2px solid rgba(255, 255, 255, .5);
                border-radius: 30px;
                backdrop-filter: blur(20px);
                box-shadow: 0 0 30px rgba(0, 0, 0, .5);
                color: black;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .block:hover {
              background-color: #F67E64;
              color: black;
            }
            </style>
            </head>
            
            <body>
            <div class="navbar">
			<div class="icon">
				<h1 class="logo">ONLINE MARKET</h1>
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
	    <br><br><br><br><br><br><hr>
            </head>
            <body>

            <br><center><h1 style="color:red;font-size:50px"><ins>Welcome to your wish list</ins></h1></center>
            <center><h2 style="color:red;font-size:40px"> kindly fill the following details</h2></center><br><br>
            <form action=shop_list.py method="post">
                <center><label style="color:blackfont-size:20px"><b> Enter your name:</b></label>
                <input type="text" class="input-field" name="name" placeholder="User Name" required></center><br><br>
                <center><label style="color:blackfont-size:20px"><b> Enter your Mobile number:</b></label>
                <input type="phone" class="input-field" name="mobile" placeholder="Enter mobile number" required></center><br><br>
                <center><label style="color:blackfont-size:20px"><b> Enter your Address:</b></label>
                <input type="text" class="input-field" name="address" placeholder="Address" required></center><br><br>
                <center><label for="area" style="color:blackfont-size:20px"><b>Choose your area:</b></label>
                <select name="area" id="area">
                <option value="select area">---select area---</option>
                <option value="kk nagar">KK Nagar</option>
                <option value="porur">Porur</option>
                </select></center><br><br>
                <center><button type="submit" class="submit-btn">Submit</button></center>
                </form>


            </body>
            </html>
        
            ''')
cur.execute("select * from vendor_details")
rec=cur.fetchall()

for i in rec:    
    if i[1]==logmail and i[2]==logpass:
        
        print('''
        <style>
        body{
                background-image:url('multichoice2.jpg');
                background-repeat:no-repeat;
                background-size:cover;
                    
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
        print('''
        <html>
        <body>
        <div class="content">
		    <h1 style="font-size:40px;color:red"><center><ins>Welcome to the Vendor page</ins></center></h1>
		    <hr><br>
	</div>
	</body>
	</html>
	''')
        print('''

        <!DOCTYPE html>
        <html lang="en">
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
        <br><br>
	<label style="font-size:40px;color:blue"><center><ins><b>Order Details</b></ins></center></label><br><br>
	<form action=v.py method="post">
                <center><label for="shop";style="font-size:40px">Select your Shop to see order details:</label>
                <select name="shop" id="shop">
                <option value="select shop">---select shop---</option>
                <option value="mhn_supermarket">MHN Super Market</option>
                <option value="krty_sweets">KRTY Sweets</option>
                <option value="sla_books">SLA Book Shop</option>
                <option value="ss_sports">SS Sports Shop</option>
                </select></center><br><br><br><br>
                <center><button type="submit" class="submit-btn" style="width:10%"><b>Submit</b></button></center>
        </form>
        </body>
        </html>
        ''')
            
