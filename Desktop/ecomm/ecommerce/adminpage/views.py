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
	if(request.POST.get('action') == 'edit'):
		cateid = request.POST.get('id')
		name = request.POST.get('name')
		cate = Category.objects.get(id=cateid)
		if(len(name)>0):
			cate.Name = name
		cate.save()
		context = {'cate':cate,'action':'edit'}
		return render(request, 'adminpage/category-view.html', context)
	if(request.POST.get('action') == 'add'):
		name = request.POST.get('name')
		cate = Category(Name=name)
		cate.save()
		categories = Category.objects.all()
		context = {'categories':categories}
		return render(request, 'adminpage/categories.html', context)
	if(request.GET.get('action') == 'edit'):
		cateid = request.GET.get('id')
		cate = Category.objects.get(id=cateid)
		context = {'cate':cate,'action':'edit'}
		return render(request, 'adminpage/category-view.html', context)
	if(request.GET.get('action') == 'add'):
		context = {'cate':0,'action':'add'}
		return render(request, 'adminpage/category-view.html', context)
	if(request.GET.get('action')=="delete"):
		cateid = request.GET.get('id')
		cate = Category.objects.get(id=cateid)
		cate.delete()
	categories = Category.objects.all()
	context = {'categories':categories}
	return render(request, 'adminpage/categories.html', context)

@staff_member_required
def users(request):
	if(request.POST.get('action') == 'edit'):
		userid = request.POST.get('id')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = User.objects.get(id=userid)
		if(len(password)>0):
			user.set_password(password)
			user.save()
		if(len(username)>0):
			user.email = email
		if(len(email)>0):
			user.username = username
		user.save()
		context = {'user':user,'action':'edit'}
		return render(request, 'adminpage/user-view.html', context)
	if(request.POST.get('action') == 'add'):
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = User.objects.create_user(username,email, password)
		user.save()
		users = User.objects.all()
		context = {'users':users}
		return render(request, 'adminpage/users.html', context)
	if(request.GET.get('action')=="edit"):
		userid = request.GET.get('id')
		user = User.objects.get(id=userid)
		context = {'user':user,'action':'edit'}
		return render(request, 'adminpage/user-view.html', context)
	if(request.GET.get('action')=="add"):
		context = {'user':0,'action':'add'}
		return render(request, 'adminpage/user-view.html', context)
	if(request.GET.get('action')=="delete"):
		userid = request.GET.get('id')
		user = User.objects.get(id=userid)
		user.delete()
	users = User.objects.all()
	context = {'users':users}
	return render(request, 'adminpage/users.html', context)

@staff_member_required
def products(request):
	if(request.POST.get('action') == 'edit'):
		proid = request.POST.get('id')
		name = request.POST.get('name')
		cateid = request.POST.get('cateid')
		description = request.POST.get('description')
		quantity = request.POST.get('quantity')
		price = request.POST.get('price')
		cateid = Category.objects.get(id=cateid)
		pro = Product.objects.get(id=proid)

		pro.ProductName=name
		pro.Cate=cateid
		pro.Description=description
		pro.Quantity=quantity
		pro.UnitPrice=price
		try:
			pro.ImgPath=request.FILES['img']
		except:
			...
		pro.save()
		categories = Category.objects.all()
		context = {'pro':pro,'categories':categories,'action':'edit'}
		return render(request, 'adminpage/product-view.html', context)
	if(request.POST.get('action') == 'add'):
		name = request.POST.get('name')
		cateid = request.POST.get('cateid')
		description = request.POST.get('description')
		quantity = request.POST.get('quantity')
		price = request.POST.get('price')
		img = request.FILES['img']
		cateid = Category.objects.get(id=cateid)
		pro = Product(ProductName=name,Cate=cateid,Description=description,Quantity=quantity,UnitPrice=price,ImgPath=img)
		pro.save()
		products = Product.objects.all()
		context = {'products':products}
		return render(request, 'adminpage/products.html', context)
	if(request.GET.get('action') == 'edit'):
		proid = request.GET.get('id')
		pro = Product.objects.get(id=proid)
		categories = Category.objects.all()
		context = {'pro':pro,'categories':categories,'action':'edit'}
		return render(request, 'adminpage/product-view.html', context)
	if(request.GET.get('action') == 'add'):
		categories = Category.objects.all()
		context = {'pro':0,'categories':categories,'action':'add'}
		return render(request, 'adminpage/product-view.html', context)
	if(request.GET.get('action')=="delete"):
		proid = request.GET.get('id')
		pro = Product.objects.get(id=proid)
		pro.delete()
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'adminpage/products.html', context)

@staff_member_required
def orders(request):
	if(request.POST.get('action') == 'edit'):
		orderid = request.POST.get('id')
		name = request.POST.get('name')
		mail = request.POST.get('mail')
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		total = request.POST.get('total')
		status = request.POST.get('status')
		order = Order.objects.get(id=orderid)
		order.FullName=name
		order.Mail=mail
		order.Address=address
		order.Phone=phone
		order.Total=total
		order.Status=status

		order.save()
		context = {'order':order,'action':'edit'}
		return render(request, 'adminpage/order-view.html', context)
	if(request.GET.get('action') == 'edit'):
		orderid = request.GET.get('id')
		order = Order.objects.get(id=orderid)
		orderdetails = OrderDetail.objects.filter(OrderID=order)
		context = {'order':order,'orderdetails':orderdetails,'action':'edit'}
		return render(request, 'adminpage/order-view.html', context)
	if(request.GET.get('action')=="delete"):
		orderid = request.GET.get('id')
		order = Order.objects.get(id=orderid)
		order.delete()
	orders = Order.objects.all()
	context = {'orders':orders}
	return render(request, 'adminpage/orders.html', context)