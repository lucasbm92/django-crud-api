from django.db import models

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class PlayerItem(models.Model):
    player = models.ForeignKey(Player, related_name="player_items", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name="player_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.player.name} owns {self.quantity} of {self.item.name}"