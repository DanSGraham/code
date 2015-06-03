#!/usr/bin/python

print "Content-type: text/html\n"

import cgi
import cgitb
cgitb.enable()
form=cgi.FieldStorage()


#currently doesn't check for the check boxes.

try:
    #Creates a dictionary with the values equal to the total cost of each item
    order={}
    order['Mice']= int(form.getvalue('Mice_quantity', 0)) * 1
    order['Bedding']= int(form.getvalue('Bedding_quantity', 0)) * 5
    order['5 Gallon Tank']= int(form.getvalue('5Gallon_tank_quantity', 0)) * 30
    order['10 Gallon Tank']= int(form.getvalue('10Gallon_tank_quantity', 0)) * 50
    order['15 Gallon Tank']= int(form.getvalue('15Gallon_tank_quantity', 0)) * 70
    order['Heating Lamp']= int(form.getvalue('Heating_lamp_quantity', 0)) * 20
    if order['Mice'] %2 != 0:
        order['Mice'] = order["Mice"]/2 + 1
    else:
        order['Mice'] = order["Mice"]/2
    x = 0
except:
    print """<head>
    <title>
    Snakesssssssssssssandmore</title>
    </head>
    <body bgcolor='gray'>
    <form name="orderFORM" action="place_order.py" method="get">
    <br>
    <h1><center>Salazar's Snake Emporium</center></h1>
    <br>
    <p>
    <font size='5'>Welcome to <b>Salazar's Snake Emporium</b>, your supplier of <i>premium</i> snake supples. We sell the <u>highest</u> quality of snake food, snake bedding, snake tanks, and heating lamps; everything a first time snake owner needs!</p>
    </font>
    <br>
    <center><table><tr><td><center><h2> <font color='green'><i>ON SSSSSSSSALE NOW!</i></font></h2></center></td></tr>
    <tr><center><td><image width='640' height='480' src='lab_mice.jpg'></td></center></tr>
    <tr><td><center><h3>MICE! Buy one get one <b>FREE!</b></h3></center></td></tr></table></center>
    <br><center><a href = 'http://en.wikipedia.org/wiki/File:Lightmatter_lab_mice.jpg'> Image Source </a></center>
    <h2> What snake supplies would you like to order?</h2>
    <br>
    <table border='1'><tr><td>Item</td><td>Quantity</td></tr>
    <tr><td>Mice $1 each </td> <td><input type="text" name="Mice_quantity"></td></tr>
    <tr><td>Bedding $5 per bag </td> <td><input type="text" name="Bedding_quantity"></td></tr>
    <tr><td>5 Gallon Tank $30 </td> <td><input type="text" name="5Gallon_tank_quantity"></td></tr>
    <tr><td>10 Gallon Tank $50 </td> <td><input type="text" name="10Gallon_tank_quantity"></td></tr>
    <tr><td>15 Gallon Tank $70 </td> <td><input type="text" name="15Gallon_tank_quantity"></td></tr>
    <tr><td>Heating Lamp $20 </td> <td><input type="text" name="Heating_lamp_quantity"></td></tr>

    </table>
    <br>
    <table>
    <tr><td>What reptiles do you own?</td></tr>
    <tr><td><input type='checkbox' name='reptile' value='snake'> A snake </td></tr>
    <tr><td><input type='checkbox' name='reptile' value='lizard'> A lizard </td></tr>
    <tr><td><input type='checkbox' name='reptile' value='dragon'> A dragon </td></tr>
    </table>
    <br>
    <p> Would you like to sign up for our daily newsletter?</p>
    <input type='radio' name='newsletter' value='yes' checked> Yes!
    <br>
    <input type='radio' name='newsletter' value='no'> No thanks.
    <br>
    <br>

    <input type='submit' value="Place Order">
    <br>
    <font color='red'>Please enter a positive number quantity!</font>
    </body>
    """
    x = 1
if sum(order.values()) <= 0 and x != 1:
    print """<head>
    <title>
    Snakesssssssssssssandmore</title>
    </head>
    <body bgcolor='gray'>
    <form name="orderFORM" action="place_order.py" method="get">
    <br>
    <h1><center>Salazar's Snake Emporium</center></h1>
    <br>
    <p>
    <font size='5'>Welcome to <b>Salazar's Snake Emporium</b>, your supplier of <i>premium</i> snake supples. We sell the <u>highest</u> quality of snake food, snake bedding, snake tanks, and heating lamps; everything a first time snake owner needs!</p>
    </font>
    <br>
    <center><table><tr><td><center><h2> <font color='green'><i>ON SSSSSSSSALE NOW!</i></font></h2></center></td></tr>
    <tr><center><td><image width='640' height='480' src='lab_mice.jpg'></td></center></tr>
    <tr><td><center><h3>MICE! Buy one get one <b>FREE!</b></h3></center></td></tr></table></center>
    <br><center><a href = 'http://en.wikipedia.org/wiki/File:Lightmatter_lab_mice.jpg'> Image Source </a></center>
    <h2> What snake supplies would you like to order?</h2>
    <br>
    <table border='1'><tr><td>Item</td><td>Quantity</td></tr>
    <tr><td>Mice $1 each </td> <td><input type="text" name="Mice_quantity"></td></tr>
    <tr><td>Bedding $5 per bag </td> <td><input type="text" name="Bedding_quantity"></td></tr>
    <tr><td>5 Gallon Tank $30 </td> <td><input type="text" name="5Gallon_tank_quantity"></td></tr>
    <tr><td>10 Gallon Tank $50 </td> <td><input type="text" name="10Gallon_tank_quantity"></td></tr>
    <tr><td>15 Gallon Tank $70 </td> <td><input type="text" name="15Gallon_tank_quantity"></td></tr>
    <tr><td>Heating Lamp $20 </td> <td><input type="text" name="Heating_lamp_quantity"></td></tr>

    </table>
    <br>
    <table>
    <tr><td>What reptiles do you own?</td></tr>
    <tr><td><input type='checkbox' name='reptile' value='snake'> A snake </td></tr>
    <tr><td><input type='checkbox' name='reptile' value='lizard'> A lizard </td></tr>
    <tr><td><input type='checkbox' name='reptile' value='dragon'> A dragon </td></tr>
    </table>
    <br>
    <p> Would you like to sign up for our daily newsletter?</p>
    <input type='radio' name='newsletter' value='yes' checked> Yes!
    <br>
    <input type='radio' name='newsletter' value='no'> No thanks.
    <br>
    <br>

    <input type='submit' value="Place Order">
    <br>
    <font color='red'>Please enter a positive number quantity!</font>
    </body>
    """
elif x != 1:
    reptiles = form.getlist('reptile')
    print "<body>"
    for key in order.keys():
        if order[key] == 0:
            del order[key]
    print "<h1>Your current order.</h1><br><p><u>Order:</u></p>"
    print "<br> <table border = '1'>"
    print "<tr><td>Item</td> <td> Price </td></tr> "
    for key in order:
        print "<tr><td>" + key + "</td><td> $" + str(order[key]) + "</td></tr>"
    print '</table>'
    print "<br>"
    print "<hr>"
    print "<br>"
    print "Total: $" + str(sum(order.values()))
    print "<br>"
    
    if reptiles != []:
        print "<p> We hope this is enough for your "

        for reptile in reptiles:
            if reptile == 'dragon':
                print "...DRAGON!? Who let you have a dragon?"
            elif reptile == reptiles[-1]:
                print reptile
            else:
                print reptile + " and"
    print ". </p> <br> <br>"
    
        
    if form.getvalue('newsletter') == 'yes':
        print "Thank you for signing up for our newsletter! <br> "
    print """<form name="confirmationForm" action="confirm_order.py" method="get">"""
    print """<input type='submit' value="Confirm Order">"""
    print "</body>"
    

