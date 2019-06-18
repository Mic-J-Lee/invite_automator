from django.db import models

class Invite(models.Model):
    successful = models.BooleanField(default=False)
    github_handle = models.CharField(max_length=200, default='')
    zapier_payload = models.TextField(default='')
    github_response = models.TextField(default='')
