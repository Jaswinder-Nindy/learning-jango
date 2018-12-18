from django.forms import ModelForm
from .models import Schools, CheckExistedUser
from django import forms
#from django.core import validators
from django.core.exceptions import ValidationError


class SchoolForm(ModelForm):
	class Meta:
		model = Schools
		fields = '__all__'



class CollegeForm(forms.Form):
	name             = forms.CharField(max_length=100, required=True)
	confirm_name     = forms.CharField(max_length = 100, required= True)
	branch           = forms.CharField(max_length=100, required=True)
	regd_Number      = forms.IntegerField(required=True)

	def clean(self):
		cleaned_data = super(CollegeForm, self).clean()
		name         = self.cleaned_data.get('name')
		confirm_name = self.cleaned_data.get('confirm_name')

		if name != confirm_name:
			raise forms.ValidationError({"confirm_name":"Please check, name and confirm name fileds are do not match"})


class CheckExistedUserForm(ModelForm):
	name 	 = forms.CharField(max_length = 100, label=("Enter your name"))
	username = forms.CharField(max_length = 100)
	email    = forms.EmailField(max_length = 100)

	class Meta:
		model = CheckExistedUser
		fields = '__all__'

	def clean(self):
		cleaned_data = super(CheckExistedUserForm, self).clean()
		username_data = self.cleaned_data.get('username')
		email_data = self.cleaned_data.get('email')

		#existedmail = CheckExistedUser.objects.filter(email__icontains = email)

		if CheckExistedUser.objects.filter(email=email_data).exists():
			raise forms.ValidationError({"email": "This email is already existed, please try another one."})

		if CheckExistedUser.objects.filter(username = username_data).exists():
			raise forms.ValidationError({'username': 'This username is already has been taken, please try another one.'})
		


		