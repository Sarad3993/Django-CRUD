from django.db import models
from django.utils.safestring import mark_safe 

class Students(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    contact = models.CharField(max_length=50)
    


    def __str__(self):
        return self.name

    def image_tag(self):
        if self.picture.url is not None:
            return mark_safe(f'<img src="{self.picture.url}" height="60"/>')
        else:
            return "" 
    image_tag.short_description = 'Image'

    

