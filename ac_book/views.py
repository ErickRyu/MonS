from django.shortcuts import render
from .models import Consume
from django.utils import timezone

def consume_list(request):
	consumes = Consume.objects.order_by('con_date')
	return render(request, 'ac_book/consume_list.html', {'consumes' : consumes})
