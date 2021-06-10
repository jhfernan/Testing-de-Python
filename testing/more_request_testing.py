import sys
import os

sys.path.append(os.getcwd())

from app_pkg.api_handler import APIHandler
from app_pkg.menu import Menu
from app_pkg.prettify import Prettify


# My Variables
api_handler = APIHandler()
menu = Menu('API App')
prettifier = Prettify()

while True:
	user_input = prettifier.main_menu(
		menu.title,
		menu.question,
		menu.error if menu.error else menu.results,
	)

	if user_input.lower() == 'q':
		prettifier.clear_screen()
		break
	elif menu.check_response(user_input):
		prettifier.clear_screen()
		print('Requesting info...')
		json_response = api_handler.get(menu.get_url(user_input))
		menu.setup_results_screen(user_input, json_response)
		prettifier.clear_screen()
		continue
	elif not user_input:
		menu.error = '*** Please put a valid input. ***'
		continue
	else:
		menu.results = 'That option is not recognized. Please try again.'

	menu.error = ''
