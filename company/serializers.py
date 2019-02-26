from rest_framework import serializers
from .models import Email

class EmailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Email
		fields = ('id', 'first_name','last_name','email','Phone_number','College_name','Qualification','attach')