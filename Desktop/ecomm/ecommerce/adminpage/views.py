from django.shortcuts import render
from store.models import *
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@staff_member_required
def admin(request):
	context = {'user':0}
	return render(request, 'adminpage/admin.html', context)

@staff_member_required
def categories(request):
	categories = Category.objects.all()
	context = {'categories':categories}
	return render(request, 'adminpage/categories.html', context)

@staff_member_required
def users(request):
	if(request.GET.get('id')):
		userid = request.GET.get('id')
		user = User.objects.get(id=userid)
		context = {'user':user}
		return render(request, 'adminpage/user-view.html', context)
	users = User.objects.all()
	context = {'users':users}
	return render(request, 'adminpage/users.html', context)

@staff_member_required
def products(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'adminpage/products.html', context)

@staff_member_required
def orders(request):
	orders = Order.objects.all()
	context = {'orders':orders}
	return render(request, 'adminpage/orders.html', context)