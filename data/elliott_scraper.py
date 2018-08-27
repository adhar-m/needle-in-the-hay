from bs4 import BeautifulSoup
import urllib.request
import time

def make_soup(page_url):
	"""Take in page url and return soup"""
	page = urllib.request.urlopen(page_url)
	soup = BeautifulSoup(page, 'html.parser')
	return soup

def get_lyrics_from_page(song_page):
	"""Take in an azlyrics page link, and return lyrics string"""
	lyrics = song_page.find('div', attrs={"class": None, "id": None})
	lyrics_text = lyrics.getText()
	return lyrics_text

def get_all_song_lyrics(all_song_links):
	"""Return all song lyrics for a list of az lyrics pages"""
	all_lyrics_text = ""
	for song_page in all_song_links:
		soup = make_soup(song_page)
		all_lyrics_text += get_lyrics_from_page(soup)
		time.sleep(5)
	return all_lyrics_text

def write_csv(lyrics_string):
	"""Split lyrics_string into lines and write to lyrics.csv"""
	lines = lyrics_string.splitlines()
	with open('lyrics.csv','w') as output_file:
		for line in lines:
			if line is not "":
				print (line)
				output_file.write(line)
				output_file.write('\n')

def get_song_links(soup):
	"""Get links to all song pages given artist page soup"""
	all_songs= soup.find_all('a',target='_blank')
	song_links =[]

	for a in all_songs:
		song_links.append("https://www.azlyrics.com/" + a.get('href'))
	all_songs_links = {link.replace('../','') for link in song_links}
	return all_songs_links


if __name__ == '__main__':
	soup = make_soup('https://www.azlyrics.com/e/elliottsmith.html')
	all_songs_links = get_song_links(soup)
	all_lyrics = get_all_song_lyrics(all_songs_links)
	write_csv(all_lyrics)

	
