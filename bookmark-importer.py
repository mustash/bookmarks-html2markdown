#!/usr/bin/python
#coding=utf-8

from bs4 import BeautifulSoup as BS
from os.path import exists
import xml.etree.ElementTree as ET
import lxml.html
import sys
import re
reload(sys)
sys.setdefaultencoding("utf-8")

# PHASE 1
# Fault Tolerant
# Blindly parse a Chrome Bookmarks export file looking for H3 to indicate folders
# and A tags with HREF attributes for URLs to add to bookmarks.

inFileName = sys.argv[1]
findStr = open(inFileName, 'r').read()
bs = BS(findStr, 'xml')
for child in bs.descendants:
	if child.name == "Doctype":
		# Ignore
		continue
	if child.name == "H3":
		# Create new Header3 in Markdown: using ###
		# Also create Table Header Row
		print "	"
		print "	"
		print "### ", unicode(child.string).encode("utf-8")
		print "	"
		print "| RESOURCE NAME 	|	URL	|"
		print "|----------------|-------|"
	if child.name == "A":
		print "| ", unicode(child.string).encode("utf-8").replace("|", ":"), "	| ", child['HREF'], " |"	

	# PHASE 2
	# Visit each URL to identify if it is dead/deprecated/broken.
	# Strip out invalid links and only add valid links.
	#t = lxml.html.parse(url)
	#print t.find(".//title").text
	#bs = BS(findStr, 'html')
