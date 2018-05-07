# Get free ebooks from Reddit

from bs4 import BeautifulSoup
import feedparser
import requests

url = "https://www.reddit.com/r/freebooks.rss"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0"}

urls = []
books = []
book_data_all = []

d = feedparser.parse(requests.get(url, headers=headers).text)
print(len(d.entries))

for e in d.entries:
	for l in BeautifulSoup(e.description, "html.parser").find_all("a"):
		if l.string == "[link]" and "reddit" not in l["href"]:
			print(e.title)
			print(l["href"])
			urls.append(l["href"])
	print()

print(urls)
print("***GETTING BOOK DATA***")
for u in urls:
	if "amazon" in u:
		book_data = BeautifulSoup(requests.get(u, headers=headers).text, "html.parser")
		
		print(u)

		title = book_data.find("span", attrs={"id":"ebooksProductTitle"}).string

		if "Visit" in book_data.find("span", attrs={"class":"author notFaded"}).find("a", attrs={"class":"a-link-normal"}).string:
			author = book_data.find("span", {"class":"a-size-medium"}).text.replace("\n", "").replace("\t", "").replace("(Author)", "").strip()
		else:
			author = book_data.find("span", attrs={"class":"author notFaded"}).find("a", attrs={"class":"a-link-normal"}).string

		try:
			price = str(book_data.find("td", attrs={"class":"a-color-price"})).replace("\n", "").replace(" ", "").split(">")[1].split("<")[0]
		except TypeError:
			price = book_data.find("td", attrs={"class":"a-color-base a-align-bottom a-text-strike"}).string.strip()

		try:
			book_data_all.append([title, author, price, u])
		except Exception as e:
			print(e)
			continue

print(book_data_all)
print(len(book_data_all))
for b in book_data_all:
	if b[2] == "$0.00":
		books.append(b)
	else:
		continue

print(len(books))
print(str(len(book_data_all) - len(books)) + " paid books")
print(books)
