# Free Books

try:
  from HTMLParser import HTMLParser as h
except ImportError:
  from html.parser import HTMLParser as h
  
from bs4 import BeautifulSoup as bs
import feedparser as fp
import requests
import urllib2

url = "https://reddit.com/r/freebooks.rss"
passes = 0
fails = 0

bookurls = []
books = {}
titles = {}

r = requests.get(url, headers={"User-Agent": ""}) # Fill the User-Agent header out!

rss = r.text
d = fp.parse(rss)

print(len(d.entries))
for e in d.entries:
	print(e.title)
	print(e.link)
	print(" ")
	print(e.description)
	print("**LINK**")
	cleanup = bs(e.description, "html.parser")
	for a in cleanup.select("table td span a"): # Gets the links
   		if "[comments]" in a:
   			continue
   		else:
   			print(a)
   			bookurls.append(a["href"].encode("ascii"))
	print(" ")
	print(" ")

print("***Book URLS***")
print(bookurls)
print("****Book Title Fetch Status****")

for l in bookurls:
	try:
		parse = bs(urllib2.urlopen(l), "html.parser")
		books[l] = parse.title.string
		print("PASS")
		passes = passes + 1
		if "amazon" in l.split(".")[1]:
			titles[l] = parse.find("span", id="ebooksProductTitle").string

	except:
		print("FAIL")
		fails = fails + 1

print("***Website Title***")
print(books)
print("***Book Titles***")
print(titles)
