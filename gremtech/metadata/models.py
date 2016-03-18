from django.db import models


class Metadata(models.Model):
    url_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    robots = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Metadata'

    def __str__(self):
        return self.url_name
