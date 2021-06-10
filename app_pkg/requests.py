from urllib.request import urlopen, Request
from urllib import parse
import json

class Requests:
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

	def post(self, url, info):
		params = parse.urlencode(info)
		params = params.encode('utf-8')
		http_request = Request(url, data=params, headers={'Content-Type': 'application/x-www-form-urlencoded'})
		with urlopen(http_request) as response:
			try:
				json_response = json.load(response)
			except Exception as e:
				json_response = ''
		return json_response
