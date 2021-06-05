from django.db import models

# Create your models here.

class Endpoint(models.Model):
    '''
    The Endpoint object represents ML API endpoint

    Attributes:
        name: The name of the endpoint, it will be used in API url,
        owner: The string with ownner name,
        created_at: The date when endpoint was created.
    '''
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)