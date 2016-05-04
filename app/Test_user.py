from unittests import Testcase

class UserClassTest(Testcase):

	def test_user_instance:
		user = User('Jane')
		self.assertInstance(Jane, User, msg="The object should be an instance of User")

	def test_db_update:
		user = User('Alex')