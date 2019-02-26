from django.db import models



# Create your models here.
class Email(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.EmailField(max_length=25)
	Phone_number = models.IntegerField(null=False, blank=False, unique=True)
	College_name = models.CharField(max_length=25)
	Qualification = models.CharField(max_length=25)
	# resume = models.FileField(upload_to ='img/')

	def __str__(self):
		return self.first_name