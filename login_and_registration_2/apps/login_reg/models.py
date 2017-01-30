from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register(self, form_data):
        print "here in usermanager  ",form_data['first_name']
        errors= []
        if not form_data['first_name']:
            errors.append('First name cannot be empty!')
        if len(errors)>0:
            return (False,errors)
        else:
            pass
            # return(True,user)

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)

    objects = UserManager()
