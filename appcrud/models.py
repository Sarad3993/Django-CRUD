from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    email = models.EmailField()
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name
