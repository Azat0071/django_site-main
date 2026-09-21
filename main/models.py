from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()

    def str(self):
        return self.name