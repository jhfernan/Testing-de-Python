import os
import math
import sys


class Prettify:
	title = ''
	width = 100
	height = 40

	def __init__(self):
		title = '*' * self.width + '\n'
		title += self.center_content('Admin Inventory Management App\n')
		title += '*' * self.width + '\n'
		self.title = title

	def center_content(self, my_string):
		return int((self.width - len(my_string)) / 2) * ' ' + my_string

	def clear_screen(self):
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

	def print_multi_column_screen(self, options, user):
		column_width = int(self.width / 2)
		column_indent = int(column_width / 3) * ' '
		options_screen = ''
		count = 0
		presented_options = []
		for option in options:
			# if hasattr(option, 'auth'):
			if 'auth' in option:
				if not getattr(user, option['auth']):
					continue

			count += 1
			presented_options.append(option)
			option_title = column_indent + str(count) + ') ' + option['title']
			if len(option_title) > column_width:
				diff = len(option_title - (column_indent * 2) - 3)
				options_screen += option_title[0:-diff] + '...'
			else:
				diff = column_width - len(option_title)
				options_screen += option_title + diff * ' '

		available_lines = self.height - (7 + math.ceil(count / 2))
		question = options_screen + '\n' * (available_lines - 3)
		question += 7 * ' '
		question += 'Please choose an option or press Q to quit: '
		response = input(question)
		return { 'res': response, 'options': presented_options }

	def resize_screen(self):
		if os.name == 'nt':
			os.system('mode {}, {}'.format(self.width, self.height))
		else:
			os.system("printf '\033[8;{};{}t'".format(self.height, self.width))
