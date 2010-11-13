from django.db import models

class Track(models.Model):
    url = models.CharField('Faixa', max_length=255)

    def __unicode__(self):
        return self.url
