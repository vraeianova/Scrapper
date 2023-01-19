import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


def run():
	for i in range(1,6):
		# response = requests.get('http://xkcd.com/{}'.format(i))
		response = requests.get('https://submangas.net/manga/kimi-o-sasou-uzuki-ana/3/8')
        soup = BeautifulSoup(response.content,'html.parser')
		image_container = soup.find(id='ppp')

		image_url = image_container.find('img')['src']
		image_name = image_url.split('/')[-1]
		print('Descargando la imagen')
		urlretrieve('https:{}'.format(image_url),image_name)
		# urlretrieve(f'https:{image_url}', image_name)

		print('Imagen descargada correctamente')

if __name__ == '__main__':
	run()