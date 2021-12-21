from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)


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
	def Price(self):
		return self.UnitPrice

class Order(models.Model):
	CreatedDate = models.DateTimeField(auto_now_add=True)
	CustomerID = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	Total = models.FloatField()
	Status = models.CharField(max_length=200, blank=True)
	FullName = models.CharField(max_length=200, blank=True)
	Mail = models.CharField(max_length=200, blank=True)
	Address = models.CharField(max_length=200, blank=True)
	Phone = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return str(self.id) + " - " + str(self.Address) + " - " + str(self.Phone) + " - " + str(self.Total) + " - " + str(self.Status)

class OrderDetail(models.Model):
	ProductID = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	OrderID = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	Quantity = models.IntegerField()
	def __str__(self):
		return str(self.OrderID.id) + " - " + str(self.OrderID.Address) + " - " + str(self.OrderID.Phone) + " - " + str(self.ProductID.ProductName) + " - " + str(self.ProductID.UnitPrice)

class Cart(models.Model):
	CustomerID = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.id

	@property
	def get_cart_items(self):
		cartdetails = self.cartdetail_set.all()
		total = sum([item.Quantity for item in cartdetails])
		return total 
	@property
	def get_cart_total(self):
		cartdetails = self.cartdetail_set.all()
		total = sum([item.ProductID.UnitPrice for item in cartdetails])
		return total 

class CartDetail(models.Model):
	ProductID = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	Cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
	Quantity = models.IntegerField(default=0, null=True, blank=True)

	def get_total(self):
		total = self.ProductID.UnitPrice * self.Quantity
		return total