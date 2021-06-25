from .menu import Menu


class Home(Menu):
	title = ''
	options = [
		{ 'title': 'Manage Users', 'auth': 'admin' },
		{ 'title': 'Manage Items' },
		{ 'title': 'Manage Vendors' },
		{ 'title': 'Sales Tracking', 'auth': 'admin' },
		{ 'title': 'Daily Report', 'auth': 'admin' },
		{ 'title': 'Logout', 'choice': 'L' }
	]

	def print_welcome_screen(self, user):
		self.default_menu('Welcome back {}'.format(user.name.title()))
		return self.print_multi_column_screen(self.options, user)
