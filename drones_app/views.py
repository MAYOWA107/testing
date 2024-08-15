from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets


from .models import Drone, DroneCategory, Pilot, Competition

from .serializers import Drone_CategorySerializer, DroneSerializer, CompetitionSerializer, PilotSerializer




class DroneCategoryView(viewsets.ModelViewSet):
    queryset = DroneCategory.objects.all()
    serializer_class = Drone_CategorySerializer



#class DroneCategoryDetailView(RetrieveUpdateDestroyAPIView):
 #   queryset = DroneCategory.objects.all()
  #  serializer_class = Drone_CategorySerializer


class DroneView(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class CompetitionView(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


#class CompetitionDetailView(RetrieveUpdateDestroyAPIView):
 #   queryset = Competition.objects.all()
  #  serializer_class = CompetitionSerializer



class PilotView(viewsets.ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer


#class PilotDetailView(RetrieveUpdateDestroyAPIView):
 #   queryset = Pilot.objects.all()
  #  serializer_class = PilotSerializer












