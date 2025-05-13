from rest_framework import viewsets
from .models import Item, Player, PlayerItem
from .serializers import ItemSerializer, PlayerSerializer, PlayerItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerItemViewSet(viewsets.ModelViewSet):
    queryset = PlayerItem.objects.all()
    serializer_class = PlayerItemSerializer