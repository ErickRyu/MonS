from django import forms
from .models import Consume, MyUser

class ConsumeForm(forms.ModelForm):
	class Meta:
		model = Consume
		fields = ('con_type', 'store_name', 'con_price', 'con_date', )


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = MyUser
		widgets = {
			'password': forms.PasswordInput(),
		}
		fields = ('email', 'date_of_birth', 'password')