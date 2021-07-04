from django.test import TestCase , Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User
#from raisemodifyorder.tests import *
from raisemodifyorder.views import *
from raisemodifyorder.models import *

# Create your tests here.


class UrlsTesting(TestCase):

	def test_accesses_correct_pages(self):
		
		self.signin_url=reverse('signin')
		self.raiseorder_url=reverse('raiseorder')
		self.dashboard_url=reverse('dashboard_foodseeker')
		self.modifyorder_url =reverse('modifyorder')
		self.header_url=reverse('header')
		
		self.assertEquals(resolve(self.raiseorder_url).func, raiseorder)
		self.assertEquals(resolve(self.modifyorder_url).func, modifyorder)
		self.assertEquals(resolve(self.dashboard_url).func, dashboard_foodseeker)
		self.assertEquals(resolve(self.signin_url).func, signin)
		self.assertEquals(resolve(self.header_url).func, header)


	


class ModelsTesting(TestCase):

	def test_model_food_seeker(self):

		fs_test=FoodSeeker(name='TestUser', mobile='1234554321', email='testuser@gmail.com')
		fs_test.save()

		fs_obtained_from_db=FoodSeeker.objects.filter(name='TestUser')
		
		self.assertEquals(fs_obtained_from_db[0].fs_id,1)
		self.assertEquals(fs_obtained_from_db[0].name,'TestUser')
		self.assertEquals(fs_obtained_from_db[0].mobile,'1234554321')
		self.assertEquals(fs_obtained_from_db[0].email,'testuser@gmail.com')


	def test_model_addresses(self):

		user_test=Addresses(person_id=1, person_role='food seeker', address='123 K.L Road, Srirampore-722309')
		user_test.save()
		user_test=Addresses(person_id=1, person_role='food provider', address='78 R.D Road, Srirampore-700309')
		user_test.save()
		user_test=Addresses(person_id=2, person_role='food seeker', address='123 Y.K Road, Howrah-700111')
		user_test.save()

		user_obtained_from_db=Addresses.objects.filter(person_role='food seeker')
		
		self.assertEquals(user_obtained_from_db[0].person_id,1)
		self.assertEquals(user_obtained_from_db[0].person_role,'food seeker')
		self.assertEquals(user_obtained_from_db[0].address,'123 K.L Road, Srirampore-722309')
		 
		self.assertEquals(user_obtained_from_db[1].person_id,2)
		self.assertEquals(user_obtained_from_db[1].person_role,'food seeker')
		self.assertEquals(user_obtained_from_db[1].address,'123 Y.K Road, Howrah-700111')
		
		user_obtained_from_db=Addresses.objects.filter(person_role='food provider',person_id=1)
		
		self.assertEquals(user_obtained_from_db[0].person_id,1)
		self.assertEquals(user_obtained_from_db[0].person_role,'food provider')
		self.assertEquals(user_obtained_from_db[0].address,'78 R.D Road, Srirampore-700309')
		
	def test_model_order(self):

		order=Order(veg_healthy=2,nonveg_ill=3,delivery_address='123 K.L Road, Srirampore-722309',status='active',food_seeker_id=1)
		order.save()

		order_obtained_from_db=Order.objects.filter(order_id=1)
		
		self.assertEquals(order_obtained_from_db[0].order_id,1)
		self.assertEquals(order_obtained_from_db[0].veg_healthy,2)
		self.assertEquals(order_obtained_from_db[0].veg_ill,None)
		self.assertEquals(order_obtained_from_db[0].nonveg_healthy,None)
		self.assertEquals(order_obtained_from_db[0].nonveg_ill,3)
		self.assertEquals(order_obtained_from_db[0].delivery_address,'123 K.L Road, Srirampore-722309')
		self.assertEquals(order_obtained_from_db[0].status,'active')
		self.assertEquals(order_obtained_from_db[0].food_seeker_id,1)
		self.assertEquals(order_obtained_from_db[0].food_provider_id,None)


class ViewsTesting(TestCase):

	def setUp(self):

		self.user=User.objects.create_user('testuser','testpassword')

	def test_view_signin(self):
		
		client =Client()
		response=client.get(reverse('signin'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'raisemodifyorder/signin.html')

	def test_view_dashboard_foodseeker(self):
		client =Client()
		request=RequestFactory().get('')
		request.session={}
		print(request.session)
		response=client.post(reverse('dashboard_foodseeker'),{'username':'testuser','password':'testpassword','mobile':'7878787878'})
	#	request.session['mobile']='7878787878'
	#	response=client.get(reverse('dashboard_foodseeker'))
	#	self.assertEquals(response.status_code,200)
	#	self.assertTemplateUsed(response,'raisemodifyorder/dashboard_foodseeker.html')


	#		fs_test=FoodSeeker({'fs_id':1,'name':'TestUser', 'mobile':'1234554321', 'email': 'testuser@gmail.com'})
	#	fs_test.save()
		
	#	response=client.post(reverse('dashboard_foodseeker'),fs_test,format='text/html')
		#response=client.get(reverse('dashboard_foodseeker'))
		