from django.urls import path

from feedback import views

urlpatterns = [
    path('create_feedback/', views.FeedbackCreateView.as_view(), name='create-feedback'),
    path('list_of_feedbacks/', views.FeedbackListView.as_view(), name='list-of-feedbacks'),
    path('update_feedback/<int:pk>', views.FeedbackUpdateView.as_view(), name='update-feedback'),
]
