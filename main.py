from app_pkg import *


home = Home()
user = User()

while True:
	user.login_user()
	response = home.print_welcome_screen(user)
	res = response['res'].lower()
	if res == 'q':
		home.shutdown()
		break
	elif res == 'l' and response['options'][-1]['title'] == 'Logout':
		user.logout()
		continue
