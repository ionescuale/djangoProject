import random
from datetime import datetime

from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserForm
from userextend.models import History


# Create your views here.

class UserCreateView(CreateView):
    template_name = 'userextend/create-user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            # atribui valoarea new_user.first_name.title() campului first_name al obiectlui new_user
            # new_user.username = new_user.first_name[0].lower()+new_user.last_name.lower()+'_'+str(randrange(100000, 999999))
            new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{random.randint(100000, 999999)}'

            new_user.save()

            # History
            get_message = (f'Userul a fost adaugat cu succes Username: {new_user.username}, email: {new_user.email}, '
                           f'first name:{new_user.first_name}, last name: {new_user.last_name}')

            History.objects.create(message=get_message, created_at=datetime.now(), active=True)

            # Trimite mail FARA TEMPLATE
            # subject = 'Adding a new account'
            # message = f'Congratulations! Your username is {new_user.username}.'

            # send_mail() -> este o functie in cadrul frameoworkului care faciliteaza trimiterea de emailuri

            # send_mail(subject, message, 'george@pop.ro',[new_user.email]) # se foloseste cand in settings.py avem console
            # send_mail(subject, message, EMAIL_HOST_USER, [new_user.email]) # se foloseste cand in settings.py avem smtp

            # Trimite mail CU TEMPLATE

            details_user = {
                'fullname':f'{new_user.first_name} {new_user.last_name}',
                'username': new_user.username
            }
            subject = 'Adding a new account'
            message = get_template('mail.html').render(details_user)

            mail = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [new_user.email]
            )
            mail.content_subtype = 'html'
            mail.send()

        return redirect('login')




# form_valid() este apelata atunci cand userul trimte un formular cu datele completate si verificate validarile
# conform cregulilor definite in formular. In cadrul acestui form_valid() veti putea prelucra informatiile inainte
# ca ele sa fie salvate

# form_valid() este folosita in urmatoarele view-uri generice: CreateView si UpdateView