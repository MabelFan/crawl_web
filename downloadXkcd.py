#!/Users/mabelfan/anaconda3/bin/python3
# downloadXkcd.py - Downloads every single Xkcd image.

import requests, bs4, os

url = 'http://xkcd.com'    # starting url
os.makedirs('xkcd', exist_ok=True)   # store images in ./xkcd
while not url.endswith('#'):
	print('Downloading page %s...' %url)
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7'}
	page = requests.get(url, headers=headers)
	page.raise_for_status()

	soup = bs4.BeautifulSoup(page.text, 'html.parser')
	# print(soup.title)
	comicElem = soup.select('#comic img')   # Find the url of the comic image.
	if comicElem == []:
		print('Could not find comic image.')
	else:
		comicUrl = comicElem[0].get('src')
		print('Downloading the image %s...' % (comicUrl))
		imgs = requests.get("https:" + comicUrl)
		imgs.raise_for_status()

		imagefile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		# os.path.basename(comicUrl) return the image name with .png
		# use os.path.join to combine the file name to be 'xkcd'+'image name'
		# then call open function to create the file under the path
		for chunk in imgs.iter_content(100000):
			imagefile.write(chunk)
		imagefile.close()

		find_prev = soup.select('a[rel="prev"]')[0]
		url = 'http://xkcd.com' + find_prev.get('href')

print('Done.')






