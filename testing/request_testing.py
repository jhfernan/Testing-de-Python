from modules.api_handler import APIHandler
from modules.prettify import Prettify


# My Variables
api_handler = APIHandler()
prettifier = Prettify()

title = 'Jonathan\'s Weather App'
error = ''
question = 'What city do you want to know the weather for? (Enter "Q" to quit)\n=> '
results = ''

while True:
	user_input = prettifier.main_menu(title, question, error if error else results)

	if user_input.lower() == 'q':
		prettifier.clear_screen()
		break
	elif not user_input:
		error = '*** Please put a valid input. ***'
		continue
	else:
		url = 'http://api.openweathermap.org/data/2.5/weather?q='
		url += user_input
		url += '&appid=8816628b6017926fbf7cc60538485608'
		json_response = api_handler.get(url)
		temp = round(json_response['main']['temp'] - 273.15, 1)
		results = 'It is currently {} degrees Celsius in {}'.format(temp, user_input.capitalize())

	error = ''
