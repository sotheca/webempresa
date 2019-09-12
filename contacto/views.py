from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactoForm

# Create your views here.
def contacto(request):
	contact_form = ContactoForm()

	if request.method == "POST":
		contact_form = ContactoForm(data=request.POST)
		if contact_form.is_valid():
			name = request.POST.get('name', '')
			email = request.POST.get('email', '')
			content = request.POST.get('content', '')
			#Enviamos el correo y redireccionamos
			email = EmailMessage(
				"La Caffettiera: Nuevo mensaje de contacto",
				"De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
				"no-contestar@inbox.mailtrap.io",
				["lansoto.92@gmail.com"],
				reply_to=[email]
			)

			try:
				email.send()
				#Algo no ha ido bien, redireccionamos a OK
				return redirect(reverse('contact')+"?ok")
			except:
				#Algo no ha ido bien, redireccionamos a FAIL
				return redirect(reverse('contact')+"?fail")

	return render(request,"contacto/contact.html",{'form':contact_form})
