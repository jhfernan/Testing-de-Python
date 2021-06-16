from app_pkg import *


menu = Menu('Api App', 'Login\n-----\nEmail: ')
prettifier = Prettify()
req = Requests()
user = User()

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

	token = req.post('http://localhost:3000/api/authenticate', data)['token']
	user_info = req.get('http://localhost:3000/api/authenticate', token)['user']
	user.set_info(user_info, token)

	# print(user.admin)
	attrs = vars(user)
	print('\n'.join("%s: %s" % item for item in attrs.items()))
	# print(get_res)
	break
