from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import EmailForm
from .models import Email
from django.http import Http404
# from .serializers import EmailSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

def home(request):
	return render(request,'index.html')

def login(request):
	return render(request,'login.html')

def car_page(request):
    if request.method == "POST":
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Details Submitted successfully submitted")
            return redirect('car_page')
    else:
        form = EmailForm()
    return render(request, 'career.html', {'form': form})


# class EmailList(APIView):
# 	def get(self, request, format=None):
# 		users = Email.objects.all()
# 		serializer = EmailSerializer(users, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializer = EmailSerializer(data=request.DATA)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		contact = request.POST['contact']
		subject = request.POST['subject']
		send_mail('Contact Form',
			"name: "+str(name)+"\n"
	        "email:"+str(email)+"\n"
	        "contact:"+str(contact)+"\n"
	        "subject :"+ str(subject),
		 settings.EMAIL_HOST_USER,
		 ['manifz90@gmail.com'], 
		 fail_silently=False)
	return render(request,'contact.html')	
