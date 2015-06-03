#!/usr/bin/python

print "Content-type: text/html\n"

import cgi
import cgitb; cgitb.enable() #helps w/ debugging
form = cgi.FieldStorage()

print "<OL>"

for element in form.keys():
    print "<LI>" + element + "=" + str(form.getlist(element)) + "</LI>"

print "</OL>"
