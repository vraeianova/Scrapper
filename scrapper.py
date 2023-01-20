from bs4 import BeautifulSoup
from urllib.request import urlopen,Request
import ssl
import requests


class GhostManga:
	def __init__(self):
		self.url = None
		self.headers = None
		self.__disable_certificate()
		self.__set_headers()
		

	def __disable_certificate(self):
			
		ssl._create_default_https_context = ssl._create_unverified_context
		
	def __set_headers(self):
		browser_headers={
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
			'Cache-Control': 'max-age=0',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
		}
		self.headers = browser_headers

		return True
			
	def set_manga_url(self,url):
		self.url = url
		print('url setted correctly!')
		return True
		
	def __extract_from_container(self,image_container):
		img_tags = image_container.find_all('img', class_='lazyload')
		img_srcs = [img['data-src'] for img in img_tags]
		return img_srcs

	def download_images(self,extracted_urls):
		print('Downloading images...')
		for index,image_url in enumerate(extracted_urls):
			req = Request(image_url, headers=self.headers)
			image = urlopen(req).read()

			with open(f"Inuyasha-{index}.webp", "wb") as f:
				f.write(image)
		return True

	def get_chapter(self):		
		response = requests.get(self.url)

		soup = BeautifulSoup(response.content,'html.parser')

		image_container = soup.find(id='images_chapter')

		extracted_urls = self.__extract_from_container(image_container)
		
		self.download_images(extracted_urls)
		
		return True

def run():
		
	new_manga = GhostManga()
	new_manga.set_manga_url("https://leermanga.net/capitulo/inuyasha-1.00")
	new_manga.get_chapter()


if __name__ == '__main__':
	run()