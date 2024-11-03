from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=2000)
    pronouns = models.CharField(max_length=255)

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    
class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=255)
class GroupTag(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)