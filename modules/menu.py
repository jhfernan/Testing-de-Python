

class Menu:
	title = ''
	error = ''
	results = ''
	question = ''

	def __init__(self, title):
		self.title = title
		self.question += 'What data would you like to see? (Enter "Q" to quit)'
		self.question += '\nPress \'U\' for the list of users'
		self.question += '\nPress \'I\' for the list of items'
		self.question += '\n=> '

	def check_response(self, response):
		possible_menu_items = ['u', 'i']
		return response.lower() in possible_menu_items

	def get_url(self, response):
		response = response.lower()
		if response == 'u':
			return 'https://api-testing-j-m.herokuapp.com/api/v1/users'
		elif response == 'i':
			return 'https://api-testing-j-m.herokuapp.com/api/v1/items'

	def setup_results_screen(self, response, json):
		response = response.lower()
		if response == 'u':
			self.results = 'Here is a list of the current users and their email:\n'
			for item in json:
				self.results += '{}: {}\n'.format(item['name'], item['email'])
		elif response == 'i':
			self.results = 'Here is a list of the current items and their info:\n'
			for item in json:
				self.results += item['name'] + ': '
				self.results += item['brand']
				self.results += '\nColor: '
				self.results += item['color']
				self.results += '\nStorage: '
				try:
					self.results += item['storage']
				except Exception as e:
					self.results += 'N\A'
				self.results += '\n\n'
