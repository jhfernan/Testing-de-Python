from .prettify import Prettify


class Menu(Prettify):
	# title = ''

	def default_menu(self, title):
		self.print_title_screen()
		self.title_card(title)

	def print_title_screen(self):
		self.resize_screen()
		self.clear_screen()
		print(self.title)

	def title_card(self, title):
		content = self.center_content(title)
		content += '\n' + self.center_content('_' * len(title))
		print(content)
