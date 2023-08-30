from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from feedback.models import Feedback
from student.models import Student
from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer, HistoryTrainer


# Create your views here.

# CreateView -> folosit pt a genera un fomrular pe baza modelului si pt a salva datele in baza de date
class TrainerCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('list-of-trainers')
    success_message = '{f_name} {l_name}'
    permission_required = 'trainer.add_trainer'

    def form_valid(self, form):
        if form.is_valid():
            new_trainer = form.save(commit=False)
            new_trainer.first_name = new_trainer.first_name.title()
            new_trainer.last_name = new_trainer.last_name.title()
            new_trainer.email = new_trainer.email.lower()

            user_id = self.request.user.id
            user_username = self.request.user.username

            get_message = (f'Trainer {new_trainer.first_name} {new_trainer.last_name} was added sucesfully by '
                           f'{user_username}')

            HistoryTrainer.objects.create(message=get_message, created_at=datetime.now(), user_id=user_id)

        return redirect('list-of-trainers')

    def get_success_message(self, cleaned_data):
        message = self.success_message + ' ' + 'was successfully added'
        print(message)
        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)


# ListView -> folosim pt a afisa inregistrarile din tabela trainer

class TrainerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'trainer/list_of_tainers.html'
    model = Trainer
    context_object_name = 'all_trainers'
    permission_required = 'trainer.view_list_of_trainers'


class TrainerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')
    success_message = '{f_name} {l_name}'
    permission_required = 'trainer.delete_trainer'

    def get_success_message(self, cleaned_data):
        message = self.success_message + ' ' + 'was successfully deleted'
        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)


class TrainerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    permission_required = 'trainer.change_trainer'

    def get_success_url(self):
        return reverse('detailed-trainer', args=[str(self.object.id)])


class TrainerDetailedView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'trainer/detailed_trainer.html'
    model = Trainer
    permission_required = 'trainer.view_trainer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()  # preluam data curenta
        context['current_datetime'] = now  # adaugam in dict context cheia current_datetime pt a afisa data/ora curenta
        # print(context['current_datetime'])
        # print(context)

        current_trainer_id = self.kwargs['pk']  # avem acces la id-ul trainerului respectiv
        # print(current_trainer_id)

        # students = Student.objects.filter(trainer_id=current_trainer_id)  # realizam un query prin care luam toti
        # # studentii asignati trainerului
        # context['students'] = students  # trimitem in interfata pe baza cheii students, toti studentii
        # # asignati trainerului respectiv
        # # print(students)

        feedbacks = Feedback.objects.filter(trainer_id=current_trainer_id)
        context['feedback'] = feedbacks
        return context


# get_context_data() este o metoda folosita in clasele de view-uri (ListView, TemplateView, UpdateView,
# CreateView, FormView, etc) care este utilizata pentru a construi si returna un dictionar de date de
# context care vor fi afisate in paginile HTML
