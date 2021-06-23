import getpass
from .menu import Menu
from .requests import Requests


class User(Menu, Requests):
	id = None
	name = None
	email = None
	bio = None
	admin = False
	token = None

	def login_user(self):
		# Get users email
		self.default_menu('Please Login')
		users_email = input('\t\t\tEmail: ')

		# Get users password
		self.default_menu('Please Login')
		print('\t\t\tEmail: {}'.format(users_email))
		users_password = getpass.getpass('\t\t\tPassword: ')

		# Prepare data for post request to API to authenticate
		data = {"email": users_email, "password": users_password}

		url = 'http://localhost:3000/api/authenticate'
		token = self.post(url, data)['token']
		users_info = self.get(url, token)['user']
		self.set_info(users_info, token)

	def set_info(self, user, token):
		self.id = user['_id']
		self.name = user['name']
		self.email = user['email']
		self.bio = user['bio']
		self.admin = True if user['admin'] else False
		self.token = token
