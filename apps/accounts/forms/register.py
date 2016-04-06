from django import forms
from apps.accounts.models import User

class RegistrationForm(forms.ModelForm):

	email = forms.EmailField(widget=forms.TextInput, label="Email")
	name = forms.CharField(widget=forms.TextInput, label="Name")
	password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")

	class Meta:
		model = User
		fields = ['email', 'name', 'alias','password1', 'password2']

	def clean(self):
		print "Cleaning *****"
		cleaned_data = super(RegistrationForm, self).clean()
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
		return self.cleaned_data

	def save(self, commit=True):
		print "Saving *****"
		user = super(RegistrationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		user.first_name = self.cleaned_data['name']
		user.username = self.cleaned_data['alias']
		print 'first name :'
		print user.first_name
		print 'User:'
		print user
		print 'username'
		print user.username
		if commit:
			print "Saving new user and pass"
			print user.first_name
			user.save()
		return user
