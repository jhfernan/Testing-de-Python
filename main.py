from app_pkg import *


home = Home()
user = User()

while True:
	user.login_user()
	response = home.print_welcome_screen(user)
	print(response)
	break
