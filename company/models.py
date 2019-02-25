from django.db import models

# Create your models here.
class Email(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.EmailField(max_length=25)
	Phone_number = models.IntegerField()
	College_name = models.CharField(max_length=25)
	Qualification = models.CharField(max_length=25)
	attach = models.FileField(upload_to ='media',default=True)

	def __str__(self):
		return self.first_name