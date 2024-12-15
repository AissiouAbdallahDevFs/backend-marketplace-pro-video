from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessionalViewSet, ReservationViewSet

router = DefaultRouter()
router.register('professionals', ProfessionalViewSet, basename='professional')
router.register('reservations', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls)),
]
