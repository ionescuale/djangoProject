from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from feedback.forms import FeedbackForm, FeedbackUpdateForm
from feedback.models import Feedback


# Create your views here.

class FeedbackCreateView(CreateView):
    template_name = 'feedback/create_feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('list-of-feedbacks')


class FeedbackListView(ListView):
    template_name = 'feedback/list_of_feedbacks.html'
    model = Feedback
    context_object_name = 'all_feedbacks'

class FeedbackUpdateView(UpdateView):
    template_name = 'feedback/update_feedback.html'
    model = Feedback
    form_class = FeedbackUpdateForm
    success_url = reverse_lazy('list-of-feedbacks')