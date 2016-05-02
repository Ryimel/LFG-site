from django.db import models
import datetime

class User(models.Model):
    user_id = models.IntegerField()
    nickname = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=12)
    second_name = models.CharField(max_length=12)
    email = models.EmailField()
    description = models.CharField(max_length=200)
    reg_time = models.DateTimeField()
    def __str__(self):
        return self.nickname
    
    
    
class Team(models.Model):
    team_id = models.IntegerField()
    name = models.CharField(max_length=20)    
    owner_id = models.IntegerField()
    description = models.CharField(max_length=200, default = '')
    teammates_list = models.ForeignKey(User)
    def __str__(self):
        return self.name
