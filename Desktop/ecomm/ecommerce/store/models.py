from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
	FullName = models.CharField(max_length=200)
	Mail = models.CharField(max_length=200)
	Address = models.CharField(max_length=200)
	Phone = models.CharField(max_length=200)
	Username = models.CharField(max_length=200)
	Password = models.CharField(max_length=200)

	def __str__(self):
		return self.FullName


class Category(models.Model):
	Name = models.CharField(max_length=200)

	def __str__(self):
		return self.Name

class Product(models.Model):
	ProductName = models.CharField(max_length=200)
	Cate = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	Description = models.CharField(max_length=200)
	Quantity = models.IntegerField()
	UnitPrice = models.FloatField()
	ImgPath = models.ImageField(max_length=500)

	def __str__(self):
		return self.ProductName

	@property
	def imageURL(self):
		try:
			url = self.ImgPath.url
		except:
			url = ''
		return url

class Order(models.Model):
	CreatedDate = models.DateTimeField(auto_now_add=True)
	Customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	Total = models.FloatField()
	Status = models.CharField(max_length=200)

	def __str__(self):
		return str(self.id)

class OrderDetail(models.Model):
	Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	Quantity = models.IntegerField()
	UnitPrice = models.FloatField()