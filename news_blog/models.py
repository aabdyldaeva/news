from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()


class Posts(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=500)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=300)
    comment_date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post
