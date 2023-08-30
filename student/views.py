from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from student.forms import StudentForm, StudentUpdateForm
from student.models import Student, HistoryStudent


# Create your views here.

# CreateView -> folosit pt a genera un formular pe baza modelului si pt a salva datele in baza de date
# SuccessMessageMixin - folosit pt a afisa un mesaj de succes in momentul in care actiunea a fost realizata cu succes
class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list-of-students')
    success_message = '{f_name} {l_name}'
    permission_required = 'student.add_student'

    def form_valid(self, form):
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.first_name = new_student.first_name.title()
            new_student.last_name = new_student.last_name.title()
            new_student.email = new_student.email.lower()
            new_student.save()
            # History
            get_message = (f'Student {new_student.first_name} {new_student.last_name} was succesfully added by '
                           f'{self.request.user.username}')

            HistoryStudent.objects.create(message=get_message, created_at=datetime.now(), active=True,
                                          user_id=self.request.user.id)
            # self reprezinta instanta cureta a clasei respective
            # self este utilizat pentru a accesa diverse atribute si metode ale instantei

            # self.request.user.id -> reprezinta obiectul userului curent asociat cu cererea HTTP.
            # Este un obiect de tip User care contine informatii despre userul autentificat.

        return redirect('list-of-students')

    def get_success_message(self, cleaned_data):
        if self.object.gender == 'male':
            message = 'Mr. ' + self.success_message + ' ' + 'was successfully added'
        else:
            message = 'Miss ' + self.success_message + ' ' + 'was successfully added'
        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)


# ListView -> folosim pt a afisa inregistrarile din tabela student_student
class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "student/list_of_students.html"
    model = Student
    context_object_name = 'all_students'   # Student.objects.all()
    permission_required = 'student.view_list_of_students'

    # def get_context_data(self, **kwargs):
    #     pass

    # def get_queryset(self):
    #     return Student.objects.filter(active=True)


# UpdateView -> il folosim pentru a actualiza datele unui student
class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    permission_required = 'student.change_student'

    def get_success_url(self):
        return reverse('detailed-student', args=[str(self.object.id)])


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')
    success_message = '{f_name} {l_name}'
    permission_required = 'student.delete_student'

    def get_success_message(self, cleaned_data):
        message = self.success_message + ' ' + 'was successfully deleted'
        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)


class StudentDetailedView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student/detailed_student.html'
    model = Student
    permission_required = 'student.view_student'

@login_required()
def search(request):
    get_value = request.GET.get('filter')
    if get_value:
        students = Student.objects.filter(Q(last_name__icontains=get_value) | Q(first_name__icontains=get_value))
    else:
        students = Student.objects.all()

    return render(request, 'student/list_of_students.html', {'all_students': students})
    # return redirect('list-of-students')


@login_required()
def assigned_students(request):
    get_value = request.GET.get('trainer_id')

    if get_value:
        students = Student.objects.filter(trainer_id=get_value)
    else:
        students = Student.objects.all()

    context = {
        'all_students': students
    }

    return render(request, 'student/assigned_students.html', context)
