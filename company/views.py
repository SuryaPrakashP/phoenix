from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import EmailForm
from .models import Email

def home(request):
	return render(request,'index.html')

def login(request):
	return render(request,'login.html')

def car_page(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            xyz = form.save(commit=False)
            xyz.save()
            messages.success(request, "Details Submitted successfully submitted")
            return redirect('car_page')
    else:
        form = EmailForm()
    return render(request, 'career.html', {'form': form})

# def car_page(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             # process form data
#             obj = Email() #gets new object
#             obj.first_name = form.cleaned_data['first_name']
#             print(form.cleaned_data['first_name'])
#             obj.last_name = form.cleaned_data['last_name']
#             print(form.cleaned_data['last_name'])
#             obj.email = form.cleaned_data['email']
#             obj.Phone_number = form.cleaned_data['Phone_number']
#             obj.College_name = form.cleaned_data['College_name']
#             obj.Qualification = form.cleaned_data['Qualification']
#             obj.attach = form.cleaned_data['attach']
#             #finally save the object in db
# #            obj.save()
#             return render(request, 'career.html', {'form': form})
#         else:
#         	print("not is_valid")
#         	return HttpResponseRedirect('/')

    # else:
    # 	form = EmailForm()
    # 	return render(request, 'career.html', {'form': form})



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
