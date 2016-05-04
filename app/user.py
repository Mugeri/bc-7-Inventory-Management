from app import models, db

class UserCRUD(User):
	
	def __init__(self, user):

		pass

	def promote_user(self, user):
		level = user.level
		if level == 3:
			level = 2
			User.level = level
			db.session.commit()
			flash(('%r has been made admin') % user.username)
		flash(('%r is already an admin') % user.username)

	def delete_user(self, user):
		session.delete(user)
		session.commit()
		return (("%r successfully deleted!") % user.username)
