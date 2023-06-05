from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Benefit(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(CustomUser, on_delete = models.CASCADE )
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='benefits/')
    benefit_like = models.ManyToManyField(CustomUser, related_name='benefit_likes', blank = True)
    benefit_like_count = models.PositiveIntegerField(default = 0)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]
    
    