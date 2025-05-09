from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name