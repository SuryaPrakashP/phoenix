from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
	class Meta:
		model = Email

		fields = ('first_name','last_name','email','Phone_number','College_name','Qualification','attach')




    
