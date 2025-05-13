from rest_framework import serializers
from .models import Item, Player, PlayerItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class PlayerItemSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())

    class Meta:
        model = PlayerItem
        fields = ["player", "item", "quantity"]

class PlayerSerializer(serializers.ModelSerializer):
    player_items = PlayerItemSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ["id", "name", "email", "player_items"]