from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk': self.pk})


class Project(models.Model):
    client = models.ForeignKey('Client', blank=True, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '<{}> {}'.format(self.client, self.name)

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})


# Create your models here.
class Entry(models.Model):
    start = models.DateTimeField(default=timezone.now)
    stop = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey('Project')
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return '[{} - {}] ({}) {}'.format(self.start, self.stop, self.project.name, self.description)

    def is_finished(self):
        return self.stop is not None
