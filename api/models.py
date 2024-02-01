from django.db import models

# Create your models here.

class Todo(models.Model):
    name           = models.CharField(max_length=100)
    description    = models.CharField(max_length=200)
    done           = models.BooleanField(default=False)
    date_created   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name