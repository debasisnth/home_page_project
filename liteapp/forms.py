from django import forms

#from django.core.mail import EmailMultiAlternatives


class ContactForm(forms.Form):

	fname = forms.CharField(label='First Name', max_length=50 ,required=True)
	lname = forms.CharField(label='Last Name', max_length=50, required=True)
	form_email = forms.EmailField(label='E-mail', max_length=50, required=True)
	subject = forms.CharField(label='Subject', max_length=50, required=True)
	message = forms.CharField(label='Message',max_length=360, widget=forms.Textarea)


	def message_template(self):


		html_content = f"""
		<p>
		{self.cleaned_data['fname']} {self.cleaned_data['lname']}({self.cleaned_data['form_email']}) has inquired on : 
		</p>
		<span>
		{self.cleaned_data['subject']}
		:</span> 
		<p>{self.cleaned_data['message']}</p>


		"""
		
		return html_content