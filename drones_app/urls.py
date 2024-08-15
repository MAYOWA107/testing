from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (DroneCategoryView, CompetitionView, PilotView, DroneView)


router = DefaultRouter()
router.register("drones", DroneView, basename='drone')
router.register('drone-category', DroneCategoryView, basename='drone_categories')
router.register('competition', CompetitionView, basename='competition')
router.register('pilot', PilotView, basename='pilot')





urlpatterns = router.urls


#urlpatterns = [
    #Drone categoty url
    #path('drone-categories', DroneCategoryListView.as_view(), name='categories'),
    #path('drone-category/<int:pk>', DroneCategoryDetailView.as_view(), name='dronecategory-detail'),

    #Drone url
    #path('', include(router.urls)),
    #path('drones', DroneListView.as_view(), name='drones'),
    #path('drone/<int:pk>', DroneDetailView.as_view(), name='drone'),

    #competiton urls
   # path('competitions', CompetitionListView.as_view(), name='competitions'),
    #path('competition/<int:pk>', CompetitionDetailView.as_view(), name='competition'),

    #pilot urls
    #path('pilots', PilotListView.as_view(), name='pilots'),
    #path('pilot/<int:pk>', PilotDetailView.as_view(), name='pilot'),

#]