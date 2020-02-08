from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from  .forms import ContactForm
from django.contrib import messages

# Create your views here.



def home(request):

	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			fname= form.cleaned_data['fname']
			lname= form.cleaned_data['lname']
			form_email= form.cleaned_data['form_email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			try:
				# send_mail(
				#     'Subject here',
				#     'Here is the message.',
				#     'from@example.com',
				#     ['to@example.com'],
				#     fail_silently=False,
				# )
				send_mail(
				    subject,
				    form.message_template(), # If content_type is text/plain
				    form_email,
				    ['debasisnth@gmail.com'],
				    fail_silently=False,
				    html_message=form.message_template(),  # If content_type is text/html
				)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			else:
				messages.add_message(request, messages.INFO, f'Thanks for sending mail! {fname}!')
				return redirect('liteapp-home')
			finally:
				pass


	return render(request, 'liteapp/index.html', {'form': form} )



def thanks(request):
	return HttpResponse("<H1>Thank You For Your Message</H1>")
	