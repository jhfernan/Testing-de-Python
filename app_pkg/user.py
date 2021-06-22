import os
import sys
import getpass
from urllib.request import urlopen, Request
from urllib import parse
import json


class User:
	id = None
	name = None
	email = None
	bio = None
	admin = False
	token = None

	def clear_screen(self):
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

	def main_menu(self):
		# Get users email
		self.clear_screen()
		base_title_card = '*' * 80 + '\n\t\t\t\t'
		base_title_card += 'User Application'
		base_title_card += '\n' + '*' * 80 + '\n\n\n'
		title_card = base_title_card + '\t\t\t_______Login__________'
		print(title_card)
		users_email = input('\t\t\tEmail: ')

		# Get users password
		self.clear_screen()
		title_card += '\n\t\t\tEmail: '
		title_card += users_email
		title_card += '\n\t\t\tPassword: '
		users_password = getpass.getpass(title_card)

		# Prepare data for post request to API to authenticate
		data = {
			"email": users_email,
			"password": users_password
		}

		url = 'http://localhost:3000/api/authenticate'
		params = parse.urlencode(data)
		params = params.encode('utf-8')
		http_request = Request(url, data=params, headers={'Content-Type': 'application/x-www-form-urlencoded'})

		with urlopen(http_request) as response:
			try:
				response_token = json.load(response)
			except Exception as e:
				response_token = ''

		token = response_token['token']
		http_request = Request(url, headers={
			'Accept': 'application/json',
			'Authorization': 'Bearer {}'.format(token)
		})
		with urlopen(http_request) as response:
			try:
				response_user = json.load(response)
			except Exception as e:
				response_user = ''
		self.set_info(response_user['user'], token)

		self.clear_screen()
		welcome_screen = base_title_card + '\t\t\tWelcome Back'
		welcome_screen += '\n\t\t\tYou are currently logged in as '
		welcome_screen += self.name.title()
		print(welcome_screen)

	def set_info(self, user, token):
		self.id = user['_id']
		self.name = user['name']
		self.email = user['email']
		self.bio = user['bio']
		self.admin = True if user['admin'] else False
		self.token = token
