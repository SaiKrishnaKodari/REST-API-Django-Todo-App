from django.shortcuts import render
from rest_framework import viewsets

from .serializers import todoSerializer
from .models import todo
# Create your views here.
class todoViewSet(viewsets.ModelViewSet):
    queryset = todo.objects.all().order_by('task')
    serializer_class = todoSerializer