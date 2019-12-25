from django.db import models
from django.conf import settings

# Create your models here.
class tweet(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tweet_content = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.tweet_content)
