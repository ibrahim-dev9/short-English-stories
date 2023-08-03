from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.title
