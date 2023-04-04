from rest_framework import viewsets, permissions
from .models import Workout, Exercise, FitnessData
from .serializers import WorkoutSerializer, ExerciseSerializer, FitnessDataSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)
    
    
class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FitnessDataViewSet(viewsets.ModelViewSet):
    serializer_class = FitnessDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FitnessData.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

