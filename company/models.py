from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Email(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.EmailField(max_length=25)
	Phone_number = PhoneNumberField(blank=True)
	College_name = models.CharField(max_length=25)
	Qualification = models.CharField(max_length=25)
	resume = models.FileField(upload_to ='img/',default=0)


	def __str__(self):
		return self.first_name