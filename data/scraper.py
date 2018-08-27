from bs4 import BeautifulSoup
import urllib.request

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
	return all_lyrics_text

def write_csv(lyrics_string):
	"""Split lyrics_string into lines and write to csv"""
	lines = lyrics_string.splitlines()
	with open('lyrics.csv','w') as output_file:
		for line in lines:
			if line is not "":
				print (line)
				output_file.write(line)
				output_file.write('\n')

if __name__ == '__main__':
	all_song_links = [
	'https://www.azlyrics.com/lyrics/elliottsmith/romancandle.html',
	'https://www.azlyrics.com/lyrics/elliottsmith/condorave.html',
	'https://www.azlyrics.com/lyrics/elliottsmith/noname1.html',
	]

	all_lyrics = get_all_song_lyrics(all_song_links)
	write_csv(all_lyrics)

