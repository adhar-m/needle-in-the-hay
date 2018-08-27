from bs4 import BeautifulSoup
import urllib.request

def get_soup(page_url):
	page = urllib.request.urlopen(page_url)
	soup = BeautifulSoup(page, 'html.parser')
	return soup


def get_links():
	all_songs= soup.find_all('a',target='_blank')
	song_links =[]

	for a in all_songs:
		song_links.append("https://www.azlyrics.com/"+a.get('href'))
	all_songs_links = {link.replace('../','') for link in song_links}
	return all_songs_links


if __name__ == '__main__':
	soup = get_soup('https://www.azlyrics.com/e/elliottsmith.html')
	all_songs_links = get_links()
	
