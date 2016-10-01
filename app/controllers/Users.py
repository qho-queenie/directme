from system.core.controller import *
import requests
import pprint
import math
import random

def warnjilly(method):
  def wrapper(*args, **kwargs):
	try:
	  return method(*args, **kwargs)
	except Exception, e:
	  print '!!!! Oh no jilly, something went wrong !!!!'
	  print e
	  raise e
  return wrapper



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
			session['cities_id'] = user['cities_id']
			return redirect('/directme')


	def register(self):
		user_info = {
			"name" : request.form['name'],
			"email" : request.form['email'],
			"city" : request.form['city'],
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
			session['city'] = (request.form['city']).replace(" ", "+")  
			return redirect('/directme')

	# @warnjilly
	def directme(self):
		user = self.models['User'].get_user_by_email(session["email"])
		session['cities_id'] = user['cities_id']
		session['name'] = user['name'].title()
		if session['cities_id'] == 1:
			city_id = 5391959
		elif session['cities_id'] == 2:
			city_id = 4391354
		elif session['cities_id'] == 3:
			city_id = 512858
		elif session['cities_id'] == 4:
			city_id = 4887398
		response = requests.get("http://api.openweathermap.org/data/2.5/weather?id=%d&APPID=86487cba59a4c9fbbbcc3f25e61690f3" % city_id)
		search = (response.json())
		# pprint.pprint(search)
		if "weather" in search and "main" in search:
			weather = search['weather'][0]['description'].title()
			temp = int(math.ceil((search['main']['temp']) * (9/5.0) - 459.67))
		else:
			weather = "Clear sky"
			temp = 66
		# print 'moo', self.load_view('directme.html', weather=weather, temp=temp)
		return self.load_view('directme.html', weather=weather, temp=temp, name=session['name'])


	@warnjilly
	def random_choice(self):

		response = requests.post("https://api.yelp.com/oauth2/token", data = {
			'grant_type': "client_credentials",
			"client_id": "qGN0-clZVHgIJQW4eEZVgA",
			"client_secret": "gDeyt0187jMBS9FWhBKDWkXycsyz174jUeIhCFEUiuJQy4Xr2UfMvX46KMASoPZz"
		})

		access_token = response.json()['access_token']

		session['category'] = request.form['category']
		session['price'] = request.form['price']
		session['distance'] = int(request.form['distance'])
		if session['cities_id'] == 1:
			session['city'] = 'san+francisco'
		elif session['cities_id'] == 2:
			session['city'] = 'houston'
		elif session['cities_id'] == 3:
			session['city'] = 'new+york'
		elif session['cities_id'] == 4:
			session['city'] = 'chicago'

		user_search = requests.get("https://api.yelp.com/v3/businesses/search?term=%s&location=%s&price=%s&radius=%d&open_now=true&limit=15" % (session['category'], session['city'], session['price'], session['distance']), headers = {
		"Authorization": "Bearer %s" % access_token
		})

		session['choices'] = (user_search.json())
		choices = session['choices']

		choice_list = choices['businesses'] 

		destination = random.choice(choice_list)

		session['business_name'] = str(destination['name'])
		session['rating'] = str(destination['rating'])
		session['price'] = str(destination['price'])
		if destination['url']:
			session['website'] = str(destination['url'])
		elif destination['website']:
			session['website'] = str(destination['website'])
		session['activity_type'] = str(destination['categories'][0]['title'])
		street_name = destination['location']['address1']
		street_name = str(street_name.replace(" ", "+"))
		city = destination['location']['city']
		city = str(city.replace(" ", "+"))
		zip_code = str(destination['location']['zip_code'])
		session['address'] = destination['location']['address1']
		session['destination'] = street_name + "," + city + "+" + zip_code

		return redirect('/destination')



	def random_choice2(self):
		# response = requests.post("https://api.yelp.com/oauth2/token", data = {
		# 	'grant_type': "client_credentials",
		# 	"client_id": "qGN0-clZVHgIJQW4eEZVgA",
		# 	"client_secret": "gDeyt0187jMBS9FWhBKDWkXycsyz174jUeIhCFEUiuJQy4Xr2UfMvX46KMASoPZz"
		# })

		# access_token = response.json()['access_token']

		# if session['cities_id'] == 1:
		# 	session['city'] = 'san+francisco'
		# elif session['cities_id'] == 2:
		# 	session['city'] = 'houston'
		# elif session['cities_id'] == 3:
		# 	session['city'] = 'new+york'
		# elif session['cities_id'] == 4:
		# 	session['city'] = 'chicago'

		# user_search = requests.get("https://api.yelp.com/v3/businesses/search?term=%s&location=%s&price=%s&radius=%d&open_now=true" % (session['category'], session['city'], session['price'], session['distance']), headers = {
		# "Authorization": "Bearer %s" % access_token
		# })

		# choices = (user_search.json())

		choices = session['choices']

		choice_list = choices['businesses'] 

		destination = random.choice(choice_list)

		session['business_name'] = str(destination['name'])
		session['rating'] = str(destination['rating'])
		session['price'] = str(destination['price'])
		if destination['url']:
			session['website'] = str(destination['url'])
		elif destination['website']:
			session['website'] = str(destination['website'])
		session['activity_type'] = str(destination['categories'][0]['title'])
		street_name = destination['location']['address1']
		street_name = str(street_name.replace(" ", "+"))
		city = destination['location']['city']
		city = str(city.replace(" ", "+"))
		zip_code = str(destination['location']['zip_code'])
		session['address'] = destination['location']['address1']
		session['destination'] = street_name + "," + city + "+" + zip_code

		return redirect('/destination')


	def destination(self):
		user = self.models['User'].get_user_by_email(session["email"])
		session['name'] = user['name'].title()
		if session['cities_id'] == 1:
			city_id = 5391959
		elif session['cities_id'] == 2:
			city_id = 4391354
		elif session['cities_id'] == 3:
			city_id = 512858
		elif session['cities_id'] == 4:
			city_id = 4887398
		response = requests.get("http://api.openweathermap.org/data/2.5/weather?id=%d&APPID=86487cba59a4c9fbbbcc3f25e61690f3" % city_id)
		search = (response.json())
		# pprint.pprint(search)
		if "weather" in search and "main" in search:
			weather = search['weather'][0]['description'].title()
			temp = int(math.ceil((search['main']['temp']) * (9/5.0) - 459.67))
		else:
			weather = "Clear sky"
			temp = 66
		SID = "ACa5bb3a96898a5cbf58db503767892b2d"
		Key = "9cab74a9763d6d767886bb2d7d8a008c"
		return self.load_view('weather.html', destination=session['destination'], SID=SID, Key=Key, myName=session['name'], yelpName=session['business_name'], address=session['address'], weather=weather, temp=temp, rating=session['rating'], price=session['price'], activity_type=session['activity_type'], website=session['website'])




	# def displayUpdate(self):
	# 	user = self.models['User'].get_user_by_email(session['email'])
	# 	return self.load_view('update.html', user=user)


	# def update(self):
	# 	user_info = {
	# 		"name" : request.form['name'],
	# 		"email" : request.form['email'],
	# 		"city" : request.form['city'],
	# 		"password" : request.form['password'],
	# 		"c_password" : request.form['c_password']
	# 	}
	# 	validations = self.models['User'].update_user(user_info)
	# 	if validations['status'] == False:
	# 		for message in validations['errors']:
	# 			flash(message, 'error')
	# 			return redirect('/update')
	# 	else:
	# 		session['success'] = 'updated account'
	# 		return redirect('/success')


	# def delete(self):
	# 	user = self.models['User'].get_user_by_email(session['email'])
	# 	return self.load_view('delete.html', user=user)


	# def destroy(self):
	# 	self.models['User'].delete_user(session['email'])
	# 	session.clear()
	# 	flash('Account successfully deleted')
	# 	return redirect('/')


	def logout(self):
		session.clear()
		flash('You are now logged out')
		return redirect('/')




