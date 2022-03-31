from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class TileImage(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    description_text = models.TextField()
    preview_img = models.ImageField(upload_to='prevs')
    image_img = models.ImageField(upload_to='pics')

