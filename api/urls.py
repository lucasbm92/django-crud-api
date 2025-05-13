from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, PlayerViewSet, PlayerItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'player-items', PlayerItemViewSet, basename='playeritem')

urlpatterns = [
    path('', include(router.urls)),
]