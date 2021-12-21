from django.shortcuts import render

# Create your views here.
def admin(request):
	context = {'user':0}
	return render(request, 'adminpage/admin.html', context)

def categories(request):
	context = {'user':0}
	return render(request, 'adminpage/category.html', context)

def users(request):
	context = {'user':0}
	return render(request, 'adminpage/users.html', context)

def products(request):
	context = {'user':0}
	return render(request, 'adminpage/products.html', context)

def orders(request):
	context = {'user':0}
	return render(request, 'adminpage/orders.html', context)