from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="photos"
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.title