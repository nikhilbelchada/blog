from django.db import models

# Create your models here.
class blog(models.Model):
    Title = models.CharField(max_length=20)
    Body = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.Title
