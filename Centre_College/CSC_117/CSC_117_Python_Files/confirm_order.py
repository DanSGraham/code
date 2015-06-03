#!/usr/bin/python

print "Content-type: text/html\n"

import cgi
import cgitb
import random
cgitb.enable()
form=cgi.FieldStorage()

print "<body bgcolor='green'> <center><h1> THANK YOU FOR YOUR BUSSSSSSSINESSSSSSSS! </h1> <br><br> <a href='http://turing.centre.edu/~daniel.graham/Form_lab.html'> Return to Homepage </a></center> </body>"
