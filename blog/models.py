from django.db import models

# Create your models here.
class Sample(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title
    
