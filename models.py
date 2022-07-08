from django.db import models

class Client (models.Model):
  pnom=models.CharField(max_length=100)
  
  def __str__(self):
    return self.pnom
