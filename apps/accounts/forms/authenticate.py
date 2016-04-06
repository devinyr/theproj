from django import forms

class AuthenticationForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput)
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		fields = ['email', 'password']

	def clean(self):
		print "Cleaning *****"
		cleaned_data = super(AuthenticationForm, self).clean()
		return self.cleaned_data
