from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="")
    course = models.IntegerField(max_length=60, default="")
    instructor = models.CharField(max_length=60, default="")
    duration = models.FloatField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.title