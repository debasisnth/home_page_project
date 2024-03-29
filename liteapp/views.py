from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.contrib import messages
from django.utils.translation import gettext as _


# Create your views here.


def home(request):
    desc = _('''
	
	Hi, I'm Debasis Nath, I am a Python/Full-Stack senior software Developer/Engineer.
	I am writing this portfolio not only to show my love for IT but I want
	to show my ability to work on architecture related issues and take full
	ownership of any project. Currently I have 3.75 years of experience in
	IT.  I have hands on experience on <u>React</u> <u>Python</u>, <u>Serverless framework</u>,
	<u>AWS CloudFormation</u>, <u>Django</u>, <u>Docker</u>, <u>Pandas</u>, <u>AWS(Lambda, S3, EC2, IAM, Textract,
	Rekognition etc..)</u>, <u>Git</u>, Core Php, Symfony, Mysql, PostgreSQL,
	Firebase, Java-script, Ionic-Angular, jQuery, etc... I also have 4 years of
	experience in technical teaching. As well as good understanding of Heroku,
	Docker, <u>Rasp-Berry Pi</u> Projects etc..
	<div>I am enthusiastic and interested in working on DataEngineering(Python, PySpark, databricks) / AWS cloud based projects .</div>	

	''')

    desc.replace('\n', ' ')

    alpha = 'https://era.thestudenthub.co.za/'
    beta = 'https://meet.thestudenthub.co.za'
    site3 = 'https://shyamsteel.tech:8002/admin/'
    # app1='https://play.google.com/store/apps/details?id=com.booboocabs.com.ionic.driver'
    # app2='https://play.google.com/store/apps/details?id=com.passenger.booboocabs.com'
    desc2 = _(f'''				
		<p data-aos="flip-left">
			These are some projects which have been configured on our AWS EC2 instance: <b>1. </b>
			<a href="{alpha}"  target="_blank" > {alpha}: Symfony Live Project </a>,
			<b>2. </b><a href="{beta}"  target="_blank" > {beta}:Jeetsi Meet Server maintained by me</a>,
			<b>3. </b><a href="{site3}"  target="_blank">{site3}:Python-Django based DRF Project</a>
		</p>

	''')

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            form_email = form.cleaned_data['form_email']
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
                    form.message_template(),  # If content_type is text/plain
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

    return render(request, 'liteapp/index.html', {'desc': desc, 'desc2': desc2, 'form': form})


def thanks(request):
    return HttpResponse("<H1>Thank You For Your Message</H1>")
