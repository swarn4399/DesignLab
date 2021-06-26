from django.shortcuts import render
from .models import FoodSeeker
from .models import Addresses
from .models import Order

# Create your views here.
def dashboard_foodseeker(request):
	mobile_number = request.POST.get("mobile_number",False)
	order_id=request.POST.get("order_id", False)
	if(mobile_number == False and order_id==False):
		print("Coming from raiseorder page")
		mobile_number=request.session['mobile']
		fs_id=request.session['fs_id']
		veg_healthy=request.POST.get("veg_healthy",False)
		if veg_healthy =="":
			veg_healthy=0
		veg_ill = request.POST.get("veg_ill",False)
		if veg_ill =="":
			veg_ill=0
		nonveg_healthy=request.POST.get("nonveg_healthy",False)
		if nonveg_healthy =="":
			nonveg_healthy=0
		nonveg_ill=request.POST.get("nonveg_ill",False)
		if nonveg_ill =="":
			nonveg_ill=0
		allergies=request.POST.get("allergy",False)
		if allergies =="":
			allergies ='None'
		delivery_address=request.POST.get("delivery_address",False)
		a=Order(veg_healthy=veg_healthy,veg_ill=veg_ill,nonveg_healthy=nonveg_healthy,nonveg_ill=nonveg_ill,allergies=allergies,delivery_address=delivery_address,status='active',food_seeker_id=fs_id)
		a.save()
		type_of_alert="raise_order"
	elif(order_id==False):
		print("Coming from signin page")
		request.session['mobile']=mobile_number
		type_of_alert="sign_in"
	else:
		print("Coming from modifyorder page")
		modify_or_cancel=request.POST.get("modify_or_cancel",False)
		mobile_number=request.session['mobile']
		a=Order.objects.filter(order_id=order_id)
		if(modify_or_cancel == "modify"):
			veg_healthy=request.POST.get("veg_healthy",False)
			if veg_healthy =="":
				veg_healthy=0
			veg_ill = request.POST.get("veg_ill",False)
			if veg_ill =="":
				veg_ill=0
			nonveg_healthy=request.POST.get("nonveg_healthy",False)
			if nonveg_healthy =="":
				nonveg_healthy=0
			nonveg_ill=request.POST.get("nonveg_ill",False)
			if nonveg_ill =="":
				nonveg_ill=0
			allergies=request.POST.get("allergy",False)
			if allergies =="":
				allergies ='None'
			delivery_address=request.POST.get("delivery_address",False)
			a.update(veg_healthy=veg_healthy,veg_ill=veg_ill,nonveg_healthy=nonveg_healthy,nonveg_ill=nonveg_ill,allergies=allergies,delivery_address=delivery_address)
			type_of_alert="modify_order"
		else:
			a.delete()
			type_of_alert="cancel_order"

	fs= FoodSeeker.objects.filter(mobile=mobile_number)
	request.session['fs_id']=fs[0].fs_id
	fs_id=request.session['fs_id']
	orders=Order.objects.filter(status='active',food_seeker_id=fs_id)
	return render(request, 'raisemodifyorder/dashboard_foodseeker.html',{'FoodSeekers': fs, 'Orders': orders, 'type_of_alert':type_of_alert})

def raiseorder(request):
	fs_id=request.session['fs_id']
	fs= FoodSeeker.objects.filter(fs_id=fs_id)
	addr=Addresses.objects.filter(person_role='food seeker',person_id=fs_id)
	return render(request, 'raisemodifyorder/raiseorder.html',{'FoodSeekers': fs, 'Addresses': addr})

def signin(request):
	return render(request, 'raisemodifyorder/signin.html')

def header(request):
	fs_id=request.session['fs_id']
	fs= FoodSeeker.objects.filter(fs_id=fs_id)
	return render(request, 'raisemodifyorder/header.html',{'FoodSeekers': fs})

def modifyorder(request):
	fs_id=request.session['fs_id']
	fs= FoodSeeker.objects.filter(fs_id=fs_id)
	modify_order_id=request.POST.get("modify_order_id", False)
	order=Order.objects.filter(order_id=modify_order_id)
	addr=Addresses.objects.filter(person_role='food seeker',person_id=fs_id)
	return render(request, 'raisemodifyorder/modifyorder.html',{'FoodSeekers': fs, 'Order': order, 'Addresses': addr})
