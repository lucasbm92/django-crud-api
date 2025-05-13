from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Player, Item, PlayerItem

class PlayerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.player_data = {"name": "John Doe", "email": "john.doe@example.com"}
        self.player = Player.objects.create(**self.player_data)
        self.item = Item.objects.create(name="Sword", description="A sharp blade")
        self.player_item_data = {"player": self.player, "item": self.item, "quantity": 2}
        self.player_item = PlayerItem.objects.create(**self.player_item_data)

    def test_create_player(self):
        response = self.client.post("/players/", {"name": "Jane Doe", "email": "jane.doe@example.com"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Jane Doe")

    def test_get_players(self):
        response = self.client.get("/players/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.player_data["name"])

    def test_update_player(self):
        response = self.client.put(f"/players/{self.player.id}/", {"name": "John Updated", "email": "john.updated@example.com"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "John Updated")

    def test_delete_player(self):
        response = self.client.delete(f"/players/{self.player.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Player.objects.count(), 0)

class ItemAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {"name": "Sword", "description": "A sharp blade"}
        self.item = Item.objects.create(**self.item_data)

    def test_create_item(self):
        response = self.client.post("/items/", {"name": "Shield", "description": "A sturdy shield"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Shield")

    def test_get_items(self):
        response = self.client.get("/items/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.item_data["name"])

    def test_update_item(self):
        response = self.client.put(f"/items/{self.item.id}/", {"name": "Sword Updated", "description": "An updated sharp blade"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Sword Updated")

    def test_delete_item(self):
        response = self.client.delete(f"/items/{self.item.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)

class PlayerItemAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.player = Player.objects.create(name="John Doe", email="john.doe@example.com")
        self.item = Item.objects.create(name="Sword", description="A sharp blade")
        self.player_item_data = {"player": self.player, "item": self.item, "quantity": 2}
        self.player_item = PlayerItem.objects.create(**self.player_item_data)

    def test_create_player_item(self):
        response = self.client.post("/player-items/", {"player": self.player.id, "item": self.item.id, "quantity": 5})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["quantity"], 5)

    def test_get_player_items(self):
        response = self.client.get("/player-items/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["quantity"], self.player_item_data["quantity"])

    def test_update_player_item(self):
        response = self.client.put(f"/player-items/{self.player_item.id}/", {"player": self.player.id, "item": self.item.id, "quantity": 10})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["quantity"], 10)

    def test_delete_player_item(self):
        response = self.client.delete(f"/player-items/{self.player_item.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PlayerItem.objects.count(), 0)