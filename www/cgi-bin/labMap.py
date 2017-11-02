#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


print "Content-type:text/html"
print                               
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title> Lindon Lab Network Topology! </title>'
print '</head>'
print '<body>'
print '<h2>Lindon Lab Network Topology!</h2>'
print '<form action="/cgi-bin/labMap2.py" method="post">'
print '<input type="submit" value="Topo Print" style="height: 100px; width: 100px; left: 250; top: 250;background-color:yellow;"/>'
print 'Print the latest Map'
print '</form>'
print '<br>' 
print '<form action="/cgi-bin/labMap4.py" method="post">'
print '<input type="submit" value="Topo Check" style="height: 100px; width: 100px; left: 250; top: 250;background-color:pink;"/>'
print 'Check the Network, Update/Print the latest Map'
print '</form>'
print '</body>'
print '</html>'
