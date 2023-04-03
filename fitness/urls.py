from django.urls import path
from .views import WorkoutList, WorkoutDetail, ExerciseList, ExerciseDetail

urlpatterns = [
    path('workouts/', WorkoutList.as_view(),name='workout-list'),
    path('workouts/<int:pk>/', WorkoutDetail.as_view(),name='workout-detail'),
    path('exercises/', ExerciseList.as_view(),name='exercise-list'),
    path('exercises/<int:pk>/', ExerciseDetail.as_view(),name='exercise-detail'),
]