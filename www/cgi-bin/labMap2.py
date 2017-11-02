#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import cgi, cgitb

# form = cgi.FieldStorage()

# site_name = form.getvalue('name')
#site_url  = form.getvalue('url')
import os,sys,time
#os.popen("python /var/www/cgi-bin/labMap3.py")
#os.popen("touch /var/www/html/images/zhu")
#subprocess.call(['touch', 'zhu'])
#f = open("/var/www/html/images/zhu","w")
#f.close()
i =0
tag = True
while True:
    if not os.path.exists("/var/www/html/images/map.png"):
        tag = False
        time.sleep(1)
        i += 1
        if i == 10:
            break
    else:
    	tag = True
	break

if tag:
	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>"
	print "<meta charset=\"utf-8\">"
	print "<title>Lindon Topo Result </title>"
	print "</head>"
	print "<body>"
	print "<img src='http://10.94.193.95/images/map.png'>"
	print "</body>"
	print "</html>"
else:
	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>"
	print "<meta charset=\"utf-8\">"
	print "<title>Lindon Topo Result </title>"
	print "</head>"
	print "<body>"
	print "<h2>Oooops! Something Go Wrong! Contact:: yijunzhu@cisco.com</h2>"
	print "</body>"
	print "</html>"
