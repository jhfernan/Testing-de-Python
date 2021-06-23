from app_pkg import *


home = Home()
user = User()

while True:
	user.login_user()
	home.print_welcome_screen(user.name)

	break
