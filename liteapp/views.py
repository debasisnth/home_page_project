from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from  .forms import ContactForm
from django.contrib import messages
from django.utils.translation import gettext as _

# Create your views here.



def home(request):

	desc=_('''
	Hi, I'm Debasis Nath, I am a <u>Python-Django</u>, <u>Pandas</u>,  <u>Ionic-Angular</u>, <u>AWS( Lambda, S3, EC2, IAM etc..)</u>, <u>Serverless Framework</u>, Core PHP, Symfony Developer, Linode Expert and AWS consultant.
    I have been working working as a Web developer with 3 years of experience in AWS(Lambda, S3, EC2, IAM etc..), Django, Core Php, Symfony 2.8, Mysql, PostgreSQL, Firebase, Javascript jQuery etc, have 4 years of experience in technical teaching. I am very much interested in Python Django development.
    I have done some projects in Django the linkes are updated in mt profile link. Also, I have a good understanding of <u>AWS</u>, EC2, Heroku, <u>GIT</u>, Docker, <u>Rasp-Berry Pi Projects</u>. 
	In school my favorite subject was Chemistry, If there any project which is related to Software development and Chemistry I will dive into it :) 
                
	''')

	alpha='https://era.thestudenthub.co.za/'
	beta='https://meet.thestudenthub.co.za'
	site3='https://booboocabs.com'
	app1='https://play.google.com/store/apps/details?id=com.booboocabs.com.ionic.driver'
	app2='https://play.google.com/store/apps/details?id=com.passenger.booboocabs.com'
	desc2= _(f'''				
		<p data-aos="flip-left">
			These are some projects which have been configured on my AWS EC2 instance: <b>1. </b>
			<a href="{alpha}"  target="_blank" > {alpha}: Symfony 2 Live Project </a>,
			<b>2. </b><a href="{beta}"  target="_blank" > {beta}:Jeetsi Meet Server maintained by me</a>,
			<b>3. </b><a href="{site3}"  target="_blank">{site3}:Python-Django Geo location related Live Project on Nginx(  Django ASGI Channel Chat Application integrated, development in progress...  )</a>
			<a href="{site3}/driver.home" target="_blank" >, Driver section of the same project</a>
			Apps I am currently working on( Ionic - Angular ): 
			i) <b><a href="{app1}">{app1}</a> </b>
			ii) <b><a href="{app2}">{app2}</a> </b>
		</p>

	''')



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


	return render(request, 'liteapp/index.html', {'desc':desc, 'desc2':desc2, 'form': form} )



def thanks(request):
	return HttpResponse("<H1>Thank You For Your Message</H1>")
	