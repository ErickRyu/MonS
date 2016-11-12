from django.shortcuts import render, get_object_or_404, redirect
from .models import Consume, MyUser
from django.utils import timezone
from .forms import ConsumeForm, UserForm
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
	return render(request, 'ac_book/consume_list_data.html')

# data 뿌리는 놈
def consume_list_data(request):
	logged_in_user = request.user
	consumes = Consume.objects.filter(user_id=logged_in_user.id).order_by('-con_date')

	con_obj = serializers.serialize('json', consumes)
	return HttpResponse(json.dumps(con_obj), content_type = "application/json")


def consume_term(request, date_from, date_to):
	logged_in_user = request.user
	# python filter  첫 날짜, 끝 날짜를 찾아주는것이 있을 것이다.
	# 받은 대로 출력
	from_year = date_from[:4]
	from_month =  date_from[4:6]
	to_year = date_to[:4]
	to_month = date_to[4:6]
	consumes = Consume.objects.filter(con_date__year__lte=to_year, con_date__month__lte=to_month,  con_date__year__gte= from_year, con_date__month__gte=from_month, user_id=logged_in_user.id).order_by('-con_date')
	
	con_obj = serializers.serialize('json', consumes)
	return HttpResponse(json.dumps(con_obj), content_type = "application/json")


def consume_read(request, pk):
	consume = get_object_or_404(Consume, pk=pk)
	return render(request, 'ac_book/consume_read.html', {'consume':consume})

@login_required
def consume_create(request):
	if request.method == "POST":
		form = ConsumeForm(request.POST)
		if form.is_valid():
			consume = form.save(commit=False)
			consume.user = request.user
			consume.save()
			return redirect('consume_read', pk=consume.pk)
	else:
		form = ConsumeForm()
	return render(request, 'ac_book/consume_update.html', {'form':form})

@login_required
def consume_update(request, pk):
	consume = get_object_or_404(Consume, pk = pk)
	if request.method == "POST":
		form = ConsumeForm(request.POST, instance = consume)
		if form.is_valid():
			consume = form.save(commit=False)
			consume.user = request.user
			consume.save()
			return redirect('consume_read', pk=consume.pk)
	else:
		form = ConsumeForm(instance = consume)
	return render(request, 'ac_book/consume_update.html', {'form':form})

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
				print("pasword = " + password)
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
