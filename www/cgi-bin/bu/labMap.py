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
print '<input type="submit" value="Topo Print" />'
print '</form>'
print '<form action="/cgi-bin/labMap3.py" method="post">'
print '<input type="submit" value="Topo Check" />'
print '</form>'
print '</body>'
print '</html>'
