from django.db import models

# Create your models here.

class FoodSeeker(models.Model):
	fs_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	email=models.CharField(max_length=100)

class Addresses(models.Model):
	person_id=models.IntegerField()
	person_role=models.CharField(max_length=50) #food seeker or food provider
	address=models.CharField(max_length=200)


class Order(models.Model):
	order_id=models.AutoField(primary_key=True)
	veg_healthy=models.IntegerField(null=True)
	veg_ill=models.IntegerField(null=True)
	nonveg_healthy=models.IntegerField(null=True)
	nonveg_ill=models.IntegerField(null=True)
	allergies=models.CharField(max_length=200,null=True)
	delivery_address=models.CharField(max_length=200)
	status=models.CharField(max_length=50)  #active, dispatched or delivered
	food_seeker_id=models.IntegerField()
	food_provider_id=models.IntegerField(null=True)

