from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from .models import Consume, MyUser, ConsumeCategory, User_ConCategory, Con_ConCategory
from django.utils import timezone
from .forms import ConsumeForm, UserForm, ConsumeCategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
import datetime
import json
from django.core import serializers


# main
# template 뿌리는 놈
def consume_list(request):
	# logged_in_user = request.user
	# consumes = Consume.objects.filter(user_id=logged_in_user.id).order_by('-con_date')
	# return render(request, 'ac_book/consume_list.html', {'consumes':consumes})
	user_categorys = User_ConCategory.objects.filter(user_id = request.user.pk)
	custom_category = []

	if user_categorys.exists() :
	   for user_category in user_categorys:
	      custom_category.append(get_object_or_404(ConsumeCategory, pk = user_category.category_id_id))

	return render(request, 'ac_book/consume_list_data.html', {'categorys':custom_category})

# data 뿌리는 놈
def consume_list_data(request):
	logged_in_user = request.user
	consumes_dic_list = Consume.objects.filter(user_id=logged_in_user.id).order_by('-con_date')
	sendArr = []
	for consume_dict in consumes_dic_list:
		con_cate = Con_ConCategory.objects.filter(consume_id=consume_dict.pk)[0]
		category_name = ConsumeCategory.objects.filter(pk = con_cate.category_id_id)[0].category_name
		sendArr.append({
			'id' : consume_dict.pk,
			'category_id' : con_cate.category_id_id,
			'category_name' : category_name,
			'store_name' : consume_dict.store_name,
			'con_price' : consume_dict.con_price,
			'con_date' : consume_dict.con_date.strftime('%Y-%m-%dT%H:%M'),
			'con_type' : consume_dict.con_type,
			'user_id' : consume_dict.user_id
		})
	return HttpResponse(json.dumps(sendArr), content_type = "application/json")


def consume_read_by_concate(request, pk):
	logged_in_user = request.user
	# Should change 2 to pk
	con_concates = Con_ConCategory.objects.filter(category_id_id=pk)
	category_name = ConsumeCategory.objects.filter(pk = pk)[0].category_name

	sendArr = []
	for con_concate in con_concates:
		consume = Consume.objects.filter(pk = con_concate.consume_id_id, user_id=logged_in_user.id).order_by('-con_date')[0]
		sendArr.append({
			'id' : consume.pk,
			'category_id' : pk,
			'category_name' : category_name,
			'store_name' : consume.store_name,
			'con_price' : consume.con_price,
			'con_date' : consume.con_date.strftime('%Y-%m-%dT%H:%M'),
			'con_type' : consume.con_type,
			'user_id' : consume.user_id
		})

	return HttpResponse(json.dumps(sendArr), content_type = "application/json")

def consume_term(request, date_from, date_to):
	logged_in_user = request.user
	# python filter  첫 날짜, 끝 날짜를 찾아주는것이 있을 것이다.
	# 받은 대로 출력
	# print('date_from : %d\tdate_to : %d\n', date_from, date_to);
	from_year = date_from[:4]
	from_month =  date_from[4:6]
	to_year = date_to[:4]
	to_month = date_to[4:6]
	consumes = Consume.objects.filter(con_date__year__lte=to_year, con_date__month__lte=to_month,  con_date__year__gte= from_year, con_date__month__gte=from_month, user_id=logged_in_user.id).order_by('-con_date')

	sendArr = []
	for consume_dict in consumes:
		con_cate = Con_ConCategory.objects.filter(consume_id=consume_dict.pk)[0]
		category_name = ConsumeCategory.objects.filter(pk = con_cate.category_id_id)[0].category_name
		sendArr.append({
			'id' : consume_dict.pk,
			'category_id' : con_cate.category_id_id,
			'category_name' : category_name,
			'store_name' : consume_dict.store_name,
			'con_price' : consume_dict.con_price,
			'con_date' : consume_dict.con_date.strftime('%Y-%m-%dT%H:%M'),
			'con_type' : consume_dict.con_type,
			'user_id' : consume_dict.user_id
		})
	return HttpResponse(json.dumps(sendArr), content_type = "application/json")

def consume_read(request, pk):
	consume = get_object_or_404(Consume, pk=pk)

	con_cate = Con_ConCategory.objects.filter(consume_id=pk)[0]
	category_name = ConsumeCategory.objects.filter(pk = con_cate.category_id_id)[0].category_name

	
	return render(request, 'ac_book/consume_read.html', {'consume':consume, 'category_name' : category_name})

@login_required
def consume_create(request):
	if request.method == "POST":
		form = ConsumeForm(request.POST)
		if form.is_valid():
			consume = form.save(commit=False)
			consume.user = request.user

			consume.save()
			Con_ConCategory.objects.create(consume_id_id=consume.pk, category_id_id=request.POST.get("id_con_cate",""))
			return redirect('consume_read', pk=consume.pk)
	else:
		consume_form = ConsumeForm()
		#read consume category from DB and send rendered page
		user_categorys = User_ConCategory.objects.filter(user_id = request.user.pk)
		custom_category = []

		if user_categorys.exists() :
		   for user_category in user_categorys:
		      custom_category.append(get_object_or_404(ConsumeCategory, pk = user_category.category_id_id))
		
	return render(request, 'ac_book/consume_create.html', {'form':consume_form, 'con_cate_form' : custom_category})

@login_required
def consume_update(request, pk):
	consume = get_object_or_404(Consume, pk = pk)
	if request.method == "POST":
		# Need to check validation
		# Need to render con_date
		store_name = request.POST.get("store_name", "")
		con_type = request.POST.get("con_type", "")
		con_price = request.POST.get("con_price", "")
		con_date = request.POST.get("con_date", "")
		category_id = request.POST.get("id_con_cate", "")		
		Consume.objects.filter(pk=pk).update(store_name=store_name, con_type = con_type, con_price=con_price)

		get_obj = Con_ConCategory.objects.filter(consume_id=pk).update(category_id_id=category_id)
	return redirect('consume_read', pk=consume.pk)

@login_required
def consume_delete(request, pk):
  consume = get_object_or_404(Consume, pk=pk)
  consume.delete()
  #return redirect('ac_book.views.consume_list')
  return redirect('consume_list')


def logout_view(request):
	logout(request)
	# return redirect('/')

def sign_up(request):
		if request.method == "POST":
			form = UserForm(request.POST)
			if form.is_valid():
				my_user = form.save(commit=False)
				email = my_user.email
				date_of_birth = my_user.date_of_birth
				password = my_user.password
				user = MyUser.objects.create_user(email, date_of_birth, password)			
				user.save()
				return redirect('/')
				#return redirect('ac_book.views.consume_detail', pk=consume.pk)
		else:
			form = UserForm()
		return render(request, 'registration/sign_up.html', {'form':form})

def user_info(request):
	pk = request.user.pk
	user = get_object_or_404(MyUser, pk = pk)
	if request.method == "POST":
		#edit user_info
		user.date_of_birth = request.POST['date_of_birth']
		user.save()
		return redirect('user_info')
	else:
		#request user_info views
		form = UserForm(instance = user)
	return render(request, 'registration/user_info.html', {'form':form})

def user_del(request):
	user = get_object_or_404(MyUser, pk = request.user.pk)
	user.delete()
	return redirect('/')

def category_consume_readAll(request):
   user_categorys = User_ConCategory.objects.filter(user_id = request.user.pk)
   custom_category = []

   if user_categorys.exists() :
      for user_category in user_categorys:
         custom_category.append(get_object_or_404(ConsumeCategory, pk = user_category.category_id_id))
   
   return render(request, 'ac_book/concategory_read_all.html', {'custom_category' : custom_category})