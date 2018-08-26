from bs4 import BeautifulSoup
import urllib.request

def get_soup(page_url):
	page = urllib.request.urlopen(page_url)
	soup = BeautifulSoup(page, 'html.parser')
	return soup

if __name__ == '__main__':
	soup = get_soup('https://www.azlyrics.com/e/elliottsmith.html')
	print(soup.prettify())