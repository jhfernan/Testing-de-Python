from .menu import Menu


class Home(Menu):
	title = ''
	options = [
		'Manage Users',
		'Manage Items',
		'Manage Vendors',
		'Sales Tracking',
		'Daily Report'
	]

	def print_welcome_screen(self, name):
		self.default_menu('Welcome back {}'.format(name.title()))
		response = self.print_multi_column_screen(self.options)
