from system.core.model import Model
import re
class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def get_user_by_email(self, email):
		query = "SELECT first_name, last_name, email, password FROM users WHERE email = :email"
		data = { 
			'email': email
		}
		user = self.db.query_db(query, data)
		if user:
			return user[0]
		else:
			return None

	def validate(self, user):
		email_regex = re.compile(r"^[^@]+@[^@]+\.[^@]+$")
		errors = []
		if not user['first_name']:
			errors.append('First name cannot be blank')
		elif not user['last_name']:
			errors.append('Last name cannot be blank')
		elif len(user['first_name']) < 2 or len(user['last_name']) < 2:
			errors.append('Name must be at least 2 characters long')
		if not user['email']:
			errors.append('Email cannot be blank')
		elif not email_regex.match(user['email']):
			errors.append('Email format is not valid!')
		if not user['password']:
			errors.append('Password cannot be blank')
		elif len(user['password']) < 8:
			errors.append('Password must be at least 8 characters long')
		elif user['password'] != user['c_password']:
			errors.append('Password and confirmation do not match')		
		return errors
		

	def add_user(self, user):
		errors = self.validate(user)
		registered = self.get_user_by_email(user['email'])
		if registered:
			errors.append('This email address is already registered!')
		if errors:
			return {"status": False, "errors": errors}
		else:
			password_hash = self.bcrypt.generate_password_hash(user['password'])
			query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW())"
			data = { 
				'first_name': user['first_name'],
				'last_name': user['last_name'], 
				'email': user['email'],
				'password': password_hash 
			}
			self.db.query_db(query, data)
			return { "status": True }

	def update_user(self, user):
		errors = self.validate(user)
		if errors:
			return {"status": False, "errors": errors}
		else:
			password_hash = self.bcrypt.generate_password_hash(user['password'])
			query = "UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email, password=:password WHERE email = :email"
			data = { 
				'first_name': user['first_name'], 
				'last_name': user['last_name'], 
				'email': user['email'],
				'password': password_hash
			}
			self.db.query_db(query, data)
			return { "status": True }

	def delete_user(self, email):
		query = "DELETE FROM users WHERE email = :email"
		data = { "email": email }
		return self.db.query_db(query, data)



