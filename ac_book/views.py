from django.shortcuts import render, get_object_or_404, redirect
from .models import Consume
from django.utils import timezone
from .forms import ConsumeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def consume_list(request):
	consumes = Consume.objects.order_by('-con_date')
	return render(request, 'ac_book/consume_list.html', {'consumes' : consumes})

def consume_detail(request, pk):
	consume = get_object_or_404(Consume, pk=pk)
	return render(request, 'ac_book/consume_detail.html', {'consume':consume})


@login_required
def consume_new(request):
	if request.method == "POST":
		form = ConsumeForm(request.POST)
		if form.is_valid():
			consume = form.save(commit=False)
			consume.user = request.user
			consume.save()
			return redirect('consume_detail', pk=consume.pk)
	else:
		form = ConsumeForm()
	return render(request, 'ac_book/consume_edit.html', {'form':form})

@login_required
def consume_edit(request, pk):
	consume = get_object_or_404(Consume, pk = pk)
	if request.method == "POST":
		form = ConsumeForm(request.POST, instance = consume)
		if form.is_valid():
			consume = form.save(commit=False)
			consume.user = request.user
			consume.save()
			return redirect('consume_detail', pk=consume.pk)
			#return redirect('ac_book.views.consume_detail', pk=consume.pk)
	else:
		form = ConsumeForm(instance = consume)
	return render(request, 'ac_book/consume_edit.html', {'form':form})

@login_required
def consume_remove(request, pk):
  consume = get_object_or_404(Consume, pk=pk)
  consume.delete()
  #return redirect('ac_book.views.consume_list')
  return redirect('consume_list')


def logout_view(request):
	logout(request)
	# return redirect('/')
