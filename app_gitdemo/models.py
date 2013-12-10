from django.db import models

class AWBS(models.Model): # model chua KHONG VAN DON
    number = models.CharField(max_length=15)        
    dateCreated = models.DateField()
        
# TODO: add new model