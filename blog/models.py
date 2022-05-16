from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#users are going to author posts-one to many relationships
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)#(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    #if the user is deleted, delete their posts as well

# Create your models here.
# django orm(Object relational map)
#migrations are useful as we are allows to make changes even if the database has already been created
