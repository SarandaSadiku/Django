from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class EmailManager(models.Manager):
    def validate(self, email_data):
        if len(email_data)<1:
            return(False, 'Field cannot be left blank!')
        elif not EMAIL_REGEX.match(email_data):
            return(False, 'Email is not valid!')
        else:
            return(True, 'Success! The email address you entered "{}"is a VALID email address! Thank You!'.format(email_data))

class Email(models.Model):
    email = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add =True)
    created_at = models.DateField(auto_now_add =True)

    objects = models.Manager()
    emailManager = EmailManager()
