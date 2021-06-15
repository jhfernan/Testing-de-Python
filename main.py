from app_pkg import *


menu = Menu('Api App', 'Login\n-----\nEmail: ')
prettifier = Prettify()
req = Requests()

while True:
	email = prettifier.main_menu(
		menu.title,
		menu.question,
		menu.error if menu.error else menu.results
	)
	password = prettifier.main_menu(
		menu.title,
		'password:\n>> ',
		'{}\n-----'.format(email),
		True
	)
	data = {
		"email": email,
		"password": password
	}

	auth_res = req.post('http://localhost:3000/api/authenticate', data)
	get_res = req.get('http://localhost:3000/api/authenticate')

	print(auth_res)
	print(get_res)
	break
