#!/usr/bin/python

# Get FREE ebooks from O'Reilly Media

from bs4 import BeautifulSoup
import urllib
import os

formats = [".pdf", ".mobi", ".epub"]
pageindex = ["Programming", "Business", "Data", "IoT", "Security", "WebOps"]
pages = ["http://www.oreilly.com/programming/free", "http://www.oreilly.com/business/free", "http://www.oreilly.com/data/free", "http://www.oreilly.com/iot/free", "http://www.oreilly.com/security/free",  "http://www.oreilly.com/webops/free"]
primary = "/home/pi/Documents/Python/ebooks"

all_titles = []

for p in pages:
    source = p
    books_title = []
    books_url = []
    
    print("\n" + pageindex[pages.index(p)] + "\n")
    
    cleanup = BeautifulSoup(urllib.urlopen(source), "html.parser")

    for a in cleanup.select("section a"):
        del a["data-toggle"]
        del a["data-container"]
        del a["data-trigger"]
        del a["data-placement"]
        del a["data-content"]
            
        books_title.append(a["title"])
        all_titles.append(a["title"].encode("utf-8"))
        
        del a["title"]
        
        # Example Link: http://www.oreilly.com/programming/free/microservices-for-java-developers.csp
        
        bb = a["href"].split("/free/")[1].split(".csp")[0] + "." + ".pdf"
        b = source + "/files/" + bb
        
        books_url.append(b.encode("utf-8"))

    os.chdir(primary)
    try:
        for b in books_url:
            filterfile = books_title[books_url.index(b)].replace(" ", "").replace(":", "_").replace("?", "").replace(".", "").replace("'", "").replace("(", "-").replace(")", "")
            for f in formats:
                if f == ".mobi":
                    os.chdir(primary + "/mobi")
                    os.system("curl -SsL " + b + " -o " + filterfile+ f)
                    print("Downloaded " + filterfile + f)
                elif f == ".epub":
                    os.chdir(primary + "/epub")
                    os.system("curl -SsL " + b + " -o " + filterfile + f)
                    print("Downloaded " + filterfile + f)
                elif f == ".pdf":
                    os.chdir(primary + "/pdf")
                    os.system("curl -SsL " + b + " -o " + filterfile + f)
                    print("Downloaded " + filterfile + f)
    except UnicodeEncodeError:
        continue
    except IndexError:
        continue
    
    print(books_title)
    
print("A total of " + str(len(all_titles)) + " books were downloaded.")
print(all_titles)
