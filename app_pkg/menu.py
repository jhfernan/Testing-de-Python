from .prettify import Prettify


class Menu(Prettify):
	default_spacing = 7

	def default_menu(self, title, title_spacing = False):
		self.print_title_screen()
		if title_spacing:
			print('\n' * self.default_spacing)
		self.title_card(title)

	def print_title_screen(self):
		self.resize_screen()
		self.clear_screen()
		print(self.title)

	def title_card(self, title):
		content = self.center_content(title)
		content += '\n' + self.center_content('_' * len(title)) + '\n'
		print(content)
