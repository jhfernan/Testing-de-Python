import os
import sys
import getpass


class Prettify:
	title = 'Jonathan\'s App'
	question = '\nWhat would you like to do?\n=> '

	def clear_screen(self):
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

	def main_menu(self, title = '', input_question = '', message = '', password = False):
		self.clear_screen()
		title_card = '*' * 80 + '\n\t\t\t'
		title_card += title if title else self.title
		title_card += '\n' + '*' * 80
		print(title_card)
		print('\n' + message if message else '')

		if not password:
			return input(input_question if input_question else self.question)
		else:
			return getpass.getpass()
