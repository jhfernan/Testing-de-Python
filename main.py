from app_pkg import *


menu = Menu('Api App', 'Login\n-----\nEmail:\n>> ')
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
		'{}\n-----'.format(email)
	)
	data = {
		"email": email,
		"password": password
	}

	auth_res = req.post('http://localhost:3000/api/authenticate', data)

	print(auth_res)
	break
