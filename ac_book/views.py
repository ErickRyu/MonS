from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Consume
from django.utils import timezone
from .forms import ConsumeForm

from django.conf.urls import include


def consume_list(request):
	consumes = Consume.objects.order_by('con_date')
	return render(request, 'ac_book/consume_list.html', {'consumes' : consumes})

def consume_detail(request, pk):
	consume = get_object_or_404(Consume, pk=pk)
	return render(request, 'ac_book/consume_detail.html', {'consume':consume})

def consume_new(request):
	if request.method == "POST":
		form = ConsumeForm(request.POST)
		if form.is_valid():
			consume = form.save(commit=False)
			consume.save()
			return redirect('consume_detail', pk=consume.pk)
	else:
		form = ConsumeForm()
	return render(request, 'ac_book/consume_edit.html', {'form':form})