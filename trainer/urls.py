from django.urls import path

from trainer import views

urlpatterns = [
    path('create_trainer/', views.TrainerCreateView.as_view(), name='create-trainer'),
    path('list_of_trainers/', views.TrainerListView.as_view(), name='list-of-trainers'),
    path('detailed_trainer/<int:pk>/', views.TrainerDetailedView.as_view(), name='detailed-trainer'),
    path('trainer_update/<int:pk>/', views.TrainerUpdateView.as_view(), name='update-trainer'),
    path('delete_trainer/<int:pk>/', views.TrainerDeleteView.as_view(), name='delete-trainer'),
]