from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=40, null=False)
    completed= models.BooleanField()

    def __str__(self):
        return self.title