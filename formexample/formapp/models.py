from django.db import models

class Person(models.Model):
    class Meta:
        verbose_name_plural = 'People'
        
    name = models.CharField(max_length=30)
    awesome = models.BooleanField()

    def __str__(self):
        return '{} ({})'.format(self.name, 'Totally Awesome' if self.awesome else 'Lame')
