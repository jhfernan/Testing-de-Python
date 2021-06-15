

class User:
	id = None
	name = None
	email = None
	bio = None
	admin = False
	token = None

	def set_info(self, user, token):
		self.id = user['id']
		self.name = user['name']
		self.email = user['email']
		self.bio = user['bio']
		self.admin = True if user['admin'] else False
		self.token = token
