from urllib.request import urlopen, Request
import json

class APIHandler:
	url = 'http://api.openweathermap.org/data/2.5/weather?q=orlando&appid=8816628b6017926fbf7cc60538485608'

	def get(self, url = ''):
		if not url:
			url = self.url
		http_request = Request(url, headers={'Accept': 'application/json'})
		with urlopen(http_request) as response:
			try:
				json_response = json.load(response)
			except Exception as e:
				json_response = ''
		return json_response
