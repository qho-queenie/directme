from system.core.controller import *
class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')

	def index(self):
		return self.load_view('index.html')


	def login(self):
		email = request.form['email']
		password = request.form['password']
		user = self.models['User'].get_user_by_email(email)
		if not user:
			flash('This email address has not been registered')
			return redirect('/')
		elif not self.models['User'].bcrypt.check_password_hash(user['password'], password):
			flash('Information given does not match login credentials!')
			return redirect('/')
		else:
			session['email'] = email
			session['success'] = 'logged in'
			return redirect('/success')


	def register(self):
		user_info = {
			"first_name" : request.form['first_name'],
			"last_name" : request.form['last_name'],
			"email" : request.form['email'],
			"password" : request.form['password'],
			"c_password" : request.form['c_password']
		}
		validations = self.models['User'].add_user(user_info)
		if validations['status'] == False:
			for message in validations['errors']:
				flash(message, 'error')
				return redirect('/')
		else:
			session["email"] = request.form['email']
			session['success'] = 'registered'   
			return redirect('/success')


	def success(self):
		user = self.models['User'].get_user_by_email(session["email"])
		session['name'] = user['first_name']
		return self.load_view('success.html', name=session['name'], success_message = session['success'])


	def displayUpdate(self):
		user = self.models['User'].get_user_by_email(session['email'])
		return self.load_view('update.html', user=user)


	def update(self):
		user_info = {
			"first_name" : request.form['first_name'],
			"last_name" : request.form['last_name'],
			"email" : request.form['email'],
			"password" : request.form['password'],
			"c_password" : request.form['c_password']
		}
		validations = self.models['User'].update_user(user_info)
		if validations['status'] == False:
			for message in validations['errors']:
				flash(message, 'error')
				return redirect('/update')
		else:
			session['success'] = 'updated account'
			return redirect('/success')


	def delete(self):
		user = self.models['User'].get_user_by_email(session['email'])
		return self.load_view('delete.html', user=user)


	def destroy(self):
		self.models['User'].delete_user(session['email'])
		session.clear()
		flash('Account successfully deleted')
		return redirect('/')


	def logout(self):
		session.clear()
		flash('You are now logged out')
		return redirect('/')




