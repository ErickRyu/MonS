from django import forms
from .models import Consume

class ConsumeForm(forms.ModelForm):
	class Meta:
		model = Consume
		fields = ('con_type', 'store_name', 'con_price', 'con_date', 'user',)