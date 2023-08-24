import random
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

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

        return redirect('login')




# form_valid() este apelata atunci cand userul trimte un formular cu datele completate si verificate validarile
# conform cregulilor definite in formular. In cadrul acestui form_valid() veti putea prelucra informatiile inainte
# ca ele sa fie salvate

# form_valid() este folosita in urmatoarele view-uri generice: CreateView si UpdateView